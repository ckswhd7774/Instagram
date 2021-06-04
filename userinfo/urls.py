from django.urls import path
from userinfo.views import SignupView

app_name = 'userinfo'

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),

]
