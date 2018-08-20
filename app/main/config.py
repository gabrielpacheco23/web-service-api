import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
	SECRET_KEY = os.getenv('SECRET_KEY', 'my_precious_secret_key')
	DEBUG = False
	SQLALCHEMY_POOL_RECYCLE = 50
	SQLALCHEMY_POOL_SIZE = 100
	SQLALCHEMY_DISCONNECTION_HANDLING = True

class DevelopmentConfig(Config):
	DEBUG = True
	#SQLALCHEMY_DATABASE_URI = 'mysql://apitranslsys:Mud@r123@apitranslsys.mysql.pythonanywhere-services.com/apitranslsys$default'
	SQLALCHEMY_DATABASE_URI = 'mysql://root:1234@localhost:3306/ws_main'
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	SQLALCHEMY_POOL_RECYCLE = 50

class TestingConfig(Config):
	DEBUG = True
	TESTING = True
	#SQLALCHEMY_DATABASE_URI = 'mysql://apitranslsys:Mud@r123@apitranslsys.mysql.pythonanywhere-services.com/apitranslsys$default'
	SQLALCHEMY_DATABASE_URI = 'mysql://root:1234@localhost:3306/ws_test'
	PRESERVE_CONTEXT_ON_EXCEPTION = False
	SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(Config):
	DEBUG = False

config_by_name = dict(
	dev=DevelopmentConfig,
	test=TestingConfig,
	prod=ProductionConfig
)

key = Config.SECRET_KEY
