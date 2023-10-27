
import subprocess
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Run Uvicorn using a custom management command'

    def handle(self, *args, **options):
        uvicorn_command = [
            'uvicorn',
            'quickstart.asgi:application',  # Use your ASGI application path
            '--port', '8000',  # Adjust the port as needed
            '--reload'
        ]

        try:
            subprocess.run(uvicorn_command, check=True)
        except subprocess.CalledProcessError:
            self.stdout.write(self.style.ERROR('Uvicorn failed to start.'))
        else:
            self.stdout.write(self.style.SUCCESS('Uvicorn started successfully.'))
