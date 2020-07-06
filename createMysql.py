#!/usr/bin/env python

# -*- coding:utf-8 -*-

#@Time      :2020/7/6 14:03

#@Author    :Laiyigui

#@File      :createMysql.py

import pymysql
conn=pymysql.connect(host='localhost',user='root',password='',db='mydb',charset='utf8',port=3306)

cursor=conn.cursor()

#建立存放电影数据的表doubanfilm6,名字自取
sql = "create table appData(num int primary key auto_increment,appId varchar(20),appName varchar(50),artistId varchar(20),artistName varchar(50),ratingCount int)"

cursor.execute(sql)

cursor.close()
conn.close()

