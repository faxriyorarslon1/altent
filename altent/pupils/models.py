from pyexpat import model
from django.db import models

# Create your models here.

class Pupil(models.Model):
    fullname = models.CharField(max_length=30)
    fullname_ru = models.CharField(max_length=30)
    role_uz = models.CharField(max_length=30)
    role_ru = models.CharField(max_length=30)
    role_eng = models.CharField(max_length=30)
    image = models.ImageField(upload_to="teachers-photo/")
    text_uz = models.CharField(max_length=100)
    text_eng = models.CharField(max_length=100)
    text_ru = models.CharField(max_length=100)

    def __str__(self):
        return self.fullname
