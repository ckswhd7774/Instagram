from django.test import TestCase

# Create your tests here.

class ArticleView(View) :
    def get(self, request, *args, **kwargs) :
        return render(request, 'mypage.html')

    def post(self, request, *args, **kwargs) :
        article_dto = self._build_article_dto(self, request.POST)
        ArticleService.article(article_dto)

        return redirect('userinfo:mypage',kwargs['pk'])

    @staticmethod
    def _build_article_dto(self, post_data) :
        return ArticleDto (
            title=post_data['title'],
            article=post_data['article'],
            user=User.objects.filter(pk=self.kwargs['pk']).first(),
        )