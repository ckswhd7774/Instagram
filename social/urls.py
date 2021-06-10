from django import views
from django.contrib import admin
from django.urls import path
from social.views import ArticleListView, UserlistView, EditView, RelationshipView, ArticleDetailView, CommentView, UploadArticleView

from social import views

app_name = 'social'

urlpatterns = [
    # login required views
    path('mypage/<int:pk>', ArticleListView.as_view(), name='mypage'),
    path('article_detail/<int:pk>', ArticleDetailView.as_view(), name='article_detail'),
    path('mypage/upload/', views.create, name='upload_article'),
    path('edit/<pk>', EditView.as_view(), name='edit'),
    path('relationship/<pk>', RelationshipView.as_view(), name='relationship'),
    path('comment/<pk>', CommentView.as_view(), name='comment'),
    path('mypage/upload2', UploadArticleView.as_view(), name='upload_article2'),

    # common
    path('admin/', admin.site.urls),
    path('userlist/', UserlistView.as_view() ,name='userlist'),
]