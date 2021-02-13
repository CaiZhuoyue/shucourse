# 路由信息
from shucourse.models import Student,Teacher,Course,Select,Admin
from shucourse import app,db,bcrypt,login_manager
from shucourse.forms import LoginForm,XuankeForm,DeleteForm
from flask import render_template,url_for,flash,redirect,request
from flask_login import login_user,current_user,logout_user,login_required
@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/home')
@login_required
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')


#学生登陆
@app.route('/student/login',methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        flash('您已登陆！')
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate():
        user = Student.query.filter_by(id=form.user_id.data).first()
        if user and user.student_password==form.password.data:
            login_user(user,remember=form.remember.data)
            next_page=request.args.get('next')
            if(next_page):
                return redirect(next_page) 
            else:
                return redirect(url_for('home'))
        else:
            flash('登陆失败！','error')
    return render_template('login.html',form=form)

#教师登陆
@app.route('/teacher/login',methods=['GET','POST'])
def teacher_login():
    if current_user.is_authenticated:
        flash('您已登陆！')
        return redirect(url_for('teacher_home'))
    form = LoginForm()
    if form.validate():
        user = Teacher.query.filter_by(id=form.user_id.data).first()
        if user and user.teacher_password==form.password.data:
            login_user(user,remember=form.remember.data)
            next_page=request.args.get('next')
            if(next_page):
                return redirect(next_page) 
            else:
                return redirect(url_for('teacher_home'))
        else:
            flash('登陆失败！','error')
    return render_template('login2.html',form=form)

#管理员登陆
@app.route('/admin/login',methods=['GET','POST'])
def admin_login():
    if current_user.is_authenticated:
        return redirect(url_for('admin_home'))
    form = LoginForm()
    if form.validate():
        user = Admin.query.filter_by(id=form.user_id.data).first()
        if user and user.admin_password==form.password.data:
            login_user(user,remember=form.remember.data)
            next_page=request.args.get('next')
            if(next_page):
                return redirect(next_page) 
            else:
                return redirect(url_for('admin_home'))
        else:
            flash('登陆失败！','error')
    return render_template('login3.html',form=form)
    
#退出登录
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('welcome'))
    # 这里redirect到的是一个函数

#选课页面
@app.route('/student/select',methods=['GET','POST'])
@login_required
def select_course():
    courses=Select.query.filter_by(student_id=current_user.id)
    form=XuankeForm()
    # if Select.query.filter_by(student_id=current_user.id).first():
    #     courses=Select.query.filter_by(student_id=current_user.id).first()
    #     render_template('xuanke.html',courses=courses,form=form)
    if form.validate():
        # 有这门课
        select_course=Course.query.filter_by(course_id=form.course_id.data).first()
        if select_course:
            select = Select(student_id=current_user.id,course_id=form.course_id.data,teacher_id=form.teacher_id.data,course_name=select_course.course_name)
            db.session.add(select)
            db.session.commit()
        flash(u'选课成功','success')
        return redirect(url_for('home'))
    return render_template('select.html',form=form,courses=courses)

@app.route('/student/delete',methods=['GET','POST'])
@login_required
def delete_course():
    # return 'delete'
    courses=Select.query.filter_by(student_id=current_user.id)
    form=DeleteForm()
    if form.validate():
        # 有这门课
        if Course.query.filter_by(course_id=form.course_id.data):
            # select = Select(student_id=current_user.id,course_id=form.course_id.data,teacher_id=form.teacher_id.data)
            select=Select.query.filter_by(student_id=current_user.id,course_id=form.course_id.data,teacher_id=form.teacher_id.data).first()
            db.session.delete(select)
            db.session.commit()
        flash(u'退课成功','success')
        courses=Select.query.filter_by(student_id=current_user.id)
        return redirect(url_for('home'))
    return render_template('delete.html',form=form,courses=courses)


@app.route('/teacher/course')
@login_required
def teacher_course():
    # courses=Select.query.filter_by(teacher_id=current_user.id).distinct()
    courses=Select.query.with_entities(Select.course_id,Select.course_name).filter_by(teacher_id=current_user.id).distinct()

    # form=XuankeForm()
    # if form.validate():
    #     select_course=Course.query.filter_by(course_id=form.course_id.data).first()
    #     if select_course:
    #         select = Select(student_id=current_user.id,course_id=form.course_id.data,teacher_id=form.teacher_id.data,course_name=select_course.course_name)
    #         db.session.add(select)
    #         db.session.commit()
    #     flash(u'选课成功','success')
    #     return redirect(url_for('home'))
    return render_template('teacher_course.html',courses=courses)


@app.route('/teacher/grade')
@login_required
def teacher_grade():
    students=Select.query.filter_by(teacher_id=current_user.id)
    # course_id=course_id
    return render_template('teacher_grade.html',students=students)

@app.route('/teacher/home')
@login_required
def teacher_home():
    return render_template('home2.html')

@app.route('/admin/home')
@login_required
def admin_home():
    return render_template('home3.html')

@app.route('/student/grade')
@login_required
def student_grade():
    return "你想查成绩吗？"


@app.route('/admin/student')
def add_student():
    return 'add student'

@app.route('/admin/teacher')
def add_teacher():
    return 'add teacher'

@app.route('/admin/course')
def add_course():
    return 'add course'

