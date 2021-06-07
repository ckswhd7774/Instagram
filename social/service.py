from userinfo.dto import ArticleDto
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
