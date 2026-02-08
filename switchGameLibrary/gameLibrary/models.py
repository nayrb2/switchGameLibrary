from django.db import models
from django.utils.text import slugify

# Create your models here.

class Game(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.DateField()
    genre = models.CharField(max_length=100)
    content_rating = models.CharField(max_length=5)
    is_switch_2 = models.BooleanField(default=False)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Game, self).save(*args, **kwargs)