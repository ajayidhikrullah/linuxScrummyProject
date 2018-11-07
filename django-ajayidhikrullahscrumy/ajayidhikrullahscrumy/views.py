from django.shortcuts import render
#
# Create your views here
from django.http import HttpResponse
from .models import ScrumyGoals, GoalStatus

def goal_status(request):
    goal_status = GoalStatus.objects.all()
    return HttpResponse(goal_status)

def scrumy_goals(request):
    scrumy_goals = ScrumyGoals.objects.all()
    return HttpResponse(scrumy_goals)







def index(request):
     return HttpResponse('Hello World')



# def index(request):
#     Scrumy = ScrumyGoals.objects.all()
#     html = ''
#     for html in Scrumy:
#         url = "/ajayidhikrullahscrumy/"
#         html += '<a href="' + url + '">' + '</a><br>'
#     return HttpResponse(html)
