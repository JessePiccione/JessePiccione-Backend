from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Award
# Create your views here.
class AwardHandler(View):
    def get(self, request):
        objects = Award.objects.all()
        context = {'objects':objects}
        return render(request, 'Awards.html', context)