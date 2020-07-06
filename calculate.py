#!/usr/bin/env python

# -*- coding:utf-8 -*-

#@Time      :2020/7/6 11:54

#@Author    :Laiyigui

#@File      :test.py

# 读取数据
data1 = []
data2 = []
for line in open("test_data1.txt"):
    data1.append(int(line))
for line in open("test_data2.txt"):
    data2.append(int(line))

# 交集
inter = sorted(list(set(data1).intersection(set(data2))))
f3 = open("inter.txt","w")
for i in inter:
   f3.write(str(i)+'\n')
f3.close()

# 并集
union = sorted(list(set(data1).union(set(data2))))
f4 = open("union.txt","w")
for i in union:
   f4.write(str(i)+'\n')
f4.close()

# 差集
diff1 = sorted(list(set(data1).difference(set(data2))))
f5 = open("diff1.txt","w")
for i in diff1:
   f5.write(str(i)+'\n')
f5.close()

diff2 = sorted(list(set(data2).difference(set(data1))))
f6 = open("diff2.txt","w")
for i in diff2:
   f6.write(str(i)+'\n')
f6.close()