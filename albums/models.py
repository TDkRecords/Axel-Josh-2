from django.db import models

class canciones(models.Model):
    nombre = models.CharField(max_length=100)
    pista = models.FileField(upload_to='audio/', default='audio/default.mp3')
    date_singles = models.DateField()
    def __str__(self):
        return self.nombre

    class Meta:
        ordering = ['-date_singles']