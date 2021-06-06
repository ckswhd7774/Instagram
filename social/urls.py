from django import views
from django.contrib import admin
from django.urls import path
from social.views import UserlistView

app_name = 'social'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('userlist/', UserlistView.as_view() ,name='userlist')
]