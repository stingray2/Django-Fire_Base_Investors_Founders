from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    bio = models.TextField(blank=True)
    profile_img = models.ImageField(upload_to='profile_image')
    loaction = models.CharField(max_length=250,blank=True)
    def __str__(self):
        return self.user.username
