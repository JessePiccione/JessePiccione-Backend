from django.shortcuts import render
from Message.forms import MessageForm
from django.views import View
# Create your views here.
class index(View):
    def post(self,request):
        f = MessageForm()
        return render(request, 'main.html', {'f':f}, status=200)
class home(View):
    def post(self,request):
        return render(request, 'home.html', {}, status=200)

    