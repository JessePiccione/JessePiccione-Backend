from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'main.html', {}, status=200)
def home(request):
    return render(request, 'home.html', {}, status=200)