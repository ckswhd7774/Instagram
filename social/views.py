from userinfo.service import UserService
from django.http import request
from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.models import  User
from django.shortcuts import render
from django.views import generic

from social.service import ArticleService, EditService
from userinfo.dto import ArticleDto, EditDto
# Create your views here.

class UserlistView(generic.ListView) :
    model = User
    template_name = 'userlist.html'
    context_object_name = 'userlist'

    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context['user_list'] = User.objects.all()
        return context

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