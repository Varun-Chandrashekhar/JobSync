from django.urls import path
from . import views
from django.contrib import admin
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('application/', views.application, name='application'),
    path('profile/', views.profile, name='profile'),
    path('token/', jwt_views.TokenObtainPairView.as_view(), name ='token_obtain_pair'),
     path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name ='token_refresh')
]
