from django.urls import path, include
from edu_sheet import views

urlpatterns = [
    path('', views.sheet, name='sheet'),
]