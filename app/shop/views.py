from flask import Blueprint, request
import logging
from app.ext import db
from app.shop.models import Cate, Shop

shop = Blueprint('shop', __name__)


@shop.route('/add/')
def add():
    cates = []
    for i in range(1, 6):
        cates.append(Cate(cname='分类' + str(i)))
    # 批量插入数据
    db.session.bulk_save_objects(cates)
    db.session.commit()
    return "添加成功"


@shop.route('/add1/')
def add1():
    shops = []
    for i in range(1, 11):
        shops.append(Shop(name='商品' + str(i), cid=1))
        # 批量插入数据
    db.session.bulk_save_objects(shops)
    db.session.commit()
    return "添加商品信息"


# 通过一的方查多的一方
"""
优点 一次查询就把的一方加载出来了
缺点 当数据够大的时候很可能会拖慢系统的性能
"""


@shop.route('/list/')
def find():
    cates = Cate.query.all()
    # for cate in cates:
    # db.session.query(Shop.name).filter(cid=cate.cid).all()
    for shop in cates[0].shops:
        logging.debug(shop.name)

    # 通过一的一方查多的一方
    # shop = db.session.query(Shop.sid, Shop.name, Shop.cid).filter(Shop.sid == 1).first()
    # cate = Cate.query.get(shop.cid)

    return '通过一的方查多的一方'


# /shop?sid=1
@shop.route('/id/', methods=['get', 'post', 'put'])
def find_by_id():
    sid = request.values.get('sid', default=0, type=int)
    shop = Shop.query.get(sid)
    print(shop.name)
    print(shop.cate.cname)
    return '通过一的方查多的一方'
