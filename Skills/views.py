from django.shortcuts import render
from django.views import View
from .models import Skill, SkillCategory
# Create your views here.
class skillsHandler(View):
    def get(self, request):
        skills = Skill.objects.all()
        categories = SkillCategory.objects.all()
        context = {
            'skills': skills,
            'types': categories,
        }
        return render(request, 'skills.html', context, status=200)