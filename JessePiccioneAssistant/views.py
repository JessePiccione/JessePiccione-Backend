from django.http import JsonResponse
from rest_framework.views import APIView 
from openai import OpenAI
from time import sleep
from datetime import datetime
from json import loads
from JessePiccione.settings import OPENAI_API_KEY
import os

# Create your views here.

class AssistantMessageView(APIView):
    def post(self, request):
        client = OpenAI(api_key=OPENAI_API_KEY)
        body = loads(request.body.decode())
        thread=client.beta.threads.create()
        message=client.beta.threads.messages.create(
            thread_id=thread.id,
            role='user',
            content=body['message'],
        )
        run = client.beta.threads.runs.create(
            thread_id=thread.id,
            assistant_id='asst_rmCtCELde6QoCP8Hac0Ai3nj',
        )
        run = client.beta.threads.runs.retrieve(
            thread_id = thread.id,
            run_id=run.id
        )
        while run.status in ('in_progress', 'queued'):
            run = client.beta.threads.runs.retrieve(
                thread_id = thread.id,
                run_id = run.id
            )
            sleep(0.5)
        messages = client.beta.threads.messages.list(
            thread_id = thread.id
        )
        context = {}
        context['message'] = messages.data[0].content[0].text.value
        context['time'] = str(datetime.now())
        return JsonResponse(context)