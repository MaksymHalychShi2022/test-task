from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission


class Command(BaseCommand):
    help = 'Set up default roles and permissions'

    def handle(self, *args, **options):
        # Define roles and their respective permissions
        roles_permissions = {
            'Admin': ['add_logentry', 'change_logentry', 'delete_logentry'],
            'Employee': ['change_logentry'],
            'Restaurant Manager': ['view_logentry'],
        }

        for role, perms in roles_permissions.items():
            group, created = Group.objects.get_or_create(name=role)
            for perm_codename in perms:
                perm = Permission.objects.get(codename=perm_codename)
                group.permissions.add(perm)

            self.stdout.write(self.style.SUCCESS(f'Successfully created/updated group for {role}'))
