import csv

from django.core.management.base import BaseCommand
from phones.models import Phone




class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('id', nargs='+', type=int)

    def handle(self, *args, **options):
        with open('phones.csv', 'r', encoding='utf-8') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
            Phone.objects.create(**phone)

