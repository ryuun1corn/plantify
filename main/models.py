import uuid

from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class TropicalPlant(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    weight = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def is_expensive(self):
        return self.price > 100
