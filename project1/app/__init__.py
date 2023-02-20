from flask import Flask, current_app
from flask_sqlalchemy import SQLAlchemy
# from .models import User
db = SQLAlchemy()


app = Flask(__name__)
app.config['SECRET_KEY'] = '12345'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pos.sqlite3'
db.init_app(app)

app.app_context().push()

from .views import views
from .auth import auth



app.register_blueprint(views, url_prefix='/')
app.register_blueprint(auth, url_prefix='/')
