from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views_admin

urlpatterns = [
    path('', login_required(views_admin.dashboard), name='dashboard'),
    path('articles/', login_required(views_admin.article_list), name='admin_article_list'),
    path('articles/add/', login_required(views_admin.article_add), name='admin_article_add'),
    path('articles/edit/<int:pk>/', login_required(views_admin.article_edit), name='admin_article_edit'),
    path('articles/delete/<int:pk>/', login_required(views_admin.article_delete), name='admin_article_delete'),
    path('login/', views_admin.admin_login, name='admin_login'),
    path('logout/', views_admin.admin_logout, name='admin_logout'),
]
