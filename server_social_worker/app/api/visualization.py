#!python3.8
# coding=utf-8
'''
 Author: Sanfor Chow
 Date: 2022-03-09 17:28:52
 LastEditors: Sanfor Chow
 LastEditTime: 2022-03-09 17:34:48
 FilePath: /social_worker/server/app/api/visualization.py
'''


from flask import Blueprint, request, jsonify
from utils import result2bs64
from utils2 import get_json




visualization = Blueprint('visualization', __name__)


@visualization.route('/visualization/', methods=['POST'])
def visualizationdata():
    """
        查询接口
        @param content:数据的查询
        @return code(200=正常返回，400=错误),data
    """
    try:
        param = request.get_json()
        key = param.get('key')
        value = param.get('value')
    except:
        return jsonify(code=400, msg='参数错误')
    if key not in ["QQNum", "QunNum"]:
        return jsonify(code=400, msg='参数错误')
    result = result2bs64(key, value, 1)
    if result["code"] == 400:
        return jsonify(code=400, msg='参数错误')
    elif result["code"] == 200:
        return jsonify(code=200, msg='successful!', image=result["image"], id2data=result["id2data"])
    elif result["code"] == 300:
        return jsonify(code=300, msg="未查询到相关数据")
    else:
        return jsonify(code=400, msg='未知错误')

@visualization.route('/antv/', methods=['POST'])
def antv():
    """
        查询接口
        @param content:数据的查询
        @return code(200=正常返回，400=错误),data
    """
    try:
        param = request.get_json()
        key = param.get('key')
        value = param.get('value')
    except:
        return jsonify(code=400, msg='参数错误')
    if key not in ["QQNum", "QunNum"]:
        return jsonify(code=400, msg='参数错误')
    result = get_json(key, value, 1)
    if result["code"] == 400:
        return jsonify(code=400, msg='参数错误')
    elif result["code"] == 200:
        return jsonify(code=200, msg='successful!', result_data=result["result_data"])
    elif result["code"] == 300:
        return jsonify(code=300, msg="未查询到相关数据")
    else:
        return jsonify(code=400, msg='未知错误')
