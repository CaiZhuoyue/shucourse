from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField
from wtforms.validators import DataRequired, Length
from shucourse.models import Student,Teacher
class LoginForm(FlaskForm):
    user_id=StringField(u'学号/工号',validators=[DataRequired(),Length(min=8,max=8)])
    password=PasswordField(u'密码',validators=[DataRequired()])
    remember=BooleanField(u'记住我')
    submit=SubmitField(u'登陆')
    