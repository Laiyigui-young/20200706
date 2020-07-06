#!/usr/bin/env python

# -*- coding:utf-8 -*-

#@Time      :2020/7/6 14:28

#@Author    :Laiyigui

#@File      :reptile.py

import requests
import json
import pymysql

# 获取榜单APP的ID值
def getAppId():
    header = {
    'User-Agent': 'AppStore/3.0 iOS/12.1.2 model/iPhone8,1 hwp/s8000 build/16C104 (6; dt:120) AMS/1',
    'X-Apple-Client-Application': 'com.apple.AppStore',
    'X-Apple-Store-Front': '143465-19,29',
    'Host': 'itunes.apple.com',
    'Accept-Encoding': 'br, gzip, deflate'
    }
    url = 'https://itunes.apple.com/WebObjects/MZStore.woa/wa/viewTop?genreId=6014&pageOnly=true'
    response = requests.get(url, headers=header)
    data = json.loads(response.text)
    idList = data['pageData']['selectedChart']['adamIds']
    return idList

# 构建mysql连接
conn = pymysql.connect(host='localhost',user='root',password='',db='mydb',charset='utf8',port=3306)
# 游标对象
cursor = conn.cursor()

# 请求头
header = {
    'User-Agent': 'AppStore/3.0 iOS/12.1.2 model/iPhone8,1 hwp/s8000 build/16C104 (6; dt:120) AMS/1',
    'X-Apple-Client-Application': 'com.apple.AppStore',
    'X-Apple-Store-Front': '143465-19,29 t:apps3',
    'Host': 'apps.apple.com',
    'Accept-Encoding': 'br, gzip, deflate'}

idList = getAppId() #获取榜单上的APPID值

for i in idList:
    # 读取数据
    url = 'https://apps.apple.com/cn/app/id{}'.format(i)
    response = requests.get(url, headers=header)
    data = json.loads(response.text)
    appId = i
    appName = data['storePlatformData']['product-dv']['results'][i]['name']
    artistId = data['storePlatformData']['product-dv']['results'][i]['artistId']
    artistName = data['storePlatformData']['product-dv']['results'][i]['artistName']
    ratingCount = data['storePlatformData']['product-dv']['results'][i]['userRating']['ratingCount']

    # 插入数据至mysql当中
    sql = 'insert into appData(appId,appName,artistId,artistName,ratingCount) values ("%s","%s","%s","%s","%d")' % (appId,appName,artistId,artistName,ratingCount)
    cursor.execute(sql)

# 关闭mysql
conn.commit()#这一句很关键，若缺少的话，将无法生成mysql数据
cursor.close()
conn.close()