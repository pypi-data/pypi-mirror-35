# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 21:29:16 2018

@author: jasonai
"""

import os
import re
import numpy as np
from pmipy import log
from pmipy import pmi
import pandas as pd
from pmipy.support import prov_mapp
from pmipy import getTargetCoordinate as gtc
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']

logger = log.createLogger(__name__)


class ParseGDPOI(object):
    def __init__(self, province='江苏省', cate='购物服务;超级市场', dbName='Gaode', collection='GaoDePOI_Baidu', LAN=True):
        client = pmi.connOcm16(LAN)
        self.coll = client[dbName][collection]
        self.province = province
        self.cate = cate
        self.storeFile = '{}-[{}]类别的原始数据.xlsx'.format(province, cate)
        if os.path.exists(self.storeFile):
            logger.info('“{}”文件已存在，使用本地原始数据！'.format(self.storeFile))
            self.df = pd.read_excel(self.storeFile)
        else:
            self.df = self.getCateData()

    def getPurityPoint(self, name='', thres=500, elastic=1):
        if name:
            logger.info('准备清洗{}点位数据...'.format(name))
            df2 = self.df[self.df['name'].str[:len(name)]==name]
        else:
            logger.info('准备清洗[{}]类别的各点位数据...'.format(self.cate))
            pass

        # 分析重复的原因
        aloneList,neiList = self.positionAnalyze(df2, thres=thres)
        # 点位去重
        repeatList = self.retainIndexTag(df2, name, neiList)
        df2['addInfo'] = 'repeat'
        df2.loc[df2.index.isin(aloneList), 'addInfo'] = 'unique'
        df2 = self.rmLackBracket(df2)
        df2 = self.rmAbnAddr(df2)
        df2.loc[df2.index.isin(repeatList), 'addInfo'] = 'retainRepeat'
        #df2['addInfo'].fillna('abandon', inplace=True)
        df2.to_excel('{}-[{}]-{}点位信息.xlsx'.format(self.province, self.cate, name))
        df2[df2['addInfo'].isin(['unique','retainRepeat'])].to_excel('{}-[{}]-{}点位信息_清洗后.xlsx'.format(self.province, self.cate, name))
        logger.info('完成{}点位数据的清洗！'.format(name))
        return df2
    
    def rmLackBracket(self, df): # 去除不包含括号的点位
        df.loc[df['name'].str.find('(')==-1, 'addInfo'] = 'Non()'
        return df
    
    def rmAbnAddr(self, df): # 去除非正规地址
        pattern = r'.*(附近|对面|隔壁|东边|西边|南边|北边)'
        df.loc[df['gaddress'].apply(lambda x: True if re.match(pattern,x) else False), 'addInfo'] = 'abnAddr'  # 目前不考虑去除无电话号码的情况
        return df

    # 从MongoDB的Gaode数据库获取
    def getCateData(self):
        if self.province in ['', '全国']:
            self.province = '全国'
            logger.info('准备获取{}的[{}]类别数据...'.format(self.province, self.cate))
            cursor = self.coll.find({'gtype':{'$regex':'^{}'.format(self.cate)}},{"_id":0})
        else:
            if self.province in prov_mapp.prov_dist.keys():
                logger.info('准备获取{}的[{}]类别数据...'.format(self.province, self.cate))
            elif self.province in prov_mapp.prov_dist2.keys():
                self.province = prov_mapp.prov_dist2[self.province]
            else:
                logger.warning('请填写正确的省份名称！')
                raise SystemExit
            cursor = self.coll.find({'lv1Name':self.province,'gtype':{'$regex':'^{}'.format(self.cate)}},{"_id":0})
        df = pd.DataFrame(list(cursor))
        df.to_excel(self.storeFile, index=False)
        logger.info('{}[{}]类别的数据量为：{}'.format(self.province, self.cate, len(df)))
        return df
    
    # 按省进行比较店铺与店铺之间的坐标距离
    def positionAnalyze(self, df, thres):
        def calDistance(df):
            _list1 = []
            indexList = list(df.index)
            for i, index1 in enumerate(indexList):
                _list2 = []
                _list2.append(index1)
                lng1, lat1 = df.loc[index1]["gcjx"], df.loc[index1]["gcjy"]
                for j, index2 in enumerate(indexList[i+1:]):
                    lng2, lat2 = df.loc[index2]["gcjx"], df.loc[index2]["gcjy"]
                    if gtc.haversine(lng1, lat1, lng2, lat2) <= thres:
                        _list2.append(index2)
                        indexList.remove(index2)
                _list1.append(_list2)    
            return _list1
        
        # 暂时使用province+city进行分组，怕某些大型超市出现跨区的行为
        df2 = df.groupby(['lv1Name', 'lv2Name']).apply(calDistance)
        aloneList, neiList = [], []
        for i in df2:
            for j in i:
                if len(j)==1:
                    aloneList.extend(j)
                else:
                    neiList.append(j)
        return aloneList, neiList

    def retainIndexTag(self, df, name, neiList):
        """
        1）	筛选品牌名放"name"字段开头部位的点位
        2）	筛选品牌名后接括号注释的点位
        3）	筛选括号内含“店”的点位
        4）	筛选括号内开头前两个字在该点位的地级市或行政区划名称中出现的点位
        5）	去除中文括号内含“西门”、“东门”、“南门”、“北门”等店铺出入口标记的点位
        6）	根据项目中发现的其他特征进行针对性筛选
        代码撰写会大致根据以上6个方向进行逐步筛选，直至只筛选到一个点位为止。
        """
        def process(indexList, group, pattern):
        # 在起始位置匹配
            mIter = map(lambda x: re.match(pattern, x), group) # 这里目前考虑匹配英文括号
            countList = [1 if i else 0 for i in mIter]
            if sum(countList) == 1:
                return indexList[countList.index(1)]
            elif sum(countList) > 1:
                return countList
            else:
                return None
        
        if neiList:
            city, region = df.iloc[0]['lv2Name'], df.iloc[0]['lv3Name']
            pattern1 = r"{}.*".format(name)
            pattern2 = r"{}[（(].*".format(name)
            pattern3 = r"{}[（(].*店[)）]".format(name, city[0], region[0])
            pattern4 = r"{}[（(][{}{}].*.*店[)）]".format(name, city[0], region[0])
            pattern5 = r"{}[（(].*[^门][)）]".format(name, city[0], region[0])
            pattList = [pattern1, pattern2, pattern3, pattern4, pattern5]
            resList = []
            for i in neiList:
                group = list(df.loc[i]['name'])
                for pattern in pattList:
                    res = process(i, group, pattern)
                    if isinstance(res, np.int64): # 注意，不要用int
                        resList.append(res)
                        break
                    elif isinstance(res, list):
                        res2 = res
                if isinstance(res, list):
                    resList.append(i[res2.index(1)])
            return resList
        else:
            logger.info('未能寻找到重复性位点!')
            return []


# 分析邻近距离的阈值对重复性分析的影响
def disIterAnalyze():
    thr = list(range(0,1001,100))
    res=[]
    for t in thr:
        aloneList, neiList = positionAnalyze(df2, thres=thr, name=name)
        res.append(len(aloneList+neiList))
    thrDes = '邻近距离的阈值对重复性分析的影响'
    logger.info(thrDes)
    logger.info('使用如下阈值:{}'.format(thr))
    logger.info('对应的去重后点位数:{}'.format(res))
def plot(thr, res):
    plt.plot(thr, res)
    plt.title(thrDes)
    plt.xticks(thr)
    plt.savefig(thrDes,dpi=120)
    plt.close()

if __name__ == '__main__':
    pgp = ParseGDPOI()
    df=pgp.getPurityPoint('欧尚超市')
