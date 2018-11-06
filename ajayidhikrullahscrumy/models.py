from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ScrumyGoals(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='ajayidhikrullahscrumy', default='')
    goal_name = models.CharField(max_length=200)
    goal_id = models.CharField(max_length=100)
    created_by = models.CharField(max_length=200)
    moved_by = models.CharField(max_length=200)
    owner = models.CharField(max_length=200)

class ScrumyHistory(models.Model):
    Scrumygoals = models.ForeignKey(ScrumyGoals, on_delete=models.PROTECT)
    moved_by = models.CharField(max_length=200)
    created_by = models.CharField(max_length=200)
    moved_from = models.CharField(max_length=200)
    moved_to = models.CharField(max_length=200)
    time_of_action = models.TimeField(auto_now=True)

class GoalStatus(models.Model):
    #Scrumygoals = models.ForeignKey(ScrumyGoals, on_delete=models.PROTECT)
    status_name = models.CharField(max_length=200)
