from django.shortcuts import render
#
# Create your views here
from django.http import HttpResponse
from .models import ScrumyGoals, GoalStatus

def goal_status(request):
    goal_status = GoalStatus.objects.all()
    return HttpResponse(goal_status)

# displays the urls in the webpage
def scrumy_goals(request):
    scrumy_goals = ScrumyGoals.objects.all()
    return HttpResponse(scrumy_goals)

# displays the urls in my webpage with the primarykey in d database
def move_goal(request, goals_id):
    move_goal = GoalStatus.objects.get(pk=goals_id)
    return HttpResponse(move_goal)
    # return HttpResponse("this is it %s." % move_goal)

# Task: Create a view named add_goal. For now all the view is required to do is create a new record on the ScrumyGoals table with the following details:
# goal_name = ‘Keep Learning Django’ ;
# goal_id = a randomly generated integer between 1000 and 9999;
# created_by = ‘Louis’;
# moved_by = ‘Louis’;
# owner = ‘Louis’;
# goal_status = a Weekly goal instance of the GoalStatus model;
# user = an instance of the User model (Louis Oma);



























def index(request):
     return HttpResponse('Hello World')



# def index(request):
#     Scrumy = ScrumyGoals.objects.all()
#     html = ''
#     for html in Scrumy:
#         url = "/ajayidhikrullahscrumy/"
#         html += '<a href="' + url + '">' + '</a><br>'
#     return HttpResponse(html)
