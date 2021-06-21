from django.http import HttpResponse, Http404
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.views import View
from django.contrib import auth
from django.views import generic
from django.contrib.auth import login, logout
from django.core.serializers.json import DjangoJSONEncoder
from django.template.loader import render_to_string
from django.core.exceptions import PermissionDenied
from django.contrib import messages

import json

from .forms import RecoveryPwForm, CustomSetPasswordForm

from .helper import email_auth_num, send_mail

from userinfo.service import UserService
from userinfo.dto import SignupDto, LoginDto
# Create your views here.``

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

class LoginView(View) :
    def get(self, request, *args, **kwargs) :
        return render(request, 'index.html')

    def post(self, request, *args, **kwargs) :
        login_dto = self._build_login_dto(request.POST)
        result = UserService.login(login_dto)

        auth.login(request, result['user'])
        return redirect('social:user_list')

    @staticmethod
    def _build_login_dto(poas_data) :
        return LoginDto (
            userid=poas_data['userid'],
            password=poas_data['password']
        )

def logout(request) :
    auth.logout(request)
    return redirect('index')

# 비밀번호찾기 GET시 매핑
class RecoveryPwView(View):
    template_name = 'recovery_pw.html'
    recovery_pw = RecoveryPwForm

    def get(self, request):
        if request.method=='GET':
            form = self.recovery_pw(None)
            return render(request, self.template_name, { 'form':form, })

# 비밀번호찾기 창에서 필드 값들을 입력하고 Ajax요청을 하는 view
def ajax_find_pw_view(request):
    user_id = request.POST.get('user_id')
    name = request.POST.get('name')
    email = request.POST.get('email')
    target_user = User.objects.get(user_id=user_id, name=name, email=email)

    if target_user:
        auth_num = email_auth_num()
        target_user.auth = auth_num 
        target_user.save()

        send_mail(
            '비밀번호 찾기 인증메일입니다.',
            [email],
            html=render_to_string('userinfo:recovery_email.html', {
                'auth_num': auth_num,
            }),
        )
    return HttpResponse(json.dumps({"result": target_user.user_id}, cls=DjangoJSONEncoder), content_type = "application/json")

# 템플릿에서 입력된 인증번호 확인하는 view
def auth_confirm_view(request):
    user_id = request.POST.get('user_id')
    input_auth_num = request.POST.get('input_auth_num')
    target_user = User.objects.get(user_id=user_id, auth=input_auth_num)
    target_user.auth = ""
    target_user.save()
    request.session['auth'] = target_user.user_id  
    
    return HttpResponse(json.dumps({"result": target_user.user_id}, cls=DjangoJSONEncoder), content_type = "application/json")

def auth_pw_reset_view(request):
    if request.method == 'GET':
        if not request.session.get('auth', False):
            raise PermissionDenied

    if request.method == 'POST':
        session_user = request.session['auth']
        current_user = User.objects.get(user_id=session_user)
        login(request, current_user)

        reset_password_form = CustomSetPasswordForm(request.user, request.POST)
        
        if reset_password_form.is_valid():
            user = reset_password_form.save()
            messages.success(request, "비밀번호 변경완료! 변경된 비밀번호로 로그인하세요.")
            logout(request)
            return redirect('userinfo:login')
        else:
            logout(request)
            request.session['auth'] = session_user
    else:
        reset_password_form = CustomSetPasswordForm(request.user)

    return render(request, 'userinfo:password_reset.html', {'form':reset_password_form})