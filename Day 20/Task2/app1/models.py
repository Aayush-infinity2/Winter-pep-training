from django.db import models

# Create your models here.
class Students(models.Model):
    name= models.CharField(max_length=200)
    age= models.IntegerField()
    course= models.CharField(max_length=200)

    def __str__(self):
        return self.name

