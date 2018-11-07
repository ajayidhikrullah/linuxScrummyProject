from django.urls import path, include
from . import views
from django.urls import *
urlpatterns = [
    path('', views.index, name='index'),
    path("scrumy_goals/", views.scrumy_goals),
    path("goal_status/", views.goal_status),
]
