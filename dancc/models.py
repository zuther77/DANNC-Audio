from django.db import models

# Create your models here.

class Upload(models.Model):
    audio = models.FileField(upload_to='audio')
    video = models.FileField(upload_to='video')

    def __str__(self):
        return str(self.pk)
