#!python3.8
# coding=utf-8
'''
 Author: Sanfor Chow
 Date: 2022-03-09 17:28:52
 LastEditors: Sanfor Chow
 LastEditTime: 2022-03-09 17:41:52
 FilePath: /social_worker/server/config.py
'''

SQL_config = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'passwd': '123456',
    'charset': 'utf8mb4',
    'local_infile': 1
    }
DATABASE = 'social_worker'


class DevelopmentConfig():
    """开发者环境配置"""
    DEBUG = True


class ProductionConfig():
    """实际生产环境配置"""
    threaded = True
    pass


config_map = {
    'dev': DevelopmentConfig,
    'pro': ProductionConfig
}
