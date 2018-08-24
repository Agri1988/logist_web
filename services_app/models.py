from django.db import models

# Create your models here.
from django.urls import reverse_lazy


class Service(models.Model):
    name = models.CharField(
        max_length=512,
        verbose_name='Наименование услуги'
    )
    unit = models.CharField(
        max_length=64,
        verbose_name='ед.измерения'
    )
    count = models.IntegerField(
        verbose_name='Количество'
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Цена'
    )
    cost_wo_vat = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Цена без НДС'
    )
    vat = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='НДС'
    )
    vat_value = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='сумма НДС'
    )
    cost_with_vat = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='сумма с НДС'
    )

    def get_absolute_url(self):
        return reverse_lazy('services_app:service_update', kwargs={'pk':self.pk})

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

    def __str__(self):
        return '{}'.format(self.name)