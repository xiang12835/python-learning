# coding=utf-8

# pip install mysqlclient

import MySQLdb


def test_pymysql():
    conn = MySQLdb.connect(
        host='localhost',
        port=3306,
        user='your_username',
        passwd='your_password',
        db='mysql'
    )

    cur = conn.cursor()
    cur.execute('''
            CREATE TABLE price (
                timestamp TIMESTAMP NOT NULL,
                BTCUSD FLOAT(8,2),
                PRIMARY KEY (timestamp)
            );
        ''')
    cur.execute('''
            INSERT INTO price VALUES(
                "2019-07-14 14:12:17",
                11234.56
            );
        ''')

    conn.commit()
    conn.close()

# ==========

# 1. 连接 MySQL


import MySQLdb

# 打开数据库连接
db = MySQLdb.connect("localhost", "testuser", "test123", "TESTDB", charset='utf8' )

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# 2. 执行 SQL 语句

# 使用 execute 方法执行 SQL 语句
cursor.execute("SELECT VERSION()")

# 使用 fetchone() 方法获取一条数据
data = cursor.fetchone()

print "Database version : %s " % data

# 关闭数据库连接
db.close()

