from django import views
from django.contrib import admin
from django.urls import path
from social.views import UserlistView, ArticleView, EditView, RelationshipView

app_name = 'social'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('userlist/', UserlistView.as_view() ,name='userlist'),
    path('article/<pk>', ArticleView.as_view(), name='article'),
    path('edit/<pk>', EditView.as_view(), name='edit'),
    path('relationship/<pk>', RelationshipView.as_view(), name='relationship'),
]
