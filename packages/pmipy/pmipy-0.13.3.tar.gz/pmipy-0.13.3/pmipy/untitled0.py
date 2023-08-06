# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 10:36:33 2018

@author: Administrator
"""

class Item():
    def __init__(self,name):
        self._name=name
    # def __str__(self):
    #     return "Item's name is :"+self._name

    def __repr__(self):
        return "Item's name is :" + self._name
    
    def ts(self,):
        print(self._name)
    

a=Item('zjx')
a.ts()


cm = ConnMysql('beverage_market_rmsodas')

with cm.conn.cursor() as cursor:
    # Read a single record
    cursor.execute(sql)
    # connection is not autocommit by default. So you must commit to save your changes.
    cm.conn.commit()
    conn.close()


sql ="DROP TABLE IF EXISTS `total_market`;\
CREATE TABLE `total_market` (\
`id` int(11) NOT NULL AUTO_INCREMENT,\
`province` varchar(50) DEFAULT NULL COMMENT '省',\
`city` varchar(100) DEFAULT NULL COMMENT '市，多个城市逗号隔开',\
`region` varchar(100) DEFAULT NULL COMMENT '区，多个区逗号隔开',\
`township` varchar(100) DEFAULT NULL COMMENT '乡镇',\
`tileName` varchar(30) DEFAULT NULL COMMENT '网格编号',\
`lng` double DEFAULT NULL COMMENT '经度',\
`lat` double DEFAULT NULL COMMENT '纬度',\
`channel` varchar(30) DEFAULT NULL COMMENT '渠道',\
`salesType` varchar(30) DEFAULT NULL COMMENT '销售类型，销量或销额',\
`category` varchar(50) DEFAULT NULL COMMENT '商品品类',\
`quantity` double DEFAULT NULL COMMENT '销售数值',\
`unit` varchar(30) DEFAULT NULL COMMENT '单位',\
`created` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,\
`updated` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00' ON UPDATE CURRENT_TIMESTAMP,\
PRIMARY KEY (`tileName`,`channel`,`salesType`,`category`,`unit`),\
KEY `province` (`province`),\
KEY `city` (`city`),\
KEY `region` (`region`),\
KEY `township` (`township`),\
) ENGINE=MyISAM DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 COMMENT='商圈分级总市场量信息';"
