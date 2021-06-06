from django.urls import path
from userinfo.views import SignupView, LoginView

app_name = 'userinfo'

urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('signup/', SignupView.as_view(), name='signup'),

]
