from django.db.models import Model, URLField, TextField, ForeignKey, CASCADE
from django.conf import settings

# Create your models here.

class Link(Model):
    url = URLField()
    description = TextField(blank=True)
    posted_by = ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=CASCADE)
