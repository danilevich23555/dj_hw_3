import csv

from django.core.management.base import BaseCommand
from phones.models import Phone
import os
from pathlib import Path
path = os.path.join(Path(__file__).parents[3], 'phones.csv')

class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open(path, 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
            print(phone)
            ph = Phone(id=phone['id'], name=phone['name'], price=phone['price'],
                       image=phone['image'], release_date=phone['release_date'],
                       lte_exists=phone['lte_exists'])
            ph.save()
