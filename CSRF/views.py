from rest_framework import views
from django.http import JsonResponse
from django.middleware.csrf import get_token
from rest_framework.permissions import IsAuthenticated

class CSRFView(views.APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        return JsonResponse({'token':get_token(request)})