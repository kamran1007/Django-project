"""loginsystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
  )




from django.contrib import admin
from django.urls import path,include


from loginapp import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('loginapp/',include('loginapp.urls'))
    path('',views.welcome,name='welcome'),
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
	path('dashboard',views.dashboard,name='dashboard'),
	path('delete<int:id>',views.user_delete,name='user_delete'),
	path('update<int:id>',views.update_data,name='update'),
	path('edit<int:id>',views.edit,name='edit'),
	path('logout',views.logout,name='logout'),
	path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
	
	


]
