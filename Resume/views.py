from django.shortcuts import render
from Message.forms import MessageForm
# Create your views here.
def index(request):
    f = MessageForm()
    return render(request, 'main.html', {'f':f}, status=200)
def home(request):
    return render(request, 'home.html', {}, status=200)