#!python3.8
# coding=utf-8
'''
 Author: Sanfor Chow
 Date: 2022-03-09 17:28:52
 LastEditors: Sanfor Chow
 LastEditTime: 2022-03-09 17:35:38
 FilePath: /social_worker/server/manage.py
'''


from app import create_app
from flask_script import Manager
from flask_cors import CORS

app = create_app('dev')
CORS(app)
manager = Manager(app)

"""
python manage.py runserver --host 127.0.0.1 --port 3268  运行服务器
"""

if __name__ == '__main__':
    manager.run()
