from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class scrumyGoals(models.Model):
    User = models.ForeignKey(User, on_delete=models.PROTECT, related_name='ajayidhikrullahscrumy')
    # goalStatus = models.ForeignKey(goalStatus, on_delete=models.PROTECT, related_name='ajayidhikrullahscrumy')
    goal_name = models.CharField(max_length=200)
    goal_id = models.CharField(max_length=100)
    created_by = models.CharField(max_length=200)
    moved_by = models.CharField(max_length=200)
    owner = models.CharField(max_length=200)

class scrumyHistory(models.Model):
    scrumyGoals = models.ForeignKey(scrumyGoals, on_delete=models.PROTECT)
    moved_by = models.CharField(max_length=200)
    created_by = models.CharField(max_length=200)
    moved_from = models.CharField(max_length=200)
    moved_to = models.CharField(max_length=200)
    time_of_action = models.TimeField(auto_now=True)

class goalStatus(models.Model):
    scrumyGoals = models.ForeignKey(scrumyGoals, on_delete=models.PROTECT)
    status_name = models.CharField(max_length=200)
