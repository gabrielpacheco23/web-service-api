from flask import request, Flask
from flask_restplus import Resource

from ..util.dto import UserDto
from ..service.user_service import save_new_user, get_all_users, get_a_user
from ..util.ping_db import PingConnectionHandler
from app.main import db, app

#from flask_sql_alchemy_session import flask_scoped_session
#from sqlalchemy.orm import sessionmaker
#from manage import app
#import manage
#app = create_app('dev')

api = UserDto.api
_user = UserDto.user

#session_factory = sessionmaker(bind=db.engine)
#session = flask_scoped_session(session_factory, app)


@api.route('/')
class UserList(Resource):
	@api.doc('list_of_registered_users')
	@api.marshal_list_with(_user, envelope='data')
	def get(self):
		"""List all registered users"""
		if app.config.get('SQLALCHEMY_DISCONNECTION_HANDLING', True):
			PingConnectionHandler(db.get_engine(app)).register()
		return get_all_users()

	@api.response(201, 'User successfully created.')
	@api.doc('create a new user')
	@api.expect(_user, validate=True)
	def post(self):
		"""Creates a new User """
		if app.config.get('SQLALCHEMY_DISCONNECTION_HANDLING', True):
			PingConnectionHandler(db.get_engine(app)).register()
		data = request.json
		return save_new_user(data=data)


@api.route('/<public_id>')
@api.param('public_id', 'The User identifier')
@api.response(404, 'User not found.')
class User(Resource):
	@api.doc('get a user')
	@api.marshal_with(_user)
	def get(self, public_id):
		"""get a user given its identifier"""		
		if app.config.get('SQLALCHEMY_DISCONNECTION_HANDLING', True):
			PingConnectionHandler(db.get_engine(app)).register()

		user = get_a_user(public_id)
		if not user:
			api.abort(404)
		else:
			return user


