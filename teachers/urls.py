from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('', views.TeacherList.as_view()),
    path('lang/<str:language>', views.TeacherLanguage.as_view()),
    path('<int:pk>', views.TeacherDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)