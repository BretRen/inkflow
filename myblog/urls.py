from django.urls import path, include
from blog.admin import custom_admin_site  # 确保导入路径正确

urlpatterns = [
    path('admin/', custom_admin_site.urls),  # 自定义 Admin 面板
    path('', include('blog.urls')),  # 前端博客页面
    path('grappelli/', include('grappelli.urls')),  # Grappelli URL
]
