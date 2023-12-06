from celery import shared_task

import random

from call_center.models import Agent

@shared_task
def agents_mood():
    agents = Agent.objects.all()
    for agent in agents:
        agent.mood = random.choice(agent.MOOD_CHOICES)[0]
        agent.save()

agents_mood()