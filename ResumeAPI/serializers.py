from rest_framework import serializers
from Awards.models import Award
from Education.models import Education
from WorkExperience.models import WorkExperience
from Message.models import Message
from Skills.models import Skill, SkillCategory
from Projects.models import Project 
from django.contrib.auth.models import User

class AwardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Award 
        fields = '__all__'
class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = '__all__'
class WorkExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkExperience
        fields = '__all__'
class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__' 
class SkillSerializer(serializers.ModelSerializer):
    category = SkillCategory()
    class Meta:
        model = Skill
        fields = '__all__'
class SkillCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SkillCategory 
        fields = '__all__'
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'