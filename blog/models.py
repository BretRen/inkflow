import markdown

from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=200)  # 文章标题
    content = models.TextField()             # 文章内容 (Markdown)
    excerpt = models.TextField(blank=True, null=True)  # 文章摘要
    created_at = models.DateTimeField(auto_now_add=True)  # 创建时间
    updated_at = models.DateTimeField(auto_now=True)      # 更新时间

    def render_markdown(self):
        """渲染 Markdown 内容，支持 Mermaid 图表等高级功能"""
        extensions = [
            'markdown.extensions.fenced_code',  # 支持代码块
            'markdown.extensions.codehilite',  # 代码高亮
            'markdown.extensions.tables',      # 表格支持
            'pymdownx.tasklist',               # 任务列表
            'pymdownx.tilde',                  # 支持删除线
            'pymdownx.emoji',                  # 支持表情符号
            'pymdownx.superfences',            # 高级代码块支持
            'markdown.extensions.extra',       # 其他扩展
        ]
        rendered_content = markdown.markdown(self.content, extensions=extensions)
        return rendered_content
