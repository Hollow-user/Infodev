from django.db import models
from django.shortcuts import reverse

class CommunicationDevice(models.Model):

    DEVICE_CHOICES = (
        ('siren', 'сирена'),
        ('loudspeaker', 'громкоговоритель')
    )
    device_type = models.CharField(
        choices=DEVICE_CHOICES, verbose_name='Устройство', max_length=50)
    address = models.TextField(max_length=150, verbose_name='Адрес')
    latitude = models.DecimalField(
        max_digits=9, decimal_places=6, verbose_name='Широта',
        null=True, blank=True)
    longitude = models.DecimalField(
        max_digits=9, decimal_places=6, verbose_name='Долгота',
        null=True, blank=True)
    radius = models.BigIntegerField(verbose_name='Радиус зоны звукопокрытия')
    active = models.BooleanField(
        verbose_name='Активность',
        default=False)

    class Meta:
        verbose_name = 'Устройство'
        verbose_name_plural = 'Устройства'
        ordering = ['id']

    def get_absolute_url(self):
        return reverse('device_url', kwargs={'id': self.id})

    def __str__(self):
        return str(self.device_type) + ' ID: ' + str(self.id)


