from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField
from wtforms.validators import DataRequired, Length
from shucourse.models import Student,Teacher,Admin,Course,Select
class LoginForm(FlaskForm):
    user_id=StringField(u'学号/工号',validators=[DataRequired(),Length(min=4,max=8)])
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
