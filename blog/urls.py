from django.urls import path
from . import views
from .views import article_detail, verify_password


urlpatterns = [
    
    path('', views.article_list, name='article_list'),  # 首页文章列表
    path('article/<int:pk>/', views.article_detail, name='article_detail'),  # 文章详情
    path('article/<int:pk>/', article_detail, name='article_detail'),
    path('article/<int:pk>/verify-password/', verify_password, name='verify_password'),
]
