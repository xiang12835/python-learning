# coding=utf-8

import MySQLdb


DB_HOST = "***.sh.cdb.myqcloud.com"
DB_PORT = 3612
DB_USER = "use_name"
DB_PASSWD = "123456"
DB = "db_name"


def do_sql(sql, values):
    # 打开数据库连接
    db = MySQLdb.connect(
        host=DB_HOST,
        user=DB_USER,
        passwd=DB_PASSWD,
        port=DB_PORT,
        db=DB,
        charset="utf8",
    )

    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    try:
        # 执行sql语句
        cursor.executemany(sql, values)
        # 提交到数据库执行
        db.commit()
    except Exception as e:
        print e
        # Rollback in case there is any error
        db.rollback()

    # 关闭数据库连接
    db.close()


if __name__ == "__main__":

    sql = 'INSERT INTO `opponent_data`(`productName`,`productType`,`useNum`,`createTime`) VALUES (%s, %s, %s, %s)'
    values = [(1,2,3,4), (5,6,7,8)]
    do_sql(sql, values)