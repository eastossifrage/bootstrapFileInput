# -*- coding:utf-8 -*-
__author__ = '东方鹗'

from flask import Flask
from config import config


def create_app(config_name):
    """ 使用工厂函数初始化程序实例"""
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app=app)

    # 注册蓝本 lib
    from .lib import lib as lib_blueprint
    app.register_blueprint(lib_blueprint, url_prefix='/lib')

    # 注册蓝本 basic
    from .basic import basic as basic_blueprint
    app.register_blueprint(basic_blueprint, url_prefix='/basic')

    return app
