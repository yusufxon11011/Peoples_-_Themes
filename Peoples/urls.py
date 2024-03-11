from django.urls import path
from . import views

urlpatterns = [
    path('', views.pupils_list, name='pupils_list'),
    path('<int:id>/', views.pupil_scores, name='pupil_scores'),
]