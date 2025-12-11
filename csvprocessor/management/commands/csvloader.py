from csvprocessor.models import Product
import pandas as pd
from django.core.management.base import BaseCommand
from django.db import connection




class Command(BaseCommand):
    help = 'Load dataset from CSV file'

    def add_arguments(self, parser):
        parser.add_argument('--file_path', type=str, help='Path to the CSV file', required=True)


    def handle(self, *args, **options):
        
        file_path = options['file_path']
        df = pd.read_csv(file_path)

        df.dropna(inplace=True)
        df['stock'] = df['stock'].abs()
        df['price'] = df['price'].abs()
        df.drop(columns=['id', 'created_at'], inplace=True)
        records = df.to_dict(orient='records')
        
        connection.ensure_connection()
        Product.objects.bulk_create([Product(**record) for record in records])


    
        self.stdout.write(self.style.SUCCESS('Successfully loaded dataset'))
