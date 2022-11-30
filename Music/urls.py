from django.urls import path
from . import views

urlpatterns = [
    path('', views.songsList),
    path('<int:pk>/', views.songsDetail)
]