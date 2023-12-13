# import random
# import sched
# import time
# from celery import shared_task

# from call_center.models import Agent

# # global_scheduler = None

# @shared_task
# def agents_mood():
#     print('Запущен agents_mood')
#     # global global_scheduler
#     agents = Agent.objects.all()
#     for agent in agents:
#         agent.mood = random.choice(agent.MOOD_CHOICES)[0]
# # Момент с save в данном случае неэффективен, множественное обращение к БД
#         agent.save()
#     # time.sleep(3)
#     # return agents_mood()

#     # global_scheduler.enter(3, 1, agents_mood, ())

# # def start_scheduler():
# #     global global_scheduler
# #     global_scheduler = sched.scheduler(time.time, time.sleep)
# #     global_scheduler.enter(0, 1, agents_mood, ())

# #     # Запускаем глобальный планировщик
# #     global_scheduler.run()

# # agents_mood()
# agents_mood.delay()

import random

from call_center_backend.celery import app
from django.apps import apps

@app.task
def add(x, y):
    return x + y


@app.task
def agents_mood():
    model = apps.get_model(app_label='call_center', model_name='Agent')
    # from call_center.models import Agent
    agents = model.objects.all()
    for agent in agents:
        agent.mood = random.choice(agent.MOOD_CHOICES)[0]
        agent.save()
