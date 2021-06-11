from django.contrib.auth.models import User
from django.http import request

from userinfo.models import Profile
from userinfo.dto import ArticleDto, CommentDto, EditDto, LikeDto, RelateDto
from social.models import Article, Comment, LikeComment ,Relationship
from django.shortcuts import get_object_or_404, get_list_or_404

class ArticleService():
    @staticmethod
    def article(dto:ArticleDto) :
        Article.objects.create(
            title=dto.title,
            article=dto.article,
            user=dto.user,
            image=dto.image
        )

    @staticmethod
    def find_all():
        return Article.objects.all()

class EditService() :
    @staticmethod
    def edit(dto:EditDto) :
        Profile.objects.filter(pk=dto.pk).update(
            name=dto.name,
            introduce=dto.introduce,
            address=dto.address
        )

class CommentService() :
    @staticmethod
    def comment(dto:CommentDto) :
        Comment.objects.create(
            content=dto.content,
            owner=dto.owner,
            writer=dto.writer,
            article=dto.article
        )

class LikeService() :
    @staticmethod
    def toggle(dto:LikeDto) :
        print(dto.comment_pk)
        user = get_object_or_404(User, pk=dto.users.pk)
        comment = get_object_or_404(Comment, pk=dto.comment_pk)
        like = LikeComment.objects.filter(comment__pk=dto.comment_pk).first()

        if like is None :
            like = LikeComment.objects.create(comment=comment)
            
        if dto.users in like.users.all() :
            like.users.remove(dto.users)

        else :
            like.users.add(dto.users)



class RelateService() :
    @staticmethod
    def toggle(dto:RelateDto) :
        users = User.objects.filter(pk=dto.user_pk).first()
        relationship = Relationship.objects.filter(users=users).first()

        if relationship is None :
            relationship = Relationship.objects.create(users=users)
        if (dto.requester) in (relationship.followers.all()) :
            relationship.followers.remove(dto.requester)
        else :
            relationship.followers.add(dto.requester)
