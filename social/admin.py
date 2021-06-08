from django.contrib import admin
from django.contrib.auth import models
from .models import Article, Photo,Comment, Like, Relationship, Hashtag
# Register your models here.
# Photo 클래스를 Inline으로 나타낸다.
class PhotoInline(admin.TabularInline) :
    model = Photo

class ArticleAdmin(admin.ModelAdmin) :
    inlines = [PhotoInline, ]

admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)
admin.site.register(Relationship)
admin.site.register(Like)
admin.site.register(Hashtag)
admin.site.register(Photo)
