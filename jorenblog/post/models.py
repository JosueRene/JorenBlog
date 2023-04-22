from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Type(models.Model):
    name = models.CharField(max_length=255)
    
    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name
    

class Post(models.Model):
    type = models.ForeignKey(Type, related_name='posts', on_delete=models.CASCADE)
    title = models.CharField(max_length=500, null=False, blank=False)
    description = models.TextField(blank=False, null=False)
    created_by = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
