from userinfo.models import Profile
from django.shortcuts import render
from django.views import generic
# Create your views here.

class UserlistView(generic.ListView) :
    model = Profile
    template_name = 'userlist.html'
    context_object_name = 'userlist'