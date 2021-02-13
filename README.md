# SHU-course-system

上海大学计算机学院2021数据库1大作业 SHU选课系统

by 可爱的蔡卓悦

### 项目技术栈：
后端 python flask框架
前端 bootstrap

### 项目文件目录
- static文件夹：css样式文件
- templated文件夹：html网页
  - layout.html 学生选课系统的基本页面
  - layout2.html 老师系统的基本页面
  - login.html 学生登陆页面
  - login2.html 老师登陆页面
  - select.html 学生选课页面
  - delete.html 学生退课页面
  - welcome.html **所有用户**经过的欢迎页面
  - home.html 学生home
  - home2.html 教师home
  - home3.html 管理员home
  - grade.html 学生成绩查询
  - grade2.html 教师登/修改成绩
  - about.html 关于本项目的介绍
- routes.py 路由和处理
- models.py 模型和类
- forms.py 各种表单的提交
- site.db sqlite数据库
- __init__.py flask网站入口

### 数据格式
-  学生学号8位
-  教师号4位
-  管理员号4位
-  密码长20位以下


### 实现的功能
- 教师登陆
  - 增删改成绩
  - 改密码
- 学生登陆
  - 选课 *
  - 退课 *
  - 查成绩
  - 改密码
- 管理员登陆
  - 增删改学生
  - 增删改老师
  - 增删改课程
  - 增加管理员？
  
### 进度记录
- 2月12日 
  - 学生选课退课界面基本完成
  - 学生登陆完成
  - 教师登陆完成
- 2月13日
  - 管理员登陆完成
  - 预计完成教师登陆成绩
  - 预计完成管理员增删改学生、教师和管理员
  - 预计完成学生改自己的密码




### 具体步骤
1. 第一步：github创建项目 git clone项目到本地
2. 在vscode中打开项目并创建虚拟环境`virtualenv VENV` 使用虚拟环境 `source VENV/bin/activate`
3. 安装需要的包和依赖（区别是什么？）
```
    pip3 install flask   
    pip3 install flask_sqlalchemy
    pip3 install flask-wtf
    pip3 install flask_bcrypt
    pip3 install flask_login
```
4. SQLAlchemy的使用
    
    新建models.py文件 在里面我们会存放需要在数据库中出现的表的python类
    
    使用`from models import db` `db.create_all()`就可以在建表

    手动插入数据：
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

5. 实现登陆功能（不需要注册）
   我发现好像需要把student_id设置为id才能正常登陆
