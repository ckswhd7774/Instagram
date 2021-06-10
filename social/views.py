from django.core.files.storage import FileSystemStorage
from django.http import request
from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.models import  User
from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from .models import Article

from social.service import ArticleService, CommentService, EditService, RelateService

from userinfo.service import UserService
from userinfo.forms import ArticleForm
from userinfo.dto import EditDto, RelateDto, CommentDto, ArticleDto

# Create your views here.

class UserlistView(generic.ListView) :
    model = User
    template_name = 'userlist.html'
    context_object_name = 'userlist'

    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context['user_list'] = User.objects.all()
        return context

class ArticleListView(generic.ListView):
    model = Article
    template_name = 'mypage.html'
    context_object_name = 'articles'

    def get(self, request, *args, **kwargs) :
        return render(request, 'mypage.html')

    def post(self, request, *args, **kwargs):
        article_dto = self._build_article_dto(self, request)
        ArticleService.article(article_dto)

        return redirect('social:mypage', kwargs['pk'])

    @staticmethod
    def _build_article_dto(self, request) :
        return ArticleDto (
        title=request.POST.get('title', 'NO TITLE'), 
        user = request.user, 
        article=request.POST.get('article', 'NO CONTENT'), 
        image=request.FILES.get('image', None)
        )

    def get_queryset(self) :
        return Article.objects.order_by()

class ArticleDetailView(generic.DetailView) :
    model = Article
    context_object_name = 'article'
    template_name = 'article_detail.html'

class EditView(View) :
    def get(self, request, *args, **kwargs) :
        context = {'user':UserService.find_by_user(kwargs['pk'])}
        return render(request, 'edit.html', context)

    def post(self, request, *args, **kwargs) :
        edit_dto = self._build_edit_dto(self, request.POST)
        EditService.edit(edit_dto)
        
        return redirect('userinfo:mypage', kwargs['pk'])

    @staticmethod
    def _build_edit_dto(self, post_data) :
        return EditDto (
            name=post_data['name'],
            introduce=post_data['introduce'],
            address=post_data['address'],
            pk=self.kwargs['pk']
        )

class UploadArticleView(View) :
    def get(self, request, *args, **kwargs) :
        return render(request, 'upload_article.html')

    def post(self, request, *args, **kwargs):
        article_dto = self._build_article_dto(self, request.POST)
        ArticleService.article(article_dto)

        return redirect('social:mypage', kwargs['pk'])

    @staticmethod
    def _build_article_dto(self, request) :
        return ArticleDto (
        title=request.POST.get('title', 'NO TITLE'), 
        user = request.user, 
        article=request.POST.get('article', 'NO CONTENT'), 
        image=request.FILES.get('image', None)
        )


def create(request) :
    if request.method == 'POST' :
        new_article = Article(
        title=request.POST.get('title', 'NO TITLE'), 
        user = request.user, 
        article=request.POST.get('article', 'NO CONTENT'), 
        image=request.FILES.get('image', None))
        new_article.save()

        return redirect('social:article_list')
    else :
        return render(request, 'upload_article.html')
            

class CommentView(View) :
    def get(self, request, *args, **kwargs) :
        return render(request, 'article_detail.html')

    def post(self, request, *args, **kwargs) :
        comment_dto = self._build_comment_dto(self, request)
        CommentService.comment(comment_dto)

        return redirect('social:article_detail', kwargs['pk'])

    @staticmethod
    def _build_comment_dto(self, request) :
        return CommentDto (
            owner=User.objects.filter(pk=self.kwargs['pk']).first(),
            writer=request.user,
            content=request.POST['content']
        )
    

class RelationshipView(View) :
    def get(self, request, *args, **kwargs) :
        return render(request, 'userinfo:mypage')

    def post(self, request, *args, **kwargs) :
        relate_dto = self._build_relate_dto(self, request)
        RelateService.toggle(relate_dto)

        return redirect('userinfo:mypage', kwargs['pk'])

    @staticmethod
    def _build_relate_dto(self, request) :
        return RelateDto (
            user_pk=self.kwargs['pk'],
            requester=request.user
        )

