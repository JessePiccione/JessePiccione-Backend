from django.core.exceptions import ValidationError
from django.views import View

from Resume.views import index
from .forms import MessageForm


# Create your views here.
class MessageView(View):
    def post(self, request):
        f = MessageForm(request.POST)
        if(f.is_valid()):
            f.save()
            return index(request)
        raise ValidationError()
                