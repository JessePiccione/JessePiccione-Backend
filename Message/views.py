from django.core.exceptions import ValidationError
from django.views import View
from twilio.rest import Client 

from Resume.views import index
from .forms import MessageForm
from .twiliocreds import *

# Create your views here.
class MessageView(View):
    def post(self, request):
        f = MessageForm(request.POST)
        if(f.is_valid()):
            f.save()
            client = Client(account_sid, auth_token)
            message = client.messages.create(from_='whatsapp:+18447953913', 
                                             body=f'''New Message from {request.POST['name']}\nEmail: {request.POST['email']}\nSubject: {request.POST['subject']}\nMessage:\n{request.POST['message']}''',
                                             to='whatsapp:+17329080037')
            return index(request)
        raise ValidationError()
                