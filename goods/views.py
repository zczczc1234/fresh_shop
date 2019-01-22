from django.shortcuts import render

from goods.models import Goods, GoodsCategory
from user.models import User


def index(request):
    if request.method == 'GET':
        # 如果访问首页，返回渲染的首页index.html页面
        # 思路：组装结果[object1,object2,object3,object4,object5,object6]
        # 组装结果的对象object：包含分类，改分类的前四个商品信息
        # 方式1 ： object ==> [GoodCategory Object,[Goods object1,Goods object2,Goods object3,Goods object4]]
        # 方式2 ： object ==> {'GoodCategory Object':[Goods object1,Goods object2,Goods object3,Goods object4]}

        categorys = GoodsCategory.objects.all()
        result = []
        for category in categorys:
            goods = category.goods_set.all()[:4] # 通过GoodsCategory表反向查询每个商品种类的商品
            data = [category,goods]
            result.append(data)
            category_type = GoodsCategory.CATEGORY_TYPE
        return  render(request,'index.html',{'result': result, 'category_type': category_type})


def detail(request,id):

    if request.method == 'GET':
        # 返回详情页面解析的商品信息
        goods = Goods.objects.filter(pk=id).first()
        goods_record = request.session.get('goods_record')
        if goods_record:
            flag = True
            for goods in goods_record:
                if goods == id:
                    goods_record.pop(goods)
                    goods_record.append(id)
                    flag = False
            if flag:
                goods_record.append(id)
            request.session['goods_record'] = goods_record
            print(goods_record)
        else:
            request.session['goods_record'] = [id]
            print(goods_record)


        return render(request,'detail.html',{'goods':goods})


def list(request,id):
    if request.method == 'GET':
        goodscategory = GoodsCategory.objects.filter(category_type=id).first()
        goods = goodscategory.goods_set.all()
        return render(request,'list.html',{'goods':goods})


