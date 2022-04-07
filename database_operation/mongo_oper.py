# coding=utf-8

# 1. 连接 MongoDB
from pymongo import MongoClient


conn = MongoClient("mongodb://%s:%s@ipaddress:49974/mydb" % ('username', 'password'))
db = conn.mydb
mongo_collection = db.mydata


# 2. 批量插入数据

res = requests.get(url, params=query).json()
commentList = res['data']['commentList']
mongo_collection.insert_many(commentList)