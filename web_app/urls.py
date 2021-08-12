"""web_app URL Configuration

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
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

# REST_FRAMEWORK:
from rest_framework import routers
from kredyty.views import UserView, LoansView
from kredyty import urls

router = routers.DefaultRouter()
router.register(r'users', UserView)   # rejestrujemy url
# router.register(r'loans', LoansView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('kredyty/', include('kredyty.urls')),
    path('login/', auth_views.LoginView.as_view(), name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    path('kredyty/', include(urls)),
    path('', include(router.urls)), # '' bedzie wypelnione tym co jest wyzej w router.register
]
