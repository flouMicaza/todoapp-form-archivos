from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='home_page'),
    path('register', views.register_user, name='register_user'),
    path('login',views.login_user, name='login'),
    path('logout',views.logout_user, name='logout'),
] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)