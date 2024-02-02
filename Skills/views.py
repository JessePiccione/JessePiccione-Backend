from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Skill, SkillCategory
# Create your views here.
class skill(View):
    def get(self, request):
        objects = Skill.objects.all()
        return HttpResponse(objects)
class skillCategory(View):
    def get(self, request):
        objects = SkillCategory.objects.all()
        return HttpResponse(objects)