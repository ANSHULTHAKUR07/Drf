from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Tags(models.Model):
    tag_name = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.tag_name
    
    
    class Meta:
        verbose_name = 'tags'
        db_table = 'tags'

class Task(models.Model):
    statusChoices = (
        ('p', 'pending'),
        ('c', 'completed')
    )
    task_name = models.CharField(max_length=50, null=False)
    task_description = models.TextField(max_length=150)
    task_status = models.CharField(choices=statusChoices, max_length=1, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tag = models.ManyToManyField(Tags)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    
    def __str__(self):
        return self.task_name
    
    class Meta:
        verbose_name = 'task'
        db_table = 'task'



