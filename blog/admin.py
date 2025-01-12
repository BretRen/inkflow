from django.contrib import admin
from django.contrib.admin import AdminSite
from .models import Article


class CustomAdminSite(AdminSite):
    site_header = "InkFlow 管理后台"
    site_title = "InkFlow 后台"
    index_title = "欢迎来到 InkFlow 管理后台"

    def each_context(self, request):
        context = super().each_context(request)
        context['css_files'] = ['css/custom_admin.css']
        context['js_files'] = ['js/custom_admin.js']
        return context


# 实例化自定义 AdminSite
custom_admin_site = CustomAdminSite(name='custom_admin')


# 将模型注册到 custom_admin_site
@admin.register(Article, site=custom_admin_site)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
