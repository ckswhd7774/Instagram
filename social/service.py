from django.contrib.auth.models import User

from userinfo.models import Profile
from userinfo.dto import ArticleDto, CommentDto, EditDto, RelateDto
from social.models import Article, Comment ,Relationship

class ArticleService():
    @staticmethod
    def article(dto:ArticleDto) :
        Article.objects.create(
            title=dto.title,
            article=dto.article,
            user=dto.user,
            imnage=dto.image
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
            writer=dto.writer
        )

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
