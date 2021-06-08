from django.urls import path
from userinfo.views import SignupView, LoginView, UserDetailView, logout
from social import views


app_name = 'userinfo'

urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('logout/', logout, name='logout'),
    path('mypage/<int:pk>', UserDetailView.as_view(), name='mypage'),
    

    # path('article_list/', ArticleListView.as_view(), name='article_list'),
    # path('article_list/upload/', UploadArticleView.as_view(), name='upload_article'),

]
