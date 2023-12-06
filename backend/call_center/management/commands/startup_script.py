from django.core.management.base import BaseCommand
from call_center.task import agents_mood 

class Command(BaseCommand):
    help = 'Run startup script'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Запускаем наш МегаУберСкрипт'))
        agents_mood.delay()
        self.stdout.write(self.style.SUCCESS('Хаос настроений агентов активирован!'))
