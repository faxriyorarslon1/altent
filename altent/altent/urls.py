"""altent URL Configuration

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
from django.urls import path
from users.views import (CustomTokenObtainPairView, UsersRegisterView)
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/login/', CustomTokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('api/v1/refreshtoken/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/register/', UsersRegisterView.as_view(), name='register'),
]


admin.site.site_header = 'Altent o\'quv markazi - boshqaruv'
admin.site.index_title = 'Ma\'lumotlar ro\'yxati'
admin.site.site_title = 'Altent Tizimi'