from django import views
from django.contrib import admin
from django.urls import path
from social.views import UserdetailView, UserlistView, EditView, RelationshipView, PostDetailView, CommentView, UploadPostView, CommentLikeView

app_name = 'social'

urlpatterns = [
    # login required views
    path('uesrdetail/<int:pk>', UserdetailView.as_view(), name='user_detail'),
    path('article_detail/<int:pk>', PostDetailView.as_view(), name='post_detail'),
    path('userdetail/upload', UploadPostView.as_view(), name='upload_post'),
    path('edit/<pk>', EditView.as_view(), name='edit'),
    path('relationship/<pk>', RelationshipView.as_view(), name='relationship'),
    path('comment/<pk>', CommentView.as_view(), name='comment'),
    path('like/<int:pk>', CommentLikeView.as_view(), name='like'),

    # common
    path('admin/', admin.site.urls),
    path('userlist/', UserlistView.as_view() ,name='user_list'),
]