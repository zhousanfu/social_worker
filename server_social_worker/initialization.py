#!python3.8
# coding=utf-8
'''
 Author: Sanfor Chow
 Date: 2022-03-09 17:28:52
 LastEditors: Sanfor Chow
 LastEditTime: 2022-03-10 17:52:56
 FilePath: /social_worker/server/initialization.py
 导入数据
'''



from config import SQL_config, DATABASE
import pymysql

connection = pymysql.connect(**SQL_config)
cursor = connection.cursor()


def clean_qq():
    f = open('data/6.9更新总库.txt', 'r', encoding='utf8')
    data = f.readlines()[:10]
    f.close()
    
    for i in range(len(data)):
        data[i] = tuple(data[i].strip().split('----'))
    print(data)

    cursor.executemany("INSERT INTO `people_contact_info` (`qq`, `tele`) VALUES ('%s', '%s')", tuple(data))
    connection.commit()



if __name__ == "__main__":
    clean_qq()
    # 关闭连接
    cursor.close()
    connection.close()
