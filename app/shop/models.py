#    外键
# 1>在主表建立外键连接的关系
# 2>在子表建立外键
from app.ext import db

"""
单向引用

双向引用
商品 --> 主表     详情表 ----> 子表

一对一  关系   
在商品中有详情的对象,在详情表没有商品的对象 这种叫单向
在商品中有详情的对象,在详情表中也有商品的对象
"""


# 建立引用
#  详情的主表
class Shop(db.Model):
    sid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True, nullable=True)
    #     建立外键关联字段 可以使用表名.字段  也可以使用类名.属性
    # cid = db.Column(db.Integer, db.ForeignKey(Cate.cid))
    # 只是单纯建立外键关系
    cid = db.Column(db.Integer, db.ForeignKey('cate.cid'))
    # 如果想建立关系 也就是说想通过子表查询出
    cate = db.relationship('Cate', back_populates='shops')
    detail = db.relationship('Detail', backref='shop', uselist=False)


# 商品的子表
class Detail(db.Model):
    did = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Numeric(10, 2))
    sid = db.Column(db.Integer, db.ForeignKey(Shop.sid, ondelete='CASCADE'))


"""
查询
增加 先添加主表,才能添加子表数据
更新
删除 删除主表数据 cascade set_null






"""


class Cate(db.Model):
    cid = db.Column(db.Integer, primary_key=True)
    cname = db.Column(db.String(64), index=True, unique=True, nullable=True)
    # 建立关联关系的对象 懒加载
    """
    参数一 argument 关联的对象的类名
    参数二  lazy  不能用于多对一 或者一对一上
            可选项:
            1> select 默认值 一条sql一句把所有的相关的数据全部查出来
            2> dynamic 只查询主表的数据,生成查询子表的sql 当我们需要使用子表的数据的时候在去查询
            3> immediate  等主表数据查询完成之后再去查询子表数据

    back_populates  方向引用(当两个对象需要双向引用的时候使用)
                    值对应双向引用对象的字段
    # backref  backref='cate' 例如可以使用 shop.cate
    uselist=None, 如果想建立一对一的关系 直接在 uselist=false
    order_by=False,指定查询子表的排序字段
    """
    # 解决开发中有些时候查询主表相关联的子表的数据过大时
    # 默认是 select 立即加载
    # dynamic 懒加载  只会加载主表的数据,不会把子表的数据也加载进内存(只会生成sql语句,
    # 当我们需要用到数据的时候,去执行查询吧数据加载进内存)
    shops = db.relationship('Shop', back_populates='cate', order_by=Shop.sid, lazy='dynamic')
    # 只能用于一对多 还多对多  能通过一的一方的查询吧多的一方也查询出来
    shops = db.relationship('Shop', back_populates='cate', lazy='dynamic')

# 老版本
# class Cate(db.Model):
#     cid = db.Column(db.Integer, primary_key=True)
#     cname = db.Column(db.String(64), index=True, unique=True, nullable=True)
#     shops = db.relationship('Shop', backref='cate', lazy='dynamic')

# class Shop(db.Model):
#     sid = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(64), index=True, unique=True, nullable=True)
#     cid = db.Column(db.Integer, db.ForeignKey('cate.cid'))
# 对多多肯定有第三张表
