# -*- coding:utf-8 -*-
__author__ = u'东方鹗'

import os
import hashlib

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
	SECRET_KEY = os.environ.get('SECRET_KEY') or hashlib.new(name='md5', string='ousi keji hawk@#').hexdigest()
	UPLOAD_FOLDER = os.path.join(basedir, 'app/lib/static/uploads')
	MAX_CONTENT_LENGTH = 32 * 1024 * 1024

	@staticmethod
	def init_app(app):
		pass


class DevelopmentConfig(Config):
	DEBUG = True


class TestingConfig(Config):
	TESTING = True



config = {
	'development': DevelopmentConfig,
	'testing': TestingConfig,
	'default': DevelopmentConfig
}
