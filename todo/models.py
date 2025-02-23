from django.db import models


class Task(models.Model):
    description = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True) # will show the time when the task was created. it never changes
    updated_at = models.DateTimeField(auto_now=True)    # will show the time when the task was updated . it changes every time the task is updated
    

    # return a human-readable representation of the model instance
    def __str__(self):
        return self.description

# Create your models here.
