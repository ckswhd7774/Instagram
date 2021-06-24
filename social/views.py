from django.http import request
from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.models import  User
from django.shortcuts import render
from django.views import generic
from boto3.session import Session
from datetime import date, datetime
from .models import Article

from config.settings import AWS_ACCESS_KEY_ID, AWS_S3_REGION_NAME, AWS_SECRET_ACCESS_KEY, AWS_STORAGE_BUCKET_NAME

import boto3
from social.service import ArticleService, CommentService, EditService, LikeService, RelateService

from userinfo.service import UserService
from userinfo.dto import EditDto, RelateDto, CommentDto, ArticleDto, LikeDto

# Create your views here.

class UserlistView(generic.ListView) :
    model = User
    template_name = 'user_list.html'
    context_object_name = 'userlist'

class UserdetailView(generic.DetailView):
    model = User
    template_name = 'user_detail.html'
    context_object_name = 'user'

    def get(self, request, *args, **kwargs) :
        context = {'user':UserService.find_by_user(kwargs['pk'])}
        return render(request, 'user_detail.html', context)

    def post(self, request, *args, **kwargs):
        # article_dto = self._build_article_dto(self, request)
        # ArticleService.article(article_dto)

        file = request.FILES.get('image')
        session = Session(
            aws_access_key_id=AWS_ACCESS_KEY_ID,
            aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
            region_name=AWS_S3_REGION_NAME,
        )
        s3 = session.resource('s3')
        now = datetime.now().strftime('%Y%H%M%S')
        img_object = s3.Bucket(AWS_STORAGE_BUCKET_NAME).put_object(
            Key=now+file.name,
            Body=file
        )

        s3_url = 'https://django-s3-cj.s3.ap-northeast-2.amazonaws.com/'
        Article.objects.create(
            title=request.POST['title'],
            user = request.user,
            article= request.POST.get('article'),
            url = s3_url+now+file.name
        )

        return redirect('social:user_detail', kwargs['pk'])

    @staticmethod
    def _build_article_dto(self, request) :
        return ArticleDto (
        title=request.POST.get('title', 'NO TITLE'), 
        user = request.user, 
        article=request.POST.get('article', 'NO CONTENT'), 
        url=request.FILES.get('image', None)
        )
    # def get_queryset(self) :
    #     return Article.objects.order_by()


class PostDetailView(generic.DetailView) :
    model = Article
    context_object_name = 'article'
    template_name = 'post_detail.html'


class EditView(View) :
    def get(self, request, *args, **kwargs) :
        context = {'user':UserService.find_by_user(kwargs['pk'])}
        return render(request, 'edit.html', context)

    def post(self, request, *args, **kwargs) :
        edit_dto = self._build_edit_dto(self, request.POST)
        EditService.edit(edit_dto)
        
        return redirect('social:user_detail', kwargs['pk'])

    @staticmethod
    def _build_edit_dto(self, post_data) :
        return EditDto (
            name=post_data['name'],
            introduce=post_data['introduce'],
            address=post_data['address'],
            pk=self.kwargs['pk']
        )

class UploadPostView(View) :
    def get(self, request, *args, **kwargs) :
        return render(request, 'upload_post.html')

    def post(self, request, *args, **kwargs):
        # article_dto = self._build_article_dto(self, request.POST)
        # ArticleService.article(article_dto)
        file = request.FILES.get('image')
        session = Session(
            aws_access_key_id=AWS_ACCESS_KEY_ID,
            aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
            region_name=AWS_S3_REGION_NAME,
        )
        s3 = session.resource('s3')
        now = datetime.now().strftime('%Y%H%M%S')
        img_object = s3.Bucket(AWS_STORAGE_BUCKET_NAME).put_object(
            Key=now+file.name,
            Body=file
        )

        s3_url = 'https://django-s3-cj.s3.ap-northeast-2.amazonaws.com/'
        Article.objects.create(
            title=request.POST['title'],
            user = request.user,
            article= request.POST.get('article'),
            url = s3_url+now+file.name
        )

        return redirect('social:user_list', kwargs['pk'])

    # @staticmethod
    # def _build_article_dto(self, request) :
    #     return ArticleDto (
    #     title=request.POST.get('title', 'NO TITLE'), 
    #     user = request.user, 
    #     article=request.POST.get('article', 'NO CONTENT'), 
    #     image=request.FILES.get('image', None)
    #     )

class CommentView(View) :
    def get(self, request, *args, **kwargs) :
        return render(request, 'post_detail.html')

    def post(self, request, *args, **kwargs) :
        comment_dto = self._build_comment_dto(self,request)
        CommentService.comment(comment_dto)
        owner = CommentService.find_owner(kwargs['pk'])
        return redirect('social:post_detail', owner.pk)

    @staticmethod
    def _build_comment_dto(self, request) :
        return CommentDto (
            article_pk=self.kwargs['pk'],
            owner=CommentService.find_owner(self.kwargs['pk']),
            writer=request.user,
            content=request.POST['content'],
        )

class CommentLikeView(View) :
    # def get(self, request, *args, **kwargs) :
    #     return render(request, 'post_detail.html')

    def post(self, request, *args, **kwargs) :
        like_dto = self._build_like_dto(self, request)
        LikeService.toggle(like_dto)
        return redirect('social:post_detail', kwargs['pk'])

    @staticmethod
    def _build_like_dto(self, request) :
        return LikeDto(
            comment_pk=self.kwargs['pk'],
            users=request.user
        )

class RelationshipView(View) :
    def get(self, request, *args, **kwargs) :
        return render(request, 'social:user_list')

    def post(self, request, *args, **kwargs) :
        relate_dto = self._build_relate_dto(self, request)
        RelateService.toggle(relate_dto)

        return redirect('social:user_detail', kwargs['pk'])

    @staticmethod
    def _build_relate_dto(self, request) :
        return RelateDto (
            user_pk=self.kwargs['pk'],
            requester=request.user
        )

        