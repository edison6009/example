from django.core.management.base import BaseCommand
from core.models import Category

class Command(BaseCommand):
    help = 'Seed initial categories only if they do not exist'

    def handle(self, *args, **kwargs):
        seed_data = [
            {'name': 'Electronics', 'description': 'Devices and gadgets'},
            {'name': 'Books', 'description': 'Printed and digital books'},
            {'name': 'Clothing', 'description': 'Apparel and accessories'},
        ]

        for entry in seed_data:
            existing = Category.objects.filter(name=entry['name']).first()

            if existing:
                if existing.description == entry['description']:
                    self.stdout.write(self.style.WARNING(f'Category "{entry["name"]}" already exists with matching data'))
                else:
                    self.stdout.write(self.style.ERROR(f'Category "{entry["name"]}" exists but has mismatched fields'))
            else:
                Category.objects.create(**entry)
                self.stdout.write(self.style.SUCCESS(f'Created category: {entry["name"]}'))
