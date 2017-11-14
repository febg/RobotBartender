#instance/config.py

import os

class Config(object):
	"""Parent configuration class."""
	DEBUG = False
	CSRF_ENABLED = True
	SECRET = os.getenv('SECRET')
	SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')

class DevelopmentConfig(Config):
	"""Configuration for Development environment"""
	DEBUG = True

class TestingConfig(Config):
	"""Configurations for testing, using test database"""
	TESTING = True
	SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:admin@localhost:5432/test_db'
	DEBUG = True

class StagingConfig(Config):
	"""Configurations for staging"""	
	DEBUG = True

class ProductionConfig(Config):
	"""Configuration for Production"""
	DEBUG = True
	TESTING = True

app_config = {
	'development': DevelopmentConfig,
	'testing': TestingConfig,
	'staging': StagingConfig,
	'production': ProductionConfig,
}
