from django.db import models

# Create your models here.
class Invester(models.Model):
    name = models.CharField(max_length=250)
    company_name = models.CharField(max_length=256)
    ceo_email = models.EmailField()
    ceo_phone = models.IntegerField()
    def __str__(self):
        return self.name