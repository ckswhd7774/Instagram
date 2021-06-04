from userinfo.service import UserService
from django.shortcuts import redirect, render
from django.views import View
from django.contrib import auth
from django.views import generic

from userinfo.dto import SignupDto
# Create your views here.

class IndexTemplateView(generic.TemplateView):
    template_name='index.html'

class SignupView(View) :
    def get(self, request, *args, **kwargs) :
        return render(request, 'signup.html')

    def post(self, request, *args, **kwargs) :
        signup_dto = self._build_signup_dtd(request.POST)
        result = UserService.signup(signup_dto)

        auth.login(request, result['user'])
        return redirect('index')

    @staticmethod
    def _build_signup_dtd(post_data) :
        return SignupDto (
            userid=post_data['userid'],
            password=post_data['password'],
            password_check=post_data['password_check'],
            name=post_data['name'],
            introduce=post_data['introduce'],
            address=post_data['address']
        )
