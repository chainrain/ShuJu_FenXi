import pandas as pd

# 读取csv的文件
file = pd.read_csv("/home/python/Desktop/itcast.csv")
# print(file)

from pymongo import MongoClient
"""需要启动mongo服务service mongod start"""
# 创建mongo连接
client = MongoClient()
collection = client['local']['startup_log']
data = list(collection.find())
# print(data)

t1 = data[0]
# print(t1)
t1 = pd.Series(t1)
print(t1)
t2 = pd.Series(data)
print(t2)