from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.DO_NOTHING)
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profilepics',blank=True)
    def __str__(self):
        return self.user.username