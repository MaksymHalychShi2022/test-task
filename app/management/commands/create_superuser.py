from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

User = get_user_model()


class Command(BaseCommand):
    help = 'Creates a default superuser'

    def handle(self, *args, **options):
        if not User.objects.filter(username='admin').exists():
            # TODO: move to env vars
            User.objects.create_superuser('admin', 'admin@example.com', 'password')
            self.stdout.write(self.style.SUCCESS('Successfully created a new superuser'))
        else:
            self.stdout.write(self.style.WARNING('Superuser already exists.'))
