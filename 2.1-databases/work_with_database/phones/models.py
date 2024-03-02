from django.db import models
from django.template.defaultfilters import slugify


class Phone(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=250)
    price = models.CharField(max_length=250)
    image = models.CharField(max_length=250)
    release_date = models.CharField(max_length=250)
    lte_exists = models.CharField(max_length=250)
    slug = models.SlugField(blank=True, unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
