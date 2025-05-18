from rest_framework import serializers
from .models import Award, AwardCategory, Education, Message, Project, HomePageEntry, Technology, Skill, SkillCategory, WorkExperience
from .serializers import AwardCategorySerializer, SkillCategorySerializer, HomePageEntrySerializer
class AwardSerializer(serializers.ModelSerializer):
    category = AwardCategorySerializer(read_only=True)
    class Meta:
        model = Award 
        fields = '__all__'
class AwardCategorySerializer(serializers.ModelSerializer):
    awards = AwardSerializer(read_only=True, many=True)
    class Meta:
        model = AwardCategory
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
    category = SkillCategorySerializer(read_only=True)
    class Meta:
        model = Skill
        fields = '__all__'
class SkillCategorySerializer(serializers.ModelSerializer):
    skills = SkillSerializer(read_only=True, many=True)
    class Meta:
        model = SkillCategory 
        fields = '__all__'    
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'
class TechnologySerializer(serializers.ModelSerializer):
    pageEntry = HomePageEntrySerializer(read_only=True)
    class Meta:
        model = Technology
        fields = '__all__'
class HomePageEntrySerializer(serializers.ModelSerializer):
    technologies = TechnologySerializer(many=True, read_only=True)
    class Meta:
        model = HomePageEntry
        fields = '__all__'