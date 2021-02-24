# 路由信息
from shucourse.models import Student,Teacher,Course,Select,Admin
from shucourse import app,db,bcrypt,login_manager
from shucourse.forms import LoginForm,XuankeForm,DeleteForm,GradeForm,StudentForm,TeacherForm,CourseForm,ChangeForm
from flask import render_template,url_for,flash,redirect,request
from flask_login import login_user,current_user,logout_user,login_required
from sqlalchemy import func
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
                return redirect(url_for('select_course'))
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
        flash('您已登陆！')
        return redirect(url_for('admin_home'))
    form = LoginForm()
    if form.validate():
        user = Admin.query.get(form.user_id.data)
        if user and user.admin_password==form.password.data:
            login_user(user)
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
    # courses=Select.query.filter_by(student_id=current_user.id)
    courses=Select.query.filter_by(student_id=current_user.id).with_entities(Course,Select.student_id==current_user.id,Select.course_id==Course.course_id).add_columns(Course.course_xuefen,Course.course_maxn,Course.course_time,Course.course_open,Select.course_id,Select.course_name,Course.course_teacher)
    form=XuankeForm()
    if form.validate():
        select_course=Course.query.filter_by(course_id=form.course_id.data).first()
        already_select=Select.query.filter_by(course_id=form.course_id.data,student_id=current_user.id).first()
        if already_select:
            return render_template('select.html',form=form,courses=courses,message="重复选课")
        elif select_course:
            select = Select(student_id=current_user.id,course_id=form.course_id.data,teacher_id=form.teacher_id.data,course_name=select_course.course_name)
            db.session.add(select)
            db.session.commit()
            return render_template('select.html',form=form,courses=courses)
        else:
            return render_template('select.html',form=form,courses=courses,message="课程不存在")
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

@app.route('/student/changepass',methods=['GET','POST'])
@login_required
def student_pwd():
    form=ChangeForm()
    if form.validate():
        student=Student.query.get(current_user.id)
        student.student_password=(form.password.data)
        # db.session.add(student)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('change.html',form=form)

@app.route('/teacher/course')
@login_required
def teacher_course():
    # courses=Select.query.filter_by(teacher_id=current_user.id).distinct()
    courses=Select.query.with_entities(Select.course_id,Select.course_name).filter_by(teacher_id=current_user.id).distinct()
    return render_template('teacher_course.html',courses=courses)

@app.route('/teacher/grade',methods=['GET','POST'])
@login_required
def teacher_grade():
    form=GradeForm()
    big=Student.query.join(Select,Student.id==Select.student_id).add_columns(Select.course_id,Student.student_name,Select.student_id,Student.student_dept,Select.student_grade).distinct()
    if(form.validate()):
        select=Select.query.filter_by(student_id=form.student_id.data).first()
        select.student_grade=(form.grade.data)
        db.session.commit()
        big=Student.query.join(Select,Student.id==Select.student_id).add_columns(Select.course_id,Student.student_name,Select.student_id,Student.student_dept,Select.student_grade).distinct()
        return render_template('teacher_grade.html',students=big,form=form)
    return render_template('teacher_grade.html',students=big,form=form)

@app.route('/teacher/home')
@login_required
def teacher_home():
    return render_template('home2.html')

@app.route('/admin/home')
def admin_home():
    return render_template('home3.html')

@app.route('/student/grade')
@login_required
def student_grade():
    courses=Select.query.filter_by(student_id=current_user.id).all()
    # avg_grade=Select.query.with_entities(func.avg(Select.student_grade).label('average')).filter(Select.student_id==current_user.id,Select.student_grade!=None)
    avg_grade=Select.query.with_entities(func.avg(Select.student_grade).label('average')).filter(Select.student_id==current_user.id)
    return render_template('grade.html',courses=courses,avg_grade=avg_grade)

@app.route('/admin/student',methods=['GET','POST'])
# @login_required
def admin_student():
    students=Student.query.all()
    return render_template('admin_student.html',students=students)

@app.route('/admin/student/add',methods=['GET','POST'])
# @login_required
def add_student():
    form=StudentForm()
    if form.validate():
        student = Student(id=form.student_id.data,student_name=form.student_name.data,student_password=form.student_id.data,student_dept=form.student_dept.data)
        db.session.add(student)
        db.session.commit()
        students=Student.query.all()
        return render_template('admin_student.html',students=students)
    return render_template('add_student.html',form=form)


@app.route('/admin/student/<string:s_id>',methods=['GET','POST'])
# @login_required
def delete_student(s_id):
    form=StudentForm()
    student=Student.query.filter_by(id=s_id).first()
    # 外键约束
    select=Select.query.filter_by(student_id=s_id).first()
    while select:
        db.session.delete(select)
        db.session.commit()
        select=Select.query.filter_by(student_id=s_id).first()
    db.session.delete(student)
    db.session.commit()
    students=Student.query.all()
    return render_template('admin_student.html',students=students,form=form)

@app.route('/admin/course/delete/<string:s_id>',methods=['GET','POST'])
# @login_required
def admin_delete_course(s_id):
    form=CourseForm()
    course=Course.query.filter_by(course_id=s_id).first()
    # 外键约束
    select=Select.query.filter_by(course_id=s_id).first()
    while select:
        db.session.delete(select)
        db.session.commit()
        select=Select.query.filter_by(course_id=s_id).first()
    db.session.delete(course)
    db.session.commit()
    courses=Course.query.all()
    return render_template('admin_course.html',courses=courses,form=form)

@app.route('/admin/teacher/delete/<string:s_id>',methods=['GET','POST'])
# @login_required
def admin_delete_teacher(s_id):
    form=TeacherForm()
    teacher=Teacher.query.filter_by(id=s_id).first()
    # 外键约束
    select=Select.query.filter_by(teacher_id=s_id).first()
    while select:
        db.session.delete(select)
        db.session.commit()
        select=Select.query.filter_by(teacher_id=s_id).first()
    db.session.delete(teacher)
    db.session.commit()
    teachers=Teacher.query.all()
    return render_template('admin_teacher.html',teachers=teachers,form=form)




@app.route('/admin/teacher/add',methods=['GET','POST'])
# @login_required
def add_teacher():
    form=TeacherForm()
    if form.validate():
        teacher = Teacher(id=form.teacher_id.data,teacher_name=form.teacher_name.data,teacher_password=form.teacher_password.data,teacher_dept=form.teacher_dept.data,teacher_stat=form.teacher_stat.data)
        db.session.add(teacher)
        db.session.commit()
        teachers=Teacher.query.all()
        return render_template('admin_teacher.html',teachers=teachers)
    return render_template('add_teacher.html',form=form)

@app.route('/admin/teacher',methods=['GET','POST'])
# @login_required
def admin_teacher():
    teachers=Teacher.query.all()
    return render_template('admin_teacher.html',teachers=teachers)

@app.route('/admin/course',methods=['GET'])
# @login_required
def admin_course():
    courses=Course.query.all()
    return render_template('admin_course.html',courses=courses)

@app.route('/admin/course/add',methods=['GET','POST'])
# @login_required
def add_course():
    form=CourseForm()
    if form.validate():
        course = Course(course_id=form.course_id.data,course_name=form.course_name.data,course_teacher=form.course_teacher.data,course_xuefen=form.course_xuefen.data,course_time=form.course_time.data,course_open=form.course_open.data,course_maxn=form.course_maxn.data)
        db.session.add(course)
        db.session.commit()
        courses=Course.query.all()
        return render_template('admin_course.html',courses=courses)
    return render_template('add_course.html',form=form)

