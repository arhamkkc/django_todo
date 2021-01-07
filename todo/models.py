from django.db import models

# Create your models here.
class Todos(models.Model):
    task = models.CharField(max_length=40)
    created_date =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.task
    
