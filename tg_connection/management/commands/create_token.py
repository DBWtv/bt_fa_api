import secrets
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Create token for telegram chat'

    def handle(self, *args, **options):
        token = secrets.token_hex(32)
        print(token)