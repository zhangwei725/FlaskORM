import datetime

from app.ext import db


# 约束
# 主键约束  唯一约束  非空约束  默认约束
# 外键约束 关联关系

# 常用的数据类型
# 数字相关
# 字符串
# 日期时间
# 大文本  二进制数据

# 1000.00
# 100000
# query


class User(db.Model):
    # __tablename__ = 't_user'
    uid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True, nullable=True)
    weight = db.Column(db.Float(10, 2))
    # # decimal
    money = db.Column(db.Numeric(10, 2))
    create_date = db.Column(db.DateTime, default=datetime.datetime.now())
    # # 不要在text字段上面加索引
    msg = db.Column(db.Text())


# 角色===权限  增删改查的权限
#
# 管理员角色    增删改查的权限
# 普通用户      增查权限
"""
定义多对多第三张表
参数 表的名称
"""

relation = db.Table('role_permission_relation',
                    db.Column('id', db.Integer, primary_key=True),
                    db.Column('per_id', db.Integer, db.ForeignKey('permission.per_id')),
                    db.Column('role_id', db.Integer, db.ForeignKey('role.role_id')))


# secondary 用于多对多,指向第三张表
class Role(db.Model):
    role_id = db.Column(db.Integer, primary_key=True)
    role_name = db.Column(db.String(64), nullable=False, index=True, unique=True)
    desc = db.Column(db.Text)
    permissions = db.relationship('Permission', secondary=relation)

    def __init__(self, role_name, desc):
        self.role_name = role_name
        self.desc = desc


# 权限


class Permission(db.Model):
    per_id = db.Column(db.Integer, primary_key=True)
    per_name = db.Column(db.String(64), nullable=False, index=True, unique=True)
    desc = db.Column(db.Text)

    def __init__(self, per_name, desc):
        self.per_name = per_name
        self.desc = desc
