from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        #fields = ('id', 'title', 'description','done') #serialize selected field
        fields = '__all__' #serialize all the fields