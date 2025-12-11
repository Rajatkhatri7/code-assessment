from csvprocessor.models import Product
import pandas as pd
from django.core.management.base import BaseCommand
from django.db import connection




class Command(BaseCommand):
    help = 'Load dataset from CSV file'

    def handle(self, *args, **options):
        
        df = pd.read_csv('/Users/rajatkhatri/Documents/Django_code_project/djangoTutorial/csvprocessor/large_dataset.csv')

        df.dropna(inplace=True)
        df['stock'] = df['stock'].abs()
        df['price'] = df['price'].abs()
        df.drop(columns=['id', 'created_at'], inplace=True)
        records = df.to_dict(orient='records')
        
        connection.ensure_connection()
        Product.objects.bulk_create([Product(**record) for record in records])


    
        self.stdout.write(self.style.SUCCESS('Successfully loaded dataset'))
