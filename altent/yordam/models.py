from django.db import models

# Create your models here.

class Yordam(models.Model):
    text_uz = models.CharField(max_length=100)
    text_eng = models.CharField(max_length=100)
    text_ru = models.CharField(max_length=100)

    def __str__(self):
        return self.text_uz

    
