from django.urls import path

from goods import views

urlpatterns = [
    # 首页
    path('index/',views.index,name='index'),
    # 详情页面
    path('detail/<int:id>/',views.detail,name='detail'),
    #商品列表
    path('list/<int:id>/',views.list,name='list'),

]
