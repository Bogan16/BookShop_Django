from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('submit_review/', views.homepage, name='submit_review')
]