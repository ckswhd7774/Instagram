from django.contrib import admin
from django.contrib.auth import models
from .models import Article,Comment, LikeComment, LikeArticle, Relationship, Hashtag



admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(LikeComment)
admin.site.register(LikeArticle)
admin.site.register(Relationship)
admin.site.register(Hashtag)
