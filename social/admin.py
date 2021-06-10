from django.contrib import admin
from django.contrib.auth import models
from .models import Article,Comment, Like, Relationship, Hashtag



admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(Relationship)
admin.site.register(Like)
admin.site.register(Hashtag)
