from django.core.management.base import BaseCommand
from inventory.models import InventoryItem
import psycopg2

class Command(BaseCommand):
    help = 'Imports data from PostgreSQL into the InventoryItem model'

    def handle(self, *args, **options):
        # Your import logic here
        conn = psycopg2.connect(
        dbname="test",
        user="postgres",
        password="vilhelm",
        host="localhost",
        port="5432",
        )
        
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM test_data")
        data = cursor.fetchall()
        
        for row in data:
            _, created = InventoryItem.objects.get_or_create(
                location=row[0],
                state=row[1],
                date_added=row[2],
                vessel_type=row[3],
                item_category=row[4],
                item_full_name=row[5],
                conversion=row[6],
                comment=row[7]
            )
        
        cursor.close()
        conn.close()
