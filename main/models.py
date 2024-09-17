from django.db import models


# Create your models here.
class TropicalPlant(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    weight = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def is_expensive(self):
        return self.price > 100

