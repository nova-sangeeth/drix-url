from django.db import models

# Create your models here.
class short_urls(models.Model):
    short_url = models.CharField(max_length=20)
    long_url = models.URLField("URL", max_length=512)

    def __str__(self):
        return self.short_url

