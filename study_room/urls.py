from django.urls import path, include
from study_room import views

urlpatterns = [
    path('', views.study_room, name='study_room'),
]