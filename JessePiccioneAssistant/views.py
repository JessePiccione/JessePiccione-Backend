from django.http import JsonResponse
from rest_framework.views import APIView 
from openai import OpenAI
import asyncio
from asgiref.sync import sync_to_async
from datetime import datetime
from json import loads
from JessePiccione.settings import OPENAI_API_KEY
import os

# Create your views here.

class AssistantMessageView(APIView):
    async def post(self, request):
        client = OpenAI(api_key=OPENAI_API_KEY)
        body = loads(request.body.decode())

        thread = await sync_to_async(client.beta.threads.create)()

        await sync_to_async(client.beta.threads.messages.create)(
            thread_id=thread.id,
            role='user',
            content=body['message'],
        )

        run = await sync_to_async(client.beta.threads.runs.create)(
            thread_id=thread.id,
            assistant_id='asst_rmCtCELde6QoCP8Hac0Ai3nj',
        )

        run = await sync_to_async(client.beta.threads.runs.retrieve)(
            thread_id=thread.id,
            run_id=run.id
        )

        backoff = 0.5
        while run.status in ("in_progress", "queued"):
            await asyncio.sleep(backoff)
            backoff = min(backoff * 2, 8)
            run = await sync_to_async(client.beta.threads.runs.retrieve)(
                thread_id=thread.id,
                run_id=run.id
            )

        messages = await sync_to_async(client.beta.threads.messages.list)(
            thread_id=thread.id
        )

        context = {
            "message": messages.data[0].content[0].text.value,
            "time": str(datetime.now()),
        }

        return JsonResponse(context)