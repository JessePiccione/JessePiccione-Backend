from django.shortcuts import render
from django.http import HttpResponse
from .models import Education
from django.views import View
# Create your views here.
class education(View):
    def post(self, request):
        objects = Education.objects.all()
        context = {'objects':objects}
        return render(request,'education.html', context)