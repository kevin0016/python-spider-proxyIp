# coding:utf-8
import pymysql.cursors
import json
import po.shArea

# mysql init
def get_cursor():
    connection = pymysql.connect(host='192.168.12.82',
                                 user='app_spread',
                                 password='RDlJ371E',
                                 db='app_spread',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    return connection.cursor()


def execute():
    cursor = get_cursor()
    cursor.execute("select id, request_body from record where cluster = 'op' limit 1")
    result = cursor.fetchall()
    for row in result:
        request_body = row["request_body"]
        print request_body


def getShArea(startPage, limit):
    cursor = get_cursor()
    cursor.execute("SELECT * FROM sh_area a LIMIT " + startPage.__str__() + "," + limit.__str__())
    result = cursor.fetchall()
    return result


def getCountShArea():
    cursor = get_cursor()
    cursor.execute("SELECT count(*) shAreaNum  FROM sh_area a")
    result = cursor.fetchall()
    print(result.__str__())
    for row in result:
        request_body = row["shAreaNum"]
        print request_body
        return request_body


if __name__ == "__main__":
    area = getShArea(0, 20)
    print(area)
