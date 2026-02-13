import csv
from django.core.management.base import BaseCommand
from gameLibrary.models import Game
from datetime import datetime

class Command(BaseCommand):
    help = 'Imports game data from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Path to the csv file')

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']
        try:
            with open(file_path, mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    is_switch2_bool = row['is_switch_2'].lower() == 'true'
                    obj, created = Game.objects.get_or_create(
                        title=row['title'],
                        defaults={
                            'release_date': datetime.strptime(row['release_date'], '%m/%d/%Y'),
                            'genre': row['genre'],
                            'content_rating': row['content_rating'],
                            'is_switch_2': is_switch2_bool
                        }
                    )
                    if created:
                        self.stdout.write(self.style.SUCCESS(
                            f"Imported: {row['title']}"))
                    else:
                        self.stdout.write(self.style.WARNING(
                            f"Skipped: {row['title']}"))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Error: {e}"))
