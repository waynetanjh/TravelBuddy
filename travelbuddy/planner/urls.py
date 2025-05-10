from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.planner, name='create_route'),
]
