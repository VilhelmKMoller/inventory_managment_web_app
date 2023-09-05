# import_data.py
import psycopg2
# from inventory_management.inventory.models import InventoryItem
from django.conf import settings
from django.db import connection

# Connect to the PostgreSQL database
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

InventoryItem = settings.INSTALLED_APPS.import_string("inventory_management.inventory.models.InventoryItem")

for row in data:
    _, created = InventoryItem.objects.get_or_create(
        location=row[0],
        state=row[1],
        date_added=row[2],
        vessel_type=row[3],
        item_category=row[4],
        item_full_name=row[5],
        conversion=row[6],
        comment=row[7],
        check_out_date=row[8]
    )

cursor.close()
conn.close()