# -*- coding: utf-8 -*-

import re
import urllib
import json
import MySQLdb
import time
import sys


reload(sys)
sys.setdefaultencoding('utf8')

# 测试线
DB_HOST = "***.sh.cdb.myqcloud.com"
DB_PORT = 3612
DB_USER = "user_name"
DB_PASSWD = "password"
DB = "db_name"


# 正式线
# DB_HOST = "***.sh.cdb.myqcloud.com"
# DB_PORT = 7863
# DB_USER = "user_name"
# DB_PASSWD = "password"
# DB = "db_name"

# 正式线配置 crontab
# vi /var/spool/cron/root
# 30 12 * * * python sync_data_from_fenbi.py
# service crond restart

NAME_TYPE_DICT = {
    "1": '公考',
    "2": '申论',
    "3": '事业单位',
    "4": '司考',
    "5": '会计',
    "6": '考研',
    "7": '教师',
}


class SyncData(object):

    def get_source(self, url):
        """获取接口数据"""
        try:
            s = urllib.urlopen(url).read()
        except Exception as e:
            print e
            s = '{}'
        return json.loads(s)

    def change_page(self, url, total_page):
        """产生不同页数的链接"""
        current_page = int(re.search('start=(\d+)', url, re.S).group(1))
        page_group = []
        for i in range(current_page, total_page + 1):
            link = re.sub('start=\d+', 'start=%s' % i, url, re.S)
            page_group.append(link)
        return page_group

    def get_info(self, dic):
        """取出需要的信息"""
        info = {}
        lecture_dict = dic.get("lectureSummary", {})
        if not lecture_dict:
            lecture_dict = dic.get("lectureSetSummary", {})
        studentCount = lecture_dict.get("studentCount", 0)
        title = lecture_dict.get("title", "")
        productType = "1"
        # for key, val in NAME_TYPE_DICT.iteritems():
        #     if val in title:
        #         productType = key
        #         break
        info['productType'] = productType
        info['studentCount'] = studentCount
        info['title'] = title

        return info

    def do_sql(self, sql, values):

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
    # url = 'http://fenbi.com/web/users/course/gwy?start=1'
    # fenbi = SyncData()
    # ret = fenbi.get_source(url)
    # print json.dumps(ret, ensure_ascii=False, sort_keys=True, indent=4)
    #
    # try:
    #     for dic in ret.get("courseInfo", []):
    #         title = dic.get("lectureSummary", {}).get("title", "")
    #         studentCount = dic.get("lectureSummary", {}).get("studentCount", 0)
    #         print title, studentCount
    # except Exception as e:
    #     print e

    url = 'http://fenbi.com/web/users/course/gwy?start=1'
    fenbi = SyncData()
    totalPages = fenbi.get_source(url).get("paramList", {}).get("totalPages", 1)
    # print totalPages
    all_links = fenbi.change_page(url, totalPages)
    # print all_links
    target_list = []
    for link in all_links:
        # print u'page -> ' + link
        dic = fenbi.get_source(link)
        for each in dic.get("courseInfo", []):
            target_list.append(fenbi.get_info(each))
    if target_list:

        sql = 'INSERT INTO `opponent_data`(`productName`,`productType`,`useNum`,`createTime`) VALUES (%s, %s, %s, %s)'
        values = []
        for dic in target_list:
            this_tup = (dic['title'], dic['productType'], dic['studentCount'], int(time.time()))
            values.append(this_tup)

        print values

        tmp_list = [values[x:x+10] for x in range(0, len(values), 10)]
        for each_list in tmp_list:
            fenbi.do_sql(sql, values)

        # fenbi.save_data(target_list)
