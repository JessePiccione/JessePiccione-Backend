from django.shortcuts import render
from django.views import View
from .models import Skill
# Create your views here.
class skillsHandler(View):
    def post(self, request):
        skills = Skill.objects.all()
        newcontext = {}
        for skill in skills:
            if newcontext.get(skill.category.category_name) is None:
                newcontext[skill.category.category_name] =[]
            newcontext[skill.category.category_name].append(skill)
            context = {'entries': newcontext}

        return render(request, 'skills.html', context, status=200)