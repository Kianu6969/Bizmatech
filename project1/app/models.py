from . import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
	__tablename__ = 'user'

	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(100), unique=True)
	password = db.Column(db.String(50))
	items = db.relationship('Item', backref='user')

	def __repr__(self):
		return f'Name: {self.username}, Password: {self.password}'

class Item(db.Model, UserMixin):
	__tablename__ = 'item'

	id = db.Column(db.Integer, primary_key=True)
	bar_code = db.Column(db.Integer)
	product = db.Column(db.String(100))
	cost = db.Column(db.Float())
	selling = db.Column(db.Integer)
	action = db.Column(db.String(100))
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))