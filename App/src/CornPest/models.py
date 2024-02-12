from django.db import models

class UploadImage(models.Model):
    image_file = models.ImageField(upload_to='images/%Y/%m/%d')
