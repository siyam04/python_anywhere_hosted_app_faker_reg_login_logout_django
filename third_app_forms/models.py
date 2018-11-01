from django.db import models


class User(models.Model):
    """ User Creating """
    username = models.CharField(max_length=10)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50, unique=True)
    verify_email = models.EmailField(max_length=50)

    class Meta:
        """ Customizing User Class """
        ordering = ['-id']

    def __str__(self):
        """ Shows the Object's Name """
        return self.username
