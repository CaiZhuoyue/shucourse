#coding:utf-8
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app=Flask(__name__)
app.config['SECRET_KEY']='ahoshdoaihro378492'
# 如果用mysql就要换一下这句话
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt=Bcrypt(app)
login_manager=LoginManager(app)
login_manager.login_view='welcome'
login_manager.login_message_catogory='info'
from shucourse import routes
# 不要改这一行的位置 不然会循环import

