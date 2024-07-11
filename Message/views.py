from django.core.exceptions import ValidationError
from django.views import View
#from twilio.rest import Client 
from django.http import HttpResponse
from django.shortcuts import render
from .forms import MessageForm
from rest_framework.views import APIView
#from .twiliocreds import *

# Create your views here
class MessageView(APIView):
    def get(self, request):
        return HttpResponse(MessageForm().as_table())
    def post(self, request):
        f = MessageForm(request.POST)
        print (request.POST)
        if(f.is_valid()):
            f.save()
            #client = Client(account_sid, auth_token)
            #message = client.messages.create(from_=from_number, 
            #                                body=f'''New Message from {request.POST['name']}\nEmail: {request.POST['email']}\nSubject: {request.POST['subject']}\nMessage:\n{request.POST['message']}''',
            #                                to=to_number)
            return HttpResponse(status=201)
        raise ValidationError()
                