from django.shortcuts import redirect, render, get_object_or_404
from .models import Article
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
import markdown


@login_required
def article_add(request):
    if request.method == 'POST':
        # 获取表单数据
        title = request.POST.get('title', '').strip()
        content = request.POST.get('content', '').strip()
        access_level = request.POST.get('access_level', 'public')  # 默认值为 'public'
        access_password = request.POST.get('access_password', '').strip()

        # 创建文章时设置所有者
        article = Article.objects.create(
            title=title,
            content=content,
            access_level=access_level,
            access_password=access_password,
        )
        print(access_level)

        return redirect('admin_article_list')

    return render(request, 'blog/edit_article.html')





def article_list(request):
    articles = Article.objects.all().order_by('-created_at')
    return render(request, 'blog/article_list.html', {'articles': articles})



def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)

    # 检查访问权限
    if article.access_level == 'private':
        if not article.is_owner(request.user):
            return HttpResponseForbidden("您无权查看此文章")

    elif article.access_level == 'protected':
        if 'access_password' not in request.session or request.session['access_password'] != article.access_password:
            return render(request, 'blog/access_password.html', {'article': article})

    elif article.access_level == 'shared':
        if 'shared_access_password' not in request.session or request.session['shared_access_password'] != article.access_password:
            return render(request, 'blog/access_password.html', {'article': article, 'shared': True})

    # 渲染文章内容（Markdown 支持）
    content_markdown = markdown.markdown(article.content, extensions=['fenced_code', 'tables'])

    # 渲染文章详情模板
    return render(request, 'blog/article_detail.html', {
        'article': article,
        'content_markdown': content_markdown
    })

def verify_password(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        input_password = request.POST['password']
        if article.access_level == 'protected' and input_password == article.access_password:
            request.session['access_password'] = input_password
            return redirect('article_detail', pk=pk)
        elif article.access_level == 'shared' and input_password == article.access_password:
            request.session['shared_access_password'] = input_password
            return redirect('article_detail', pk=pk)
        else:
            return render(request, 'blog/access_password.html', {
                'article': article,
                'error': '密码错误',
                'shared': article.access_level == 'shared'
            })

