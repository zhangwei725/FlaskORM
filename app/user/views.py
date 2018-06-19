from flask import Blueprint

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
