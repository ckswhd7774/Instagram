from django import views
from django.contrib import admin
from django.urls import path
from social.views import ArticleListView, UserlistView, EditView, RelationshipView, ArticleDetailView, CommentView

from social import views

app_name = 'social'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('userlist/', UserlistView.as_view() ,name='userlist'),
    # path('article/<pk>', ArticleView.as_view(), name='article'),
    path('edit/<pk>', EditView.as_view(), name='edit'),
    path('relationship/<pk>', RelationshipView.as_view(), name='relationship'),
    path('article_list/', ArticleListView.as_view(), name='article_list'),
    path('article_list/upload/', views.create, name='upload_article'),
    path('article_detail/<int:pk>', ArticleDetailView.as_view(), name='article_detail'),
    path('comment/<pk>', CommentView.as_view(), name='comment')
]
