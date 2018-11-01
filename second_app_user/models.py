from django.db import models


class User(models.Model):
    """ User Creating """
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.EmailField(max_length=254, unique=True)

    class Meta:
        """ Customizing User Class """
        ordering = ['-id']

    def __str__(self):
        """ Shows the Object's Name """
        return self.first_name + self.last_name
