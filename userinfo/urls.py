from django.urls import path
from userinfo.views import SignupView, LoginView, UserDetailView, logout

app_name = 'userinfo'

urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('logout/', logout, name='logout'),
    path('mypage/<int:pk>', UserDetailView.as_view(), name='mypage'),
]
