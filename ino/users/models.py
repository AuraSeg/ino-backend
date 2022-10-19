from django.db import models
from milestones.models import TeamMember

# Create your models here.

class UserModel(models.Model):
    team_member = models.OneToOneField(TeamMember, on_delete=models.CASCADE)
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=100)    

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return 'Team'