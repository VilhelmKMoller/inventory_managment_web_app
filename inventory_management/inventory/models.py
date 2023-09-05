from django.db import models

# to connect with postgress
class InventoryItem(models.Model):
    location = models.CharField(max_length=100)
    state = models.BooleanField()
    date_added = models.DateField()
    vessel_type = models.CharField(max_length=100)
    item_category = models.CharField(max_length=100)
    item_full_name = models.CharField(max_length=200)
    conversion = models.CharField(max_length=100)
    comment = models.TextField()

    def __str__(self):
        return self.item_full_name