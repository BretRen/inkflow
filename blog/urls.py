from django.urls import path
from . import views

urlpatterns = [
    path('', views.article_list, name='article_list'),  # 首页文章列表
    path('article/<int:pk>/', views.article_detail, name='article_detail'),  # 文章详情
]
