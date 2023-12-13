from django.apps import AppConfig
import os

class CallCenterConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'call_center'

    # def ready(self):
    #     if not os.environ.get("DJANGO_APP_INITIALIZED"):
    #         os.environ["DJANGO_APP_INITIALIZED"] = "True"
    #         from django.core.management import call_command
    #         call_command('startup_script')
