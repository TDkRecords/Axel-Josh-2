from django.db import models
from django.db.models.fields import CharField, URLField
from django.db.models.fields.files import ImageField

class Project(models.Model):
    title = CharField(max_length=100)
    description = CharField(max_length=250)
    image = ImageField(upload_to="portfolio/images/")
    url = URLField(blank=True)
    date_portfolio = models.DateField(null=True, blank=True)
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date_portfolio']