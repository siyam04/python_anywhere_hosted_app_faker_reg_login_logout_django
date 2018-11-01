from django.db import models


class Topic(models.Model):
    """ Topic Creating """
    top_name = models.CharField(max_length=264, unique=True)

    class Meta:
        """ Customizing Topic Class """
        ordering = ['-id']  # Shows the Objects in Descending Order
        # verbose_name_plural = 'Topics'

    def __str__(self):
        """ Shows the Object's Name """
        return self.top_name


class WebPage(models.Model):
    """ Information """
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    name = models.CharField(max_length=264, unique=True)
    url = models.URLField(unique=True)

    class Meta:
        """ Customizing Topic Class """
        ordering = ['-id']

    def __str__(self):
        """ Shows the Object's Name """
        return self.name


class AccessRecord(models.Model):
    """ Records """
    name = models.ForeignKey(WebPage, on_delete=models.CASCADE)
    date = models.DateField()

    class Meta:
        """ Customizing Topic Class """
        ordering = ['-id']

    def __str__(self):
        """ Shows the Object's Name using TypeCast from Numbers to String """
        return str(self.date)

