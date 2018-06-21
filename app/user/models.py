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



