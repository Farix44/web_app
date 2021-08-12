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
from kredyty.views import UserViewSet, LoansViewSet
from kredyty import urls
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)   # rejestrujemy url
# router.register(r'loans', LoansViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('kredyty/', include('kredyty.urls')),
    path('login/', auth_views.LoginView.as_view(), name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    path('kredyty/', include(urls)),
    path('api-token-auth/', obtain_auth_token),
    path('', include(router.urls)), # '' bedzie wypelnione tym co jest wyzej w router.register
]
