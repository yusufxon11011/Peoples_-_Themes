from django.urls import path
from . import views

urlpatterns = [
    path('', views.weekdays_list, name='weekdays_list'),
    path('uz/', views.weekdays_uz_list, name='weekdays_uz_list'),
    path('en/', views.weekdays_en_list, name='weekdays_en_list'),
    path('ru/', views.weekdays_ru_list, name='weekdays_ru_list'),
]