from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # 默认 Django 管理后台
    path('inkflow-admin/', include('blog.urls_admin')),  # 自定义管理后台
    path('', include('blog.urls')),  # 前端博客页面
]

