from django.db import models
import datetime


# Create your models here.
class Team(models.Model):

    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return 'Team'


class Milestone(models.Model):

    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    due_date = models.DateField(default=datetime.date.today)
    completion_status = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return 'Milestone'


class TeamMember(models.Model):

    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    milestone = models.ForeignKey(Milestone, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    function = models.CharField(max_length=500, null=True)
    description = models.CharField(max_length=500, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return 'Team member'


class Roles(models.Model):

    team_member = models.ForeignKey(TeamMember, on_delete=models.CASCADE)
    is_leader = models.BooleanField(default=False)
    is_member = models.BooleanField(default=False)
    
    def __str__(self):
        return 'Roles'