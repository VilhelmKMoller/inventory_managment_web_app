from django.db import models

class Cage1OnTop(models.Model):
    checked = models.BooleanField(default=False)
    vessel_type = models.CharField(max_length=255)
    item_category = models.CharField(max_length=255)
    item_full_name = models.TextField()
    conversion = models.CharField(max_length=255, blank=True)
    comment = models.TextField(blank=True)

# Similarly, define other models for "Cage 1 Shelf 1", "Cage 1 Shelf 2", etc.
