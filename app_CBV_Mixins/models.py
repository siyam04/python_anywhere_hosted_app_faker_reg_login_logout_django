from django.db import models
from django.urls import reverse


class School(models.Model):
    """Creating School"""
    name = models.CharField(max_length=256)
    principal = models.CharField(max_length=256)
    location = models.CharField(max_length=256)

    class Meta:
        """ Customizing School Class """
        ordering = ['id']
        # verbose_name_plural = 'Schools'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})


class Student(models.Model):
    """Creating Student"""
    name = models.CharField(max_length=256)
    age = models.PositiveIntegerField()
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='students')

    class Meta:
        """ Customizing School Class """
        ordering = ['id']

    def __str__(self):
        return self.name
