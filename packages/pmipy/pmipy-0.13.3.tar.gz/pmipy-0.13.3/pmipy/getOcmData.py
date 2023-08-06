# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 21:38:10 2018

@author: jasonai
"""


from pmipy import log
from pmipy import pmi
from tqdm import tqdm
import pandas as pd
import os
#from pmipy.support import prov_mapp
from pmipy.OCM import getTileName
from pmipy.OCM import getFactor 

logger = log.createLogger(__name__)


# 根据经纬度获取网格编号
def getTileByLngLat(filePath, lnglat, dbName='Claudius', boundColl='GeoBoundary', outfile='', ):
    ll = getTileName.OCMLatLng(dbName, bondColl)
    ll.serialize()
    result = pmi.readXlsCsv(filePath)
    df, path, fileName = result['data'], result['path'], result['file']
    df_ll = df[list(lnglat)]
    recordList = []
    for lng, lat in tqdm(df_ll.values):
        tileName = ll.getTileName(lng, lat)
        recordList.append(tileName)
    df2 = pd.DataFrame(recordList)
    df = pd.concat([df, df2], axis=1)
    # 输出文件名
    if not outfile:
        outfile = fileName + '_tileName.xlsx'
    else:
        outfile = outfile + '.xlsx'
    output = os.path.join(path, outfile)
    df.to_excel(output, index=False)
    logger.info("已完成数据获取！输出文件路径为:%s" % output)
    return df
    

# 根据经纬度获取1、4、9网格的点位数量
def getDataByLngLat(filePath, lnglat, tagList, tileNum=1, dbName='Claudius', 
                    boundColl='GeoBoundary', dataColl='TileData', outfile=''):
    ll = getTileName.OCMLatLng(dbName, boundColl)
    ll.serialize()
    gbt = getFactor.getDataByTileName(tagList=tagList, MongoDB=dbName, collection=dataColl)
    logger.info("成功连接数据库！")
    result = pmi.readXlsCsv(filePath)
    df, path, fileName = result['data'], result['path'], result['file']
    df_ll = df[list(lnglat)]
    recordList = []
    if tileNum == 1:
        for lng, lat in tqdm(df_ll.values):
            tileName = ll.getTileName(lng, lat)
            recordList.append(gbt.proc(tileName))
    else:  # 获取邻近多个网格数据
        for lng, lat in tqdm(df_ll.values):
            tileNameList = ll.getTileNames(lng, lat, tileNum)
            tempList = []
            for tileName in tileNameList:
                tempList.append(gbt.proc(tileName))
            df_temp = pd.DataFrame(tempList)
            df_temp = df_temp.sum()
            recordList.append(dict(df_temp))

    df2 = pd.DataFrame(recordList)
    df = pd.concat([df, df2], axis=1)
    # 输出文件名
    if not outfile:
        outpgtfile = fileName + '_ocm.xlsx'
    else:
        outpgtfile = outpgtfile + '.xlsx'
    output = os.path.join(path, outfile)
    df.to_excel(output, index=False)
    logger.info("输出文件路径为:%s" % output)
    return df


# 根据指定区域获取指定的标签数据
def getAggDataByArea(area:dict, minLevel='tileName', tagList, rmTagList=['categories.', '.size'], 
                  dbName='Claudius', collection='TileData'):
    gda = getFactor.getDataByArea(tagList=tagList, rmTagList=rmTagList, dbName, collection)
    level = ['province', 'city', 'region', 'township', 'tileName']
    if minLevel != 'tileName':
        try:
            pos = level.index(minLevel)
            for lvl in level[pos+1:]:
                
        except ValueError:
            logger.error('请输入正确的最小层级(从列表{}中选择)！'.format(level))
    
    if city:
        gda.
    if province in ['全国','all','']:
        


if __name__ == '__main__':
    filePath = '深圳网吧_转baidu坐标.xlsx'
    lnglat = ['经度', '纬度']
    getOcmDataByLngLat(filePath, lnglat)




