from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('', views.YordamList.as_view()),
    path('lang/<str:language>', views.YordamLanguage.as_view()),
    path('<int:pk>', views.YordamDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)