from django.urls import path
from . import views

urlpatterns = [
    path('jobs/', views.submit_job, name='submit_job'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
