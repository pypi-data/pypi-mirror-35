# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 10:01:43 2018

@author: Administrator
"""

import pandas as pd
from pmipy import log
from pmipy import pmi

logger = log.createLogger(__name__)

def parseJson_old(record):
    row = {}
    for tier1 in record.keys():
        if type(record[tier1])==dict:
            for tier2 in record[tier1].keys():
                if type(record[tier1][tier2])==dict:
                    for tier3 in record[tier1][tier2].keys():
                        if type(record[tier1][tier2][tier3])==dict: 
                            for tier4 in record[tier1][tier2][tier3].keys():
                                if type(record[tier1][tier2][tier3][tier4])==dict: 
                                    for tier5 in record[tier1][tier2][tier3][tier4].keys():
                                        row[tier1+'.'+tier2+'.'+tier3+'.'+tier4+'.'+tier5] = record[tier1][tier2][tier3][tier4][tier5]
                                else:
                                    row[tier1+'.'+tier2+'.'+tier3+'.'+tier4] = record[tier1][tier2][tier3][tier4]
                        else:
                            row[tier1+'.'+tier2+'.'+tier3] = record[tier1][tier2][tier3]
                else:
                    row[tier1+'.'+tier2] = record[tier1][tier2]
        else:
            row[tier1] = record[tier1]
    return row


# 拆解字典对象的key需要配合 fieldNamesFormat 函数使用 -> .a.b.c等
def parseJson(record: dict):
    def _process(record: dict, fieldnames={}, key=''):
        """
        提取要生成csv文件的标题字段
        :param record: dict对象
        :param fieldnames: 存字段的字典{}
        :param key:
        """
        for each in record.keys():
            if isinstance(record[each], dict):
                 _process(record[each], fieldnames,key + '.' + each)
            else:
                key2 =  key + '.' + each
                fieldnames[key2[1:]] = record[each]
        
        return fieldnames
    return _process(record)


def getDataFrame(cursor): 
    rowList = []
    for record in cursor:
        row = parseJson(record)
        rowList.append(row)
    df = pd.DataFrame(rowList)
    return df


# 去除“其他”
def removeOther(df): 
    col =  [i for i in list(df) if '其他' not in i]
    return df[col]

# 去除列名中的指定字段，比如'categories'
def removeTag(df, tagList=['categories.']):
    col = list(df)
    for tag in tagList:
        col = [i.replace(tag, '') for i in col]
    df.columns = col
    return df


class getDataByTileName(object):
    def __init__(self, tagList=['poi','dianping','population','anjuke','anjukeRent','segmentation'], 
                 MongoDB='Claudius', collection='TileData'):
        client16 = pmi.connOcm16()
        self.collection = client16[MongoDB][collection]
        self.matchDict = {'meters': 1000, 'processTime':'201711'}
        self.showDict = {'province':1, 'city': 1, 'region': 1, 'township': 1, 'tileName': 1, '_id': 0}
        for tag in tagList:
            self.showDict[tag] = 1

    def proc(self, tileName): # poi、dianping
        self.matchDict['tileName'] = tileName
        cursor = self.collection.find_one(self.matchDict, self.showDict, no_cursor_timeout=True)
        try:
            _dict = parseJson(cursor)
        except AttributeError:
            _dict = {'tileName': tileName}
          
        return _dict


class getDataByArea(object):
    def __init__(self, tagList=['poi','dianping','population','anjuke','anjukeRent','segmentation'], 
                 aliasList=[],rmTagList=['categories.', '.size'], MongoDB='Claudius', collection='TileData'):
        client16 = pmi.connOcm16()
        self.collection = client16[MongoDB][collection]
        self.matchDict = {'meters': 1000, 'processTime':'201711'}
        self.showDict = {'province':1, 'city': 1, 'region': 1, 'township': 1, 'tileName': 1, '_id': 0}
        self.rmTagList = rmTagList
        self.tagList = tagList
        self.aliasList = aliasList
        for tag in tagList:
            self.showDict[tag] = 1
        
    def proc(self, area:dict): # poi、dianping {'province':'江苏省'}
        self.matchDict.update(area)
        cursor = self.collection.find(self.matchDict, self.showDict, no_cursor_timeout=True)
        documentList = []
        for document in cursor:
            _dict = parseJson(document)
            documentList.append(_dict)
        df = pd.DataFrame(documentList)
        df = removeTag(df, self.rmTagList)
        return df
    

class getAggDataByArea(object):
    def __init__(self, tagList=['poi.categories.购物.categories.集市','poi.categories.购物.categories.超市'],
                 aliasList=[], minLevel='township',MongoDB='Claudius', collection='TileData'):
        client16 = pmi.connOcm16()
        self.collection = client16[MongoDB][collection]
        self.matchDict = {'meters': 1000, 'processTime':'201711'}
        self.minLevel = minLevel
        self.tagList = tagList
        self.aliasList = aliasList

    def agg(self, area:dict): # poi、dianping {'province':'江苏省'}
        self.matchDict.update(area)
        level = ['province', 'city', 'region', 'township', 'tileName']
        gDict = {'_id':{}}
        
        try:
            pos = level.index(self.minLevel)
            useLevel = level[:pos+1]
            for lvl in useLevel:
                gDict['_id'][lvl] = '$' + lvl
        except ValueError:
            logger.error('请输入正确的最小层级(从列表{}中选择)！'.format(level))
            raise SystemExit
        
        
        if not len(self.aliasList)==len(self.tagList):
            for tag in self.tagList:
                alias = tag.replace('.categories.', '_').replace('.size', '')
                gDict[alias] = {'$sum' : '${0}'.format(tag)}
                
        else:
            for (alias, tag) in zip(self.aliasList, self.tagList):
                gDict[alias] = {'$sum' : '${0}'.format(tag)}
        
        m = {'$match': self.matchDict}
        g = {'$group': gDict}
        
        cursor = self.collection.aggregate([m, g])
        # 解析_id
        documentList = []
        for document in cursor:
            _dict = parseJson(document)
            documentList.append(_dict)
        df = pd.DataFrame(documentList)
        # 去除_id.
        col = list(df)
        colNew = [i.replace('_id.','') for i in col]
        df.columns = colNew
        return df



if __name__ == '__main__':
    # 测试
    gada = getAggDataByArea(minLevel='township')
    df=gada.agg({'province':'江苏省'})
    
    # 测试2
    gda = getDataByArea(['poi'])
    df=gda.proc({'province':'江苏省'})

