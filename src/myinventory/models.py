import uuid
from django.db import models


class ItemModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    admin_description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="items", blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "image": self.image.url,
        }
