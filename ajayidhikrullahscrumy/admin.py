from django.contrib import admin
from .models import scrumyGoals, scrumyHistory, goalStatus

# Register your models here.
admin.site.register(scrumyGoals)
admin.site.register(scrumyHistory)
admin.site.register(goalStatus)

