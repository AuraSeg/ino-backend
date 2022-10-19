from django.forms import ValidationError
from rest_framework import serializers
from .models import Team, TeamMember, Milestone, Roles

class TeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = Team
        fields = [
            'id',
            'name',
            'description',
        ]
        extra_kwargs = {'id':{'read_only': True}}


class TeamMemberSerializer(serializers.ModelSerializer):

    class Meta:
        model = TeamMember
        fields = [
            'id',
            'team',
            'milestone',
            'name',
            'function',
            'description'
        ]
        extra_kwargs = {'id':{'read_only': True}}


class MilestoneSerializer(serializers.ModelSerializer):

    class Meta:
        model = Milestone
        fields = [
            'id',
            'team',
            'title',
            'description',
            'due_date',
            'completion_status'
        ]
        extra_kwargs = {'id':{'read_only': True}}


class RolesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Roles
        fields = [
            'team_member',
            'is_leader',
            'is_member',
        ]