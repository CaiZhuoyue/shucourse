# 路由信息
from shucourse.models import Student,Teacher
from shucourse import app,db,bcrypt,login_manager
from shucourse.forms import LoginForm
from flask import render_template,url_for,flash,redirect
from flask_login import login_user
@app.route('/')
def hello():
    return 'hello!'

@app.route('/about')
def about():
    return 'about'

@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate():
    # if form.validate():
        user = Student.query.filter_by(student_id=form.user_id.data).first()
        if user and user.student_password==form.password.data:
            login_user(user,remember=form.remember.data)
            return redirect(url_for('home'))
        else:
            flash('登陆失败！')
    return render_template('login.html',form=form)
    # return redirect(url_for('about'))
    

@app.route('/logout')
def logout():
    # logout_user()
    return redirect(url_for('home'))



