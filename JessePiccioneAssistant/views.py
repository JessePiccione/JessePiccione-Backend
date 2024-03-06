from django.shortcuts import render
from django.http import JsonResponse
from django.views import View 
from openai import OpenAI
from .creds import *
from time import sleep
from datetime import datetime
from json import loads
# Create your views here.
client = OpenAI(api_key=OPENAI_API_KEY)
class AssistantMessageView(View):
    def post(self, request):
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
            sleep(1)
        messages = client.beta.threads.messages.list(
            thread_id = thread.id
        )
        context = {}
        context['message'] = messages.data[0].content[0].text.value
        context['time'] = str(datetime.now())
        return JsonResponse(context)