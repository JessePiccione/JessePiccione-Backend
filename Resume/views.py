from django.shortcuts import redirect
from rest_framework import status, generics 

class Home(generics.GenericAPIView):
    def get(self, request):
        return redirect('/admin', True)