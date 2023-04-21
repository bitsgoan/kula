from django.db import models

# Create your models here.

class ShortenURL(models.Model):
    uuid = models.CharField(max_length=7,null=True)
    full_url = models.URLField(max_length = 250)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.uuid)
