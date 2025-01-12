import markdown

from django.db import models
    
from django.contrib.auth.models import User

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    access_level = models.CharField(
        max_length=20,
        choices=[
            ('private', '私密'),
            ('protected', '密码保护'),
            ('shared', '受保护的'),
            ('public', '公开'),
        ],
        default='public',
    )
    access_password = models.CharField(max_length=100, blank=True, null=True)


