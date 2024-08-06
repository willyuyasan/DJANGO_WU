from django.forms import ModelForm
from .models import Task

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ('tittle', 'description','done') #serialize selected field
        #fields = '__all__' #serialize all the fields