from django.db import models

class Vip(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='vip/images')
    files = models.FileField(upload_to='vip/files')
    instructions = models.FileField(upload_to='vip/instructions')
    date_vip = models.DateTimeField()
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date_vip']