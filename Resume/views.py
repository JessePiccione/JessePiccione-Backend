from django.shortcuts import render
from Message.forms import MessageForm
from django.views import View
from .models import HomePageEntry, Technology
# Create your views here.
class index(View):
    def get(self,request):
        f = MessageForm()
        return render(request, 'main.html', {'f':f}, status=200)
class home(View):
    def post(self,request):
        entries = HomePageEntry.objects.all()
        technologies = Technology.objects.all()
        return render(request, 'home.html', {'entries':entries,'technologies':technologies}, status=200)

    