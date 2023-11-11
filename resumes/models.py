from django.db import models

# Create your models here.
class Profiles(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length = 50)
    tech = models.CharField(max_length=200)
    mobile = models.CharField(max_length=10)
    email = models.EmailField(default = None)
    photo = models.FileField()
    class Meta:
        db_table = 'Profiles'
