# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 16:03:02 2018

@author: Administrator
"""

import os
from pmipy import log
from pmipy import pmi
from tqdm import tqdm
import numpy as np
import pandas as pd
from pmipy import getOcmData
from pmipy import getTargetCoordinate as gtc
import multiprocessing as mp

logger = log.createLogger(__name__)

MongoDB = 'Claudius'
collection = 'TileData'
testDB = 'ClaudiusTest'

client16 = pmi.connOcm16()

coll = client16[testDB][collection]
# 获取经纬度坐标矩阵
ll = getOcmData.OCMLatLng()

# 创建grid
def createNewClaudius(meter):
    collOld = client16[MongoDB][collection]
    collNew = coll
    cursor = collOld.find({'meters': meter, 'processTime':'201711'},{'tileName': 1,'province':1, 
                       'city': 1, 'region': 1, 'polygon': 1, 'meters': 1, '_id': 0}, no_cursor_timeout=True)
    for document in cursor:
        collNew.insert_one(document)

# 获取含省市区，tileName和polygon信息
def getCityTile(collection, city, meter=1000, processTime='201807'):
    cursor = collection.find({'city':city, 'meters': meter, 'processTime':processTime},{'tileName': 1, 
                             'city': 1,  'polygon': 1, '_id': 0}, no_cursor_timeout=True)
    #tempPath = pmi.commonTempPath()
    #tileFilePath = os.path.join(tempPath, 'tileName_{}.csv'.format(meter))
    #df = pd.DataFrame(list(cursor))
    documentList = []
    for document in cursor:
        ploygon = eval(document['polygon'])
        document['lng1'] = ploygon[0][0]
        document['lng2'] = ploygon[2][0]
        document['lat1'] = ploygon[0][1]
        document['lat2'] = ploygon[2][1]
        documentList.append(document)
    
    df = pd.DataFrame(documentList)
    return df


# ***注：执行此函数必须保证df_tile, df_point的经纬度排过序（small->big）
# 根据源数据点位的经纬度统计我ocm单元格的点位数,
# 网格四个顶点的顺序：左下角-左上角-右上角-右下角
def aggSum(df_tile, df_point, apex, pLL, pValue, tag):
    """
    (lng1,lat2) -- (lng2,lat2)
         |            |
    (lng1,lat1) -- (lng2,lat1)
    """
    # 检查df_tile的信息是否完整
    
    tileMin1 = df_tile[apex[0]].iloc[0]
    tileMin2 = df_tile[apex[2]].min()
    tileMax2 = df_tile[apex[3]].max()
    df_point = df_point[(df_point[pLL[0]]>=tileMin1)&(df_point[pLL[1]]>=tileMin2)&(df_point[pLL[1]]<=tileMax2)]
    # 叠加网格内的点位置
    pointValuesList = []
    for lng1, lng2, lat1, lat2 in tqdm(df_tile[apex].values):
        pointValues = 0
        """
        # 删除dataframe或list耗时低效，运算时间反而边长，因此下列被注释掉的代码放弃使用
        _list = df_point.loc[:, [pLL[0],pLL[1],pValue]].values.tolist()
        for lng,lat,value in _list:
            if (lng1 < lng <= lng2) & (lat1 < lat <= lat2):
                pointValues += value
                _list.remove([lng,lat,value])
            elif lng > lng2:
                break
        """
        for lng,lat,value in df_point.loc[:, [pLL[0],pLL[1],pValue]].values:
            if (lng1 < lng <= lng2) & (lat1 < lat <= lat2):
                pointValues += value
            elif lng > lng2:
                break

        pointValuesList.append(pointValues)
    df_tile[tag] = pointValuesList
    return df_tile


# 可用于圆形单元区域的点位数量统计
def cpuAccelerator(df_tile, df_point, pLng='lng', pLat='lat', pValue='count', tag='ycx', core_num='max'):
    core_max = mp.cpu_count()
    if core_num != 'max':
        try:
            ncore = int(core_num)
            core_num = ncore if ncore <= core_max else core_max
        except ValueError:
            logger.info('请输入正确的进程数(整数值)！')
            raise SystemExit
    else:
        core_num = core_max
    # 确保有序lng, lat有序
    # 计算经纬度跨度
    lngSpan = df_tile['lng2'].iloc[-1] - df_tile['lng1'].iloc[0]
    latSpan = df_tile['lat2'].iloc[-1] - df_tile['lat1'].iloc[0]
    # 对比城市横向和纵向的跨度
    if lngSpan + 5 >= latSpan: # 目前还没有证据证明经纬度排序先后会影响运算效率！
        apex = ['lng1','lng2','lat1','lat2']
        pLL = [pLng, pLat]
    else:
        apex = ['lat1','lat2', 'lng1','lng2']
        pLL = [pLat, pLng]
    
    df_tile.sort_values(apex[:2], inplace=True)
    df_point.sort_values(pLL, inplace=True)
    df_split = np.array_split(df_tile, core_num)
    p = mp.Pool(processes=core_num) 
    funcList = []

    for df in df_split:
        f = p.apply_async(aggSum, args=(df, df_point, apex, pLL, pValue, tag))
        funcList.append(f)

    logger.info('开始各进程运算...')
    p.close()
    p.join()
    resList = []
    for f in funcList:
        resList.append(f.get(timeout=0.5))
    df_all = pd.concat(resList)
    return df_all



def mapTile(df_point, ll, pLng, pLat):
    tileList = []
    for lng, lat in df_point[[pLng, pLat]].values:
        tileName = ll.getTileName(lng, lat)
        tileList.append(tileName)
    df_point['tileName'] = tileList
    return df_point


def cpuAccelerator2(df_point, ll, pLng='lng', pLat='lat', point='count', tag='moveIndex', core_num='max'):
    core_max = mp.cpu_count()
    if core_num != 'max':
        try:
            ncore = int(core_num)
            core_num = ncore if ncore <= core_max else core_max
        except ValueError:
            logger.info('请输入正确的进程数(整数值)！')
            raise SystemExit
    else:
        core_num = core_max


    df_split = np.array_split(df_point, core_num)
    p = mp.Pool(processes=core_num) 
    funcList = []

    for df in df_split:
        f = p.apply_async(mapTile, args=(df, ll, pLng, pLat, ))
        funcList.append(f)

    logger.info('开始多进程运算...')
    p.close()
    p.join()
    resList = []
    for f in funcList:
        resList.append(f.get(timeout=0.5))
    df_all = pd.concat(resList)
    df_all = df_all[['tileName', point]].groupby('tileName').sum()
    df_all = df_all.rename(columns={point:tag})
    logger.info('结束多进程运算！')
    return df_all


# 更新宜出行文档
@pmi.execInfo()
def updateYCX(cityList=['厦门市', '莆田市'], dbName='ycx', ycxTable='ycx_scale20181226', 
              meter=1000, processTime='201807'):
    # 按城市更新--思路：先获取已有宜出行数据的城市名单
    cm = pmi.ConnMysql(dbName)
    city_name = 'city_name'
    pValue = 'count'
    moveIndex = 'moveIndex'
    filePath='地级市常住人口.xlsx'
    try:
        df_pop = pd.read_excel(filePath).set_index('city')
    except FileNotFoundError:
        logger.warning('{}文件不存在，请补充此文件！'.format(filePath))
        raise SystemExit
    logger.info('准备从{}数据库的{}数据表中获取宜出行数据...'.format(dbName, ycxTable))
    sql_info = "select distinct {}, time from `{}`".format(city_name, ycxTable)
    df_info = pd.read_sql(sql_info, cm.engine).set_index(city_name)
    if not len(cityList):
        cityList = list(df_info.index.drop_duplicates())
    logger.info('准备处理如下城市的宜出行数据：\n{}'.format(cityList))
    def getCityYCX(city, date=''):
        sql = "SELECT  count / max_data as count, lng, lat FROM `{}` where {}='{}' and time='{}'".format(ycxTable, 
                                                                 city_name, city, date)
        df_city = pd.read_sql(sql, cm.engine)
        return df_city

    # 将宜出行高德经纬度转百度经纬度
    def gaode2baidu(df_point):
        logger.info('高德坐标转百度坐标...')
        df_point = gtc.transform(df_point, ['lng','lat'], 'gaode', 'baidu')
        df_point.drop(['lng','lat'], axis=1, inplace=True)
        df_point.rename(columns={'baidu经度':'lng','baidu纬度':'lat'}, inplace=True)
        logger.info('完成坐标转换！')
        return df_point

    # 获取地级市常住人口数据，计算宜出行校正系数cof

    def getPermanentPop(df_pop, city):
        try:
            permanentPop = df_pop.loc[city]['常住人口（人）']
            return permanentPop
        except KeyError:
            logger.warning('{}的常住人口数据不存在或存在异常,本次将跳过该城市的更新！'.format(city))
            return 0
            
    def _getYCXdf(city, t):
        df_point = getCityYCX(city, date=t)
        """
        # 运行速度已经很快，目前觉得没有必要存放到本地
        ycxCityFileName = '_{}_{}_{}人流指数.xlsx'.format(meter,city, t)
        if os.path.exists('./'+ycxCityFileName):
            logger.info('{}宜出行数据已在本地存储，跳过处理阶段！'.format(city))
            df_point = pd.read_excel(ycxCityFileName)
        """
        df_point = gaode2baidu(df_point)
        cof = permanentPop / df_point[pValue].sum()
        # 之前的耗能算法为df_ycx = cpuAccelerator(df_tile, df_point, tag=moveIndex)  
        df_ycx = cpuAccelerator2(df_point, ll, tag=moveIndex)  
        df_ycx['moveValue'] = df_ycx[moveIndex] * cof
        df_ycx['moveValue'] = df_ycx['moveValue'].round()
        df_ycx[moveIndex] = df_ycx[moveIndex].round(3)
        df_ycx['crawlTime'] = t
        return df_ycx
    # 获取坐标矩阵
    ll.serialize()
    for city in cityList:
        cityYCXFile = '{}宜出行数据.xlsx'.format(city)
        permanentPop = getPermanentPop(df_pop, city)
        if os.path.exists(cityYCXFile):
            logger.info('检测到{}宜出行数据已在本地存储，本次项目忽略该城市的更新！'.format(city))
            continue
        if not permanentPop:
            continue
        logger.info('准备更新{}的数据...'.format(city))
        # logger.info('获取{}的网格编号及各定点的经纬度信息...'.format(city))
        # df_tile = getCityTile(coll, city)
        timeList = list(df_info.loc[city]['time'])
        logger.info('获取/处理宜出行数据...')
        for i, t in enumerate(timeList): # 目前的date为字符串格式
            logger.info('处理<{}>时间段的数据...'.format(t))
            if not i:
                df_ycx = _getYCXdf(city, t)
            else:
                df_ycx = pd.concat([df_ycx, _getYCXdf(city, t)])
        df_ycx.to_excel(cityYCXFile)
        df_ycx2 = pd.pivot_table(df_ycx, index='tileName', columns=['crawlTime'], values=[moveIndex, 'moveValue'])
        ## 需对缺失值进行填0
        df_ycx2 = df_ycx2.fillna(0)
        # 计算栅格所有时间段的move平均值
        df_ycx2[(moveIndex,'mean')]  = df_ycx2[moveIndex].mean(axis=1).round(3)
        df_ycx2[('moveValue','mean')] = df_ycx2['moveValue'].mean(axis=1).round()
        mvDict = df_ycx2['moveValue'].to_dict('index') # moveValue
        miDict = df_ycx2[moveIndex].to_dict('index')
        logger.info('准备更新数据至{}数据库的{}集合中...'.format(testDB, collection))
        for tn in tqdm(mvDict.keys()):
            coll.update_one({'tileName':tn, 'meters':meter, 'processTime':processTime}, 
                            {'$set': {'ycx':{'moveValue':mvDict[tn], 'moveIndex':miDict[tn]}}})
        logger.info('完成{}的宜出行数据更新！\n'.format(city))


# 更新Linx数据
@pmi.execInfo()
def updateLinx(dbName='linxdata', table='linx_js', meter=1000, processTime='201807'):
    logger.info('准备从{}数据库的{}数据表中获取Linx数据...'.format(dbName, table))
    cm = pmi.ConnMysql(dbName)
    #sql_info = "select distinct 城市名称 from `{}` where 城市级别 != 'c'".format(table)
    #df_info = pd.read_sql(sql_info, cm.engine).set_index('城市名称')
    #logger.info('准备处理如下城市的Linx数据：\n{}'.format(cityList))
    def getCityLinxSales(city):
        sql = "SELECT 销售分数 as saleScore, baidu经度 as lng, baidu纬度 as lat FROM `{}` where 城市名称='{}'".format(table, city)
        df_city = pd.read_sql(sql, cm.engine)
        return df_city
    def getLinxSales():
        sql = "SELECT 销售分数 as saleScore, baidu经度 as lng, baidu纬度 as lat FROM `{}`".format(table)
        df = pd.read_sql(sql, cm.engine)
        return df
    
    ll.serialize()
    logger.info('从{}数据库的{}数据表获取LinxData数据！'.format(dbName, table))
    df = getLinxSales()
    tileNameList = []
    for l1, l2 in df[['lng', 'lat']].values:
        tileName = ll.getTileName(l1, l2)
        tileNameList.append(tileName)
    
    df['tileName'] = tileNameList
    # 简单计算各tile的销售分数
    #df.to_excel('LinxData格子编号验证.xlsx')
    df_sales = df[['tileName','saleScore']].groupby('tileName').sum()
    for tn in tqdm(df_sales.index):
        coll.update_one({'tileName':tn, 'meters':meter, 'processTime':processTime}, 
                        {'$set': {'LinxData':{'销售分数':df_sales.loc[tn]['saleScore']}}})
    logger.info('完成LinxData的更新！\n')

# 更新tileData的行政区标签
@pmi.execInfo()
def updateAdmin(dbName='gaode_admin', table='Jiangsu', dbType='mongodb', meter=1000, processTime='201807'):
    logger.info('准备从{}数据库的{}数据表中获取高德行政区划数据...'.format(dbName, table))
    if dbType == 'mongodb':
        client = pmi.connOcm16()
        collGD = client[dbName][table]
        cursor = collGD.find({},{'tileName':1, "province":1, "city":1, "region":1,"township":1, "_id":0})
        for doc in cursor:
            if doc['province'] == [ ]:  # 使用“高德外围”替换[ ]
                doc['province'] = '高德外围'
                doc['city'] = '高德外围'
                doc['region'] = '高德外围'
                doc['township'] = '高德外围'

            else: 
                if doc['city'] == []:
                    doc['city'] = None
                if doc['region'] == []:
                    doc['region'] = None
                if doc['township'] == []:
                    doc['township'] = None
            coll.update_one({'tileName':doc['tileName'], 'meters':meter, 'processTime':processTime}, 
                            {'$set': {'province':doc['province'], 'city':doc['city'], 'region':doc['region'], 
                                      'township':doc['township']}})

        logger.info('完成{}高德行政区划信息的更新！'.format(table))


    elif dbType in ['mysql', 'sql']:
        def getGDAdmin2():
            cm = pmi.ConnMysql(dbName)
            sql = "SELECT tileName, province, city, region, township FROM `{}`".format(table)
            df = pd.read_sql(sql, cm.engine)
            return df
        df = getGDAdmin2()
        for tn, prov, ct, reg, ts in tqdm(df.values):
            coll.update_one({'tileName':tn, 'meters':meter, 'processTime':processTime}, 
                            {'$set': {'province':prov, 'city':ct, 'region':reg, 'township':ts}})
        logger.info('完成高德行政区划信息的更新！')
    else:
        logger.warning('请检查数据库类型是否正确，或者{}数据库类型的读取功能有待开发！'.format(dbType))
        raise SystemExit


if __name__== '__main__':
    city = '南京市'
    updateYCX(city)

