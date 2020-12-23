"""travel_recommend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from travel import views
from recommend_app import views
from recommend_app import cal_knn

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', views.IndexFunc, name='home'),
    path('login', views.LoginFunc),
    path('logout', views.LogoutFunc),
    path('main', views.MainFunc, name='main'), 
    path('search', views.SearchFunction),
    path('detail', views.DetailFunction),
    path('signup', views.SignupFunction),
    path('signup2', views.SignupFunction2),
    path('cal_svd', recommend_app.views.Cal_Svd),
    path('cal_svd', recommend_app.cal_knn.Cal_Knn),
]
