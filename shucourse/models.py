from shucourse import db,login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    stu=Student.query.get((user_id))
    te=Teacher.query.get((user_id))
    if stu:
        return stu
    else:
        return te

#学生
class Student(db.Model,UserMixin):
    # student_id=db.Column(db.String(8),primary_key=True,unique=True)
    id=db.Column(db.String(8),primary_key=True,unique=True)
    student_name=db.Column(db.String(20),nullable=False)
    student_password=db.Column(db.String(20),nullable=False)
    student_dept=db.Column(db.String(2),nullable=False)
    # backref就是类似与新建一列
    selects=db.relationship('Select',backref='student',lazy=True)
    # 定义如何输出
    def __repr__(self):
        return f"Student('{self.id}','{self.student_name}','{self.student_password}','{self.student_dept}')"

#教师
class Teacher(db.Model,UserMixin):
    id=db.Column(db.String(4),primary_key=True,unique=True)
    teacher_name=db.Column(db.String(20),nullable=False)
    teacher_password=db.Column(db.String(20),nullable=False)
    teacher_dept=db.Column(db.Integer,nullable=False)
    # 教师职称
    teacher_stat=db.Column(db.String(20))
    def __repr__(self):
        return f"Teacher('{self.id}','{self.teacher_name}','{self.teacher_password}','{self.teacher_dept}')"

# 管理员
class Admin(db.Model,UserMixin):
    id=db.Column(db.String(4),primary_key=True,unique=True)
    admin_password=db.Column(db.String(20),nullable=False)
    def __repr__(self):
        return f"Admin('{self.id}','{self.admin_password}')"

# 课程表
class Course(db.Model):
    course_id=db.Column(db.String(8),primary_key=True,unique=True)
    course_name=db.Column(db.String(20),nullable=False)
    # 课程的教师号
    course_teacher=db.Column(db.String(8),nullable=False)
    # 开课时间
    course_time=db.Column(db.String(20))
    # 课程最多人数
    course_maxn=db.Column(db.Integer)
    course_xuefen=db.Column(db.Integer)
    # 是否开课
    course_open=db.Column(db.Boolean)
    grade=db.Column(db.Integer)
    def __repr__(self):
        return f"Course('{self.course_id}','{self.course_name}','{self.course_teacher}')"

# 选课表
class Select(db.Model):
    select_id=db.Column(db.Integer,primary_key=True,unique=True)
    # 外键
    course_id=db.Column(db.String(8),db.ForeignKey('course.course_id'),nullable=False)
    course_name=db.Column(db.String(20),db.ForeignKey('course.course_name'),nullable=False)
    # 外键
    teacher_id=db.Column(db.String(4),db.ForeignKey('teacher.id'),nullable=False)
    # 外键
    student_id=db.Column(db.String(8),db.ForeignKey('student.id'),nullable=False)
    student_grade=db.Column(db.Integer)

# 学院表
class Department(db.Model):
    dept_id=db.Column(db.String(2),primary_key=True,unique=True)
    dept_name=db.Column(db.String(20),nullable=False)
    def __repr__(self):
        return f"Select('{self.course_id}','{self.student_id}','{self.course_name}','{self.teacher_id}','{self.student_grade}'"



