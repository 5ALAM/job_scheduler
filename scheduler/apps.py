from django.apps import AppConfig

class SchedulerConfig(AppConfig):
    name = 'scheduler'

    def ready(self):
        from .tasks import start_job_thread
        start_job_thread()
