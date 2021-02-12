# SHU-course-system

上海大学计算机学院2021数据库1大作业 SHU选课系统

by 可爱的蔡卓悦

### 项目技术栈：
后端 python flask框架


### 具体步骤
1. 第一步：github创建项目 git clone项目到本地
2. 在vscode中打开项目并创建虚拟环境`virtualenv VENV` 使用虚拟环境 `source VENV/bin/activate`
3. 安装需要的包和依赖（区别是什么？）
```
    pip3 install flask   
    pip3 install flask_sqlalchemy
    pip3 install flask-wtf
    pip3 install flask_bcrypt
```
4. SQLAlchemy的使用
    
    新建models.py文件 在里面我们会存放需要在数据库中出现的表的python类
    定义完毕之后在项目根目录下打开终端
```
    from models import db
    db.create_all()
    from models import Student,Teacher
    student_1=Student(student_name='caizhuoyue',student_id='18120***',student_password='123123',student_dept=1)
    student_2=Student(student_name='alibaba',student_id='18120***',student_password='123123',student_dept=2)
    db.session.add(student_1)
    db.session.add(student_2)
    db.session.commit()  
    db.query.all()
```