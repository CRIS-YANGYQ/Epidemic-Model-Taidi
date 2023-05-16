import os

import pymysql
import csv
import codecs


def get_conn():
    conn = pymysql.connect(host='localhost', port=3306, user='root', password='ff2017', db='tedi_data', charset='utf8')
    return conn


def insert(cur, sql, args):
    cur.execute(sql, args)


def read_csv_to_mysql(filename):
    current = 0
    with codecs.open(filename=filename, mode='r', encoding='utf-8') as f:
        reader = csv.reader(f)
        head = next(reader)
        conn = get_conn()
        cur = conn.cursor()
        sql = 'insert into venue_code_info values(%s,%s,%s,%s,%s)'
        for item in reader:
            args = list(item)
            current += 1
            args[0] = current
            args = tuple(args)
            insert(cur, sql=sql, args=args)
            conn.commit()
        cur.close()
        conn.close()

    print("success!")


if __name__ == '__main__':
    pre = "C:/Users/Deng_/PycharmProjects/test_for_tedi/tedi-230412/datas/venue_code_info/"
    i = 0
    for file in os.listdir(pre):
        read_csv_to_mysql(pre + file)
        i += 1
        print('current: ', i)
