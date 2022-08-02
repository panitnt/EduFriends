from django.urls import path, include
from edu_sheet import views

urlpatterns = [
    path('', views.sheet, name='sheet'),
    path('<int:sheet_id>/', views.details, name='details'),
    path('share/', views.share, name='share'),
]