from django import views
from django.contrib import admin
from django.urls import path
from social.views import MypageView, UserlistView, EditView, RelationshipView, ArticleDetailView, CommentView, UploadArticleView, CommentLikeView

app_name = 'social'

urlpatterns = [
    # login required views
    path('mypage/<int:pk>', MypageView.as_view(), name='mypage'),
    path('article_detail/<int:pk>', ArticleDetailView.as_view(), name='article_detail'),
    path('mypage/upload', UploadArticleView.as_view(), name='upload_article'),
    path('edit/<pk>', EditView.as_view(), name='edit'),
    path('relationship/<pk>', RelationshipView.as_view(), name='relationship'),
    path('comment/<pk>', CommentView.as_view(), name='comment'),
    path('like/<int:pk>', CommentLikeView.as_view(), name='like'),

    # common
    path('admin/', admin.site.urls),
    path('userlist/', UserlistView.as_view() ,name='userlist'),
]