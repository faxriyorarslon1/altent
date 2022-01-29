from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import include, url
from rest_framework import permissions
from users.views import (CustomTokenObtainPairView, UsersRegisterView)
from rest_framework_simplejwt.views import TokenRefreshView
from django.conf import settings
from django.conf.urls.static import static
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
    path('api/v1/login/', CustomTokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('api/v1/refreshtoken/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/register/', UsersRegisterView.as_view(), name='register'),

    path('api/v1/yordam/', include('yordam.urls')),
    path('api/v1/teachers/', include('teachers.urls')),
    path('api/v1/pupils/', include('pupils.urls')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_header = 'Altent o\'quv markazi - boshqaruv'
admin.site.index_title = 'Ma\'lumotlar ro\'yxati'
admin.site.site_title = 'Altent Tizimi'