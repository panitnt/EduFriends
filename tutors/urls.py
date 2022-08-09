from django.urls import path, include
from tutors import views

urlpatterns = [
    path('', views.tutors, name='tutors'),
    path('tobe/', views.tobetutors, name='tobetutors'),
    path('<int:tutor_id>', views.tutor_detail, name='tutor_detail'),
]