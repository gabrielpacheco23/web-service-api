import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
	SECRET_KEY = os.getenv('SECRET_KEY', 'my_precious_secret_key')
	DEBUG = False
	SQLALCHEMY_POOL_RECYCLE = 50
	SQLALCHEMY_POOL_SIZE = 100
	SQLALCHEMY_DISCONNECTION_HANDLING = True
	#SQLALCHEMY_DATABASE_URI = 'mysql://b5113854d7ce0c:2e5bd146@us-cdbr-iron-east-01.cleardb.net/heroku_f928163fc4a243b?reconnect=true'
	SQLALCHEMY_DATABASE_URI = 'postgres://fpxcyrzzsqrwwc:5d871194b0a7475568df0086456b854dc097226118f9d2f50a7d97ebd0eb71ab@ec2-54-235-244-185.compute-1.amazonaws.com:5432/dd66ra009a756n'


class DevelopmentConfig(Config):
	DEBUG = True
	#SQLALCHEMY_DATABASE_URI = 'mysql://apitranslsys:Mud@r123@apitranslsys.mysql.pythonanywhere-services.com/apitranslsys$default'
	#SQLALCHEMY_DATABASE_URI = 'mysql://root:1234@localhost:3306/ws_main'
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	SQLALCHEMY_POOL_RECYCLE = 50

class TestingConfig(Config):
	DEBUG = True
	TESTING = True
	#SQLALCHEMY_DATABASE_URI = 'mysql://apitranslsys:Mud@r123@apitranslsys.mysql.pythonanywhere-services.com/apitranslsys$default'
	#SQLALCHEMY_DATABASE_URI = 'mysql://root:1234@localhost:3306/ws_test'
	PRESERVE_CONTEXT_ON_EXCEPTION = False
	SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(Config):
	DEBUG = False
	#SQLALCHEMY_DATABASE_URI = 'mysql://root:1234@localhost:3306/ws_main'

config_by_name = dict(
	dev=DevelopmentConfig,
	test=TestingConfig,
	prod=ProductionConfig
)

#git push

key = Config.SECRET_KEY
