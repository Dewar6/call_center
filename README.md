# call_center

### Celery

При реализации Celery стоит учитывать, что после версии 4.0 Celery перестал
адекватно отрабатывать из коробки под виндой (информация найдена на 
https://stackoverflow.com/questions/62524908/task-receive-but-doesnt-excute). 
Один из вариантов фикса данной проблемы - установка библиотеки gevent и 
запуск Celery с дополнительными ключами:
```
celery -A <proj_name> worker -l info -P gevent
```
Удобное отслеживание работы Celery может осуществляться посредством веб
интерфейса flower
```
https://docs.celeryq.dev/en/stable/userguide/monitoring.html#flower-real-time-celery-web-monitor
```

### Celery и Django

Если в таске Celery необходимо манипулировать моделями Django, их вначале
требуется правильным образом импортировать. Пример правильного импорта:

```
# core/tasks.py

from celery.decorators import task
from django.apps import apps

@task(name="celery_test_task") 
def celery_test_task():
    # call apps via Django
    model = apps.get_model(app_label='users', model_name='CustomUser')
    # Now models is accessible, such as model.objects.get_or_create()
```

Почитать подробнее про get_models() можно в документации
```
https://docs.djangoproject.com/en/2.2/ref/applications/#django.apps.AppConfig.get_models
```