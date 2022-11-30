from django.urls import path
from . import views

urlpatterns = [
    path('', views.songList),
    path('<int:pk>/', views.songDetail)
]