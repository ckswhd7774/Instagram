from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from userinfo.views import IndexTemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('social/', include('social.urls')),
    path('userinfo/', include('userinfo.urls')),
    path('', IndexTemplateView.as_view(), name='index')
    
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
