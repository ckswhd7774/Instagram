from userinfo.models import Profile
from userinfo.dto import ArticleDto, EditDto
from social.models import Article

class ArticleService():
    @staticmethod
    def article(dto:ArticleDto) :
        Article.objects.create(
            title=dto.title,
            article=dto.article,
            user=dto.user
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