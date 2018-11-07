from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# Here is the first model created with class, and its represnt d status of each goals
class GoalStatus(models.Model):
    status_name = models.CharField(max_length=200, default="")
    # this will show the real meaning of each objects i.e. retrieve

    def __str__(self):
        return self.status_name

# this is the Goals that will be achieved
class ScrumyGoals(models.Model):
    goal_status = models.ForeignKey (GoalStatus, on_delete=models.PROTECT, related_name="ajayidhikrullahscrumy")
    user = models.OneToOneField(User, on_delete=models.PROTECT, related_name='ajayidhikrullahscrumy', default='')
    goal_name = models.CharField(max_length=200)
    goal_id = models.CharField(max_length=100)
    created_by = models.CharField(max_length=200)
    moved_by = models.CharField(max_length=200)
    owner = models.CharField(max_length=200)
    # retrieves the name of each goal as called

    def __str__(self):
        return self.goal_name

class ScrumyHistory(models.Model):
    goals = models.ForeignKey(ScrumyGoals, on_delete=models.PROTECT, related_name="ajayidhikrullahscrumy")
    moved_by = models.CharField(max_length=200)
    created_by = models.CharField(max_length=200)
    moved_from = models.CharField(max_length=200)
    moved_to = models.CharField(max_length=200)
    time_of_action = models.CharField(max_length=100)

    def __str__(self):
        return self.created_by



