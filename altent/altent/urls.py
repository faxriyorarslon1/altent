from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from users.views import (CustomTokenObtainPairView, UsersRegisterView)
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/login/', CustomTokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('api/v1/refreshtoken/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/register/', UsersRegisterView.as_view(), name='register'),

    path('api/v1/yordam/', include('yordam.urls')),
]


admin.site.site_header = 'Altent o\'quv markazi - boshqaruv'
admin.site.index_title = 'Ma\'lumotlar ro\'yxati'
admin.site.site_title = 'Altent Tizimi'