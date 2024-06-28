from django.db import models

# Create your models here.
from django.db import models
from ckeditor.fields import RichTextField
from image_cropping import ImageRatioField


class Page(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextField()
    header_image = models.ImageField(upload_to='headers/')
    cropping = ImageRatioField('header_image', '1920x1080')

    def __str__(self):
        return self.title
