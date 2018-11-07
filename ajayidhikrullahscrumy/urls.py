from django.urls import path
from . import views
# from django.urls import *



urlpatterns = [
    path('', views.index, name='index'),
    path("scrumy_goals/", views.scrumy_goals), #/ajayidhikrullah/my_task/
    path("goal_status/", views.goal_status), #/ajayidhikrullah/goal_status/

    # extension of urls in ur webpages i.e. www.ajayi/sikiru/adekunle etc
    #/ajayidhikrullahscrumy/move_goal/(int:goal_id)
    path('move_goal/<int:goals_id>/', views.move_goal, name='move_goal'),

]
