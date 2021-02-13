from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField
from wtforms.validators import DataRequired, Length,EqualTo
from shucourse.models import Student,Teacher,Admin,Course,Select
class LoginForm(FlaskForm):
    user_id=StringField(u'学号/教师号',validators=[DataRequired(),Length(min=4,max=8)])
    password=PasswordField(u'密码',validators=[DataRequired()])
    remember=BooleanField(u'记住我')
    submit=SubmitField(u'登陆')
    
class XuankeForm(FlaskForm):
    # student_id=StringField()
    course_id=StringField(u'课程号:',validators=[DataRequired(),Length(min=8,max=8)])
    teacher_id=StringField(u'教师号:',validators=[DataRequired(),Length(min=4,max=4)])
    submit=SubmitField(u'选课')

class DeleteForm(FlaskForm):
    # student_id=StringField()
    course_id=StringField(u'课程号:',validators=[DataRequired(),Length(min=8,max=8)])
    teacher_id=StringField(u'教师号:',validators=[DataRequired(),Length(min=4,max=4)])
    submit=SubmitField(u'退课')

class StudentForm(FlaskForm):
    student_id=StringField(u'学号:',validators=[DataRequired(),Length(min=8,max=8)])
    student_name=StringField(u'姓名:',validators=[DataRequired(),Length(min=2,max=20)])
    student_dept=StringField(u'学院号:',validators=[DataRequired(),Length(min=1,max=2)])
    submit=SubmitField(u'添加学生')

class TeacherForm(FlaskForm):
    teacher_id=StringField(u'教师号:',validators=[DataRequired(),Length(min=4,max=4)])
    teacher_name=StringField(u'姓名:',validators=[DataRequired(),Length(min=2,max=20)])
    teacher_dept=StringField(u'学院号:',validators=[DataRequired(),Length(min=1,max=2)])
    submit=SubmitField(u'添加教师')


class CourseForm(FlaskForm):
    course_id=StringField(u'课程号:',validators=[DataRequired(),Length(min=8,max=8)])
    course_name=StringField(u'课程名:',validators=[DataRequired(),Length(min=2,max=20)])
    course_teacher=StringField(u'教师号:',validators=[DataRequired(),Length(min=4,max=4)])
    submit=SubmitField(u'添加课程')


class ChangeForm(FlaskForm):
    password=PasswordField(u'密码:',validators=[DataRequired(),Length(min=2,max=20),EqualTo('confirm',message="两次密码不一样")])
    confirm=PasswordField(u'确认密码:',validators=[DataRequired(),Length(min=2,max=20)])
    submit=SubmitField(u'确认修改')
