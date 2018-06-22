from flask import Blueprint, request, render_template, redirect
from app.ext import db
from app.shop.models import Shop

homework = Blueprint('homework', __name__, template_folder='templates')


# /work/list/1/10/
@homework.route('/list/')
def list():
    # get 请求
    # request.args
    # post请求还有 put
    # request.form
    page = request.values.get('page', default=1, type=int)
    #
    size = request.values.get('size', default=10, type=int)
    paginate = db.session.query(Shop.sid, Shop.name).order_by(Shop.sid).paginate(page=page, per_page=size,
                                                                                 error_out=False)
    shops = paginate.items
    return render_template('shops.html', shops=shops, paginate=paginate)

"""
添加商品
"""


@homework.route('/add/', methods=['get', 'post'])
def add():
    if request.method == 'GET':
        return render_template('add.html')
    elif request.method == 'POST':
        name = request.values.get('name')
        cid = request.values.get('cid', default=1, type=int)
        shop = Shop(name=name, cid=cid)
        db.session.add(shop)
        db.session.commit()
        return redirect('/work/list/')


@homework.route('/update/', methods=['GET', 'POST'])
def update():
    if request.method == 'GET':
        sid = request.values.get('sid', type=int)
        shop = Shop.query.get(sid)
        return render_template('update.html', shop=shop)
    elif request.method == 'POST':
        sid = request.values.get('sid', type=int)
        cid = request.values.get('cid', type=int)
        name = request.values.get('name')
        Shop.query.filter(Shop.sid == sid).update({Shop.cid: cid, Shop.name: name})
        db.session.commit()
        return redirect('/work/list/')


@homework.route('/del/')
def delete():
    sid = request.values.get('sid', type=int)
    db.session.delete(Shop.query.get(sid))
    db.session.commit()
    return redirect('/work/list/')
