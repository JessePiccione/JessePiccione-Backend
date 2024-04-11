from django.shortcuts import render
from django.contrib.auth.models import Group
from rest_framework import generics
from .serializers import *
from .permissions import IsAdminUser
from rest_framework.permissions import IsAuthenticated
# Create your views here.
class AwardListView(generics.ListAPIView):
    queryset = Award.objects.all()
    serializer_class = AwardSerializer
class AwardDetailsView(generics.RetrieveAPIView):
    queryset = Award.objects.all()
    serializer_class = AwardSerializer

class EducationListView(generics.ListAPIView):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer
class EducationDetailsView(generics.RetrieveAPIView):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer

class WorkExperienceListView(generics.ListAPIView):
    queryset = WorkExperience.objects.all()
    serializer_class = WorkExperienceSerializer
class WorkExperienceDetailsView(generics.RetrieveAPIView):
    queryset = WorkExperience.objects.all()
    serializer_class = WorkExperienceSerializer

class MessageListView(generics.ListAPIView):
    queyset = Message.objects.all()
    serialzier_class = MessageSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
class MessageCreateView(generics.CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
class MessageDetailsView(generics.RetrieveDestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes =[IsAuthenticated, IsAdminUser]

class SkillListView(generics.ListAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
class SkillDetailsView(generics.RetrieveAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    
class SkillCategoryListView(generics.ListAPIView):
    queryset = SkillCategory.objects.all()
    serializer_class = SkillCategorySerializer
class SkillCategoryDetailsView(generics.RetrieveAPIView):
    queryset = SkillCategory.objects.all()
    serializer_class = SkillCategorySerializer
    
class ProjectListView(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
class ProjectDetailsView(generics.RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    