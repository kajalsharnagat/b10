from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string
import random

class Command(BaseCommand):
    help = 'Create random users'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Indicates the number of users to be created')

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        for _ in range(total):
            s = get_random_string(random.randint(5, 9))
            User.objects.create_user(username= s, email= s.lower() + '@gmail.com', password='Python@123')
