from django.contrib import admin
from .models import Article, Comment, Like, Relationship, Hashtag
# Register your models here.

admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(Relationship)
admin.site.register(Like)
admin.site.register(Hashtag)