from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import SET_NULL
from django.db.models.fields.related import ForeignKey, OneToOneField
from django.shortcuts import redirect, render
from behaviors import BaseFiled
# Create your models here.

class Article(BaseFiled) :
    title = models.CharField(max_length=64)
    article = models.TextField()
    user = ForeignKey(User, on_delete=models.CASCADE, related_name='article', null=True, blank=True)
    image = models.ImageField(upload_to='image/', blank=True, null=True)

    def __str__(self):
        return (f"{self.id}" + "by " + self.user.username + "/" + self.title)

class Comment(BaseFiled) :
    # 어떤 글에 대한 댓글인가 / 댓글에 대한 게시물
    owner = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='owner', null=True, blank=True)
    # 댓글 쓴 사람
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='writer', null=True, blank=True)
    content = models.TextField()


class LikeComment(BaseFiled) :
    # 댓글에 대한 좋아요
    comment = models.OneToOneField(Comment, on_delete=models.SET_NULL, related_name='like', null=True, blank=True)
    users = models.ManyToManyField(User, related_name='like_comment', blank=True)

class LikeArticle(BaseFiled) :
    # 게시글에 대한 좋아요
    article = models.OneToOneField(Article, on_delete=models.SET_NULL, related_name='like_article', null=True, blank=True)
    users = models.ManyToManyField(User, related_name='like_article', blank=True)


class Relationship(BaseFiled) :
    users = models.OneToOneField(User, on_delete=models.SET_NULL, related_name='relationship' , null=True, blank=True)
    # 내가 팔로우 하고 있는 사람들
    followers = models.ManyToManyField(User, related_name='following', blank=True)


class Hashtag(BaseFiled) :
    users = models.ManyToManyField(User, related_name='tag', blank=True)
    # 태그되어있는 게시물
    article = models.ManyToManyField(Article, related_name='article_tag', blank=True)