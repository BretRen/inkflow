from django.shortcuts import render, get_object_or_404, redirect
from .models import Article
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test

# 检查用户是否是超级管理员
def is_superadmin(user):
    return user.is_superuser

@user_passes_test(is_superadmin)
def dashboard(request):
    return render(request, 'blog/admin/dashboard.html')

# 登录视图
def admin_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_superuser:
                login(request, user)
                return redirect('dashboard')
            else:
                return render(request, 'blog/admin/login.html', {'error': '仅超级管理员可登录'})
        else:
            return render(request, 'blog/admin/login.html', {'error': '用户名或密码错误'})
    return render(request, 'blog/admin/login.html')

# 注销视图
def admin_logout(request):
    logout(request)
    return redirect('admin_login')

# 管理后台首页
def dashboard(request):
    return render(request, 'blog/admin/dashboard.html')

# 文章列表
def article_list(request):
    articles = Article.objects.all().order_by('-created_at')
    return render(request, 'blog/admin/article_list.html', {'articles': articles})

# 添加文章
def article_add(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        Article.objects.create(title=title, content=content)
        return redirect('admin_article_list')
    return render(request, 'blog/admin/article_form.html')

# 编辑文章
def article_edit(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        article.title = request.POST['title']
        article.content = request.POST['content']
        article.save()
        return redirect('admin_article_list')
    return render(request, 'blog/admin/article_form.html', {'article': article})

# 删除文章
def article_delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.delete()
    return redirect('admin_article_list')
