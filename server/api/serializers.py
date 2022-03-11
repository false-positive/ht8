from rest_framework import serializers


from api.models import User, Team, Project, Milestone, Task
from files.models import File


class UserSerializer(serializers.ModelSerializer):
    teams = serializers.StringRelatedField(source='team_set',many=True)
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'teams', 'uuid']


class TeamSerializer(serializers.ModelSerializer):
    members =  serializers.StringRelatedField(many=True)
    projects = serializers.StringRelatedField(source='project_set', many=True)
    class Meta:
        model = Team
        fields = ['name', 'description', 'projects', 'members', 'id']


class MilestoneSerializer(serializers.ModelSerializer):
    tasks = serializers.StringRelatedField(source='task_set', many=True)
    class Meta:
        model = Milestone
        fields = ['name', 'description', 'tasks']
        depth = 1


class ProjectSerializer(serializers.ModelSerializer):
    teams = serializers.StringRelatedField()
    milestones = MilestoneSerializer(source='milestone_set', many=True, read_only=True)
    class Meta:
        model = Project
        fields = ['name', 'team', 'description', 'milestones', 'id']
        depth = 1


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['name', 'description']
