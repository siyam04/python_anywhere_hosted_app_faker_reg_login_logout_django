from django.db import models
from django.contrib.auth.models import User


class UserProfileInfo(models.Model):
    """ Creating User profile using built-in User class"""

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    portfolio_site = models.URLField(blank=True)
    # pip install pillow to use this
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    class Meta:
        """ Customizing UserProfileInfo Class """
        ordering = ['-id']

    def __str__(self):
        """ Shows the built-in User Name """
        return self.user.username



