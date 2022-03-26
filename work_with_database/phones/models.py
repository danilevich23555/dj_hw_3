from django.db import models
from django.utils.text import slugify

class Phone(models.Model):
        name = models.CharField(max_length=100)
        price = models.CharField(max_length=100)
        image = models.CharField(max_length=100)
        release_date = models.CharField(max_length=100)
        lte_exists = models.CharField(max_length=100)
        slug = models.SlugField()

        def save(self, *args, **kwargs):
                self.slug = slugify(self.name)
                super(Phone, self).save(*args, **kwargs)