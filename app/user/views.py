from operator import and_, or_

from flask import Blueprint, render_template

from app.ext import db
from .models import User

"""

"""
user = Blueprint('user', __name__)


# 过滤函数
# 执行查询函数
# fLask 1.0
@user.route('/show/')
def show():
    # 过滤列
    query = db.session.query(User.name).all()
    # 查询所有的行跟列
    users = User.query.all()
    user = User.query.filter_by(name='test1').first()
    #     # 过滤行
    # filter 可以使用运算符
    users = User.query.filter(User.name == 'xm').all()
    #  select  uid,name from user  where nam='xm' and passwo=123456
    return '查询'


# 过滤器
@user.route('/1/')
def filter01():
    name = 'test'
    # %s%
    User.query.filter(User.name.like('%' + name + '%'))
    # s%
    User.query.filter(User.name.startswith())
    # %s
    User.query.filter(User.name.endswith())
    # IN  NOT IN
    User.query.filter(~User.name.in_(['t', 's', 'c']))
    # is null
    User.query.filter(User.name is None)
    # is not null
    User.query.filter(User.name is not None)
    User.query.filter(and_(User.name == 'test1', User.weight > 120.00))
    # 也可以
    # User.query.filter(User.name == 'test1').filter(User.weight > 120.00)
    # or
    User.query.filter(or_(User.name == '小明', User.desc.like('%说%')))
    return '常用的操作符'


"""
page*size
select  * from user
limit 0 10
"""
1 * 10


# page   pagezize
# 分页
# limit  表示去多少条数据
# offset 表示偏移量  表示从设置的偏移量大小+1开始获取数据
# 计算最大页数


#


@user.route('/limit/<int:page>/<int:size>/')
def query_limit(page, size):
    # 注意:做分页的不需要设置执行函数
    # users = db.session.query(User.name, User.uid, User.create_date).order_by(User.uid).limit(size).offset(
    #     (page - 1) * size)
    #
    # total = User.query.count() / size if User.query.count() % size == 0 else User.query.count() / size + 1
    # print(total)
    # users = User.query.order_by().slice((page - 1) * size, page * size)
    #
    paginate = User.query.order_by(User.uid).paginate(page=page, per_page=size, error_out=False)
    users = paginate.items
    print(paginate.total)
    print(paginate.pages)
    return render_template('user/users.html', users=users)


# 什么是事务  指的一系列操作, 这些操作要么一起成功要么全部失败
@user.route('/save/')
def save_all():
    # db.session.save_all()
    # # insert into user (name) values('test')
    objects = []
    for i in range(1, 101):
        objects.append(User(name='test' + str(i)))
    db.session.bulk_save_objects(objects)
    # insert  into user (name) values('test1'),('test')
    db.session.commit()
    return '批量保存'
