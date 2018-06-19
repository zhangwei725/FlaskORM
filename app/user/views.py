from flask import Blueprint

from .models import User

"""

"""
user = Blueprint('user', __name__)


# 过滤函数
# 执行查询函数


@user.route('/show/')
def show():
    # 查询所有的行跟列
    users = User.query.all()
    # 过滤列
    user = User.query.filter_by(name='test1').first()
    #     # 过滤行
    # filter 可以使用运算符
    users = User.query.filter(User.name == 'xm').all()

    #  select  uid,name from user  where nam='xm' and passwo=123456
    return '查询'
