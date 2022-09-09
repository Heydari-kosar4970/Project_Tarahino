from django.urls import path
from . import views

urlpatterns = [
    path('register', views.registration_page, name='registration_page'),
    path('login', views.login_page, name='login_page'),
    path('logout', views.logout_user, name='logout_user'),
]
