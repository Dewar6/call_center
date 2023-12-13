# # import threading

# # from django.core.management.base import BaseCommand
# # from call_center.tasks import agents_mood, start_scheduler

# # class Command(BaseCommand):
# #     help = 'Run startup script'

# #     def handle(self, *args, **options):
# #         self.stdout.write(self.style.SUCCESS('Запускаем наш МегаУберСкрипт'))
# # # agents_mood нужно использоваться с delay() если хотим отправить на
# # # выполнение в селери
# #         thread = threading.Thread(target=agents_mood)
# #         thread_2 = threading.Thread(target=start_scheduler)
# #         thread.start()
# #         thread_2.start()
# #         current_thread = threading.current_thread()
# #         self.stdout.write(
# #             self.style.SUCCESS(
# #                 f'Хаос настроений агентов активирован! Поток {current_thread.name}'
# #             )
# #         )


# from django.core.management.base import BaseCommand
# from call_center.tasks import agents_mood

# class Command(BaseCommand):
#     help = 'Run startup script'

#     def handle(self, *args, **options):
#         self.stdout.write(self.style.SUCCESS('Запускаем наш МегаУберСкрипт'))
#         agents_mood.delay()
#         self.stdout.write(
#             self.style.SUCCESS(
#                 f'Хаос настроений агентов активирован!'
#             )
#         )