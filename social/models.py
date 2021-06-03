from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import SET_NULL
from django.db.models.fields.related import ForeignKey, OneToOneField
from userinfo.models import Profile
from behaviors import BaseFiled
# Create your models here.

class Article(BaseFiled) :
    title = models.CharField(max_length=64)
    article = models.TextField()
    user = ForeignKey(Profile, on_delete=models.CASCADE, related_name='article_user', null=True, blank=True)


class Comment(BaseFiled) :
    # 어떤 글에 대한 댓글인가 / 댓글에 대한 게시물
    owner = models.ForeignKey(Article, on_delete=SET_NULL, related_name='owner', null=True, blank=True)
    # 댓글 쓴 사람
    writer = models.ForeignKey(Article, on_delete=SET_NULL, related_name='writer', null=True, blank=True)
    content = models.TextField()


class Like(BaseFiled) :
    # 게시글에 대한 좋아요
    article = models.OneToOneField(Article, on_delete=SET_NULL, related_name='like_article', null=True, blank=True)
    # 댓글에 대한 좋아요
    comment = models.OneToOneField(Comment, on_delete=SET_NULL, related_name='like_comment', null=True, blank=True)
    users = models.ManyToManyField(User, related_name='like', blank=True)


class Relationship(BaseFiled) :
    users = models.OneToOneField(User, on_delete=SET_NULL, related_name='relationship' , null=True, blank=True)
    # 내가 팔로우 하고 있는 사람들
    followers = models.ManyToManyField(User, related_name='following', blank=True)


class Hashtag(BaseFiled) :
    users = models.ManyToManyField(User, related_name='tag', blank=True)
    # 태그되어있는 게시물
    article = models.ManyToManyField(Article, related_name='article_tag', blank=True)