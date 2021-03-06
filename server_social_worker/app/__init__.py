#!python3.8
# coding=utf-8
'''
 Author: Sanfor Chow
 Date: 2022-03-09 17:28:52
 LastEditors: Sanfor Chow
 LastEditTime: 2022-03-09 17:37:03
 FilePath: /social_worker/server/app/__init__.py
'''
from flask import Flask
from config import config_map


def create_app(name):
    """
    创建app实例
    @param name:配置环境的名称，可选 dev， pro
    @return: app实例
    """
    app = Flask(__name__, static_folder='../static')


    # 配置
    app.config.from_object(config_map[name])

    # 接口
    from app.api.search import search
    from app.api.visualization import visualization
    app.register_blueprint(search, url_prefix='/s')
    app.register_blueprint(visualization,url_prefix='/v')

    return app
