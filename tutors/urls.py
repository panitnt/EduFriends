from django.urls import path, include
from tutors import views

urlpatterns = [
    path('', views.tutors, name='tutors'),
    path('tobe/', views.tobetutors, name='tobetutors'),
]