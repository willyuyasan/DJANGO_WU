from django.contrib import admin
from .models import Task

#Class to define the only read field for a table
class TaskAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)

# Register your models here.
admin.site.register(Task, TaskAdmin) #Adds models to the admin pannel
