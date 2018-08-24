from django.db import models

# Create your models here.
from django.urls import reverse_lazy


class Document(models.Model):
    number = models.CharField(
        max_length=64,
        verbose_name='Документ'
    )
    services = models.ManyToManyField(
        'services_app.Service',
        verbose_name='Услуги',
        blank=True,
        null=True,
    )
    partner = models.ForeignKey(
        'partners_app.Partner',
        on_delete=models.DO_NOTHING,
        verbose_name='Плательщик'
    )
    price_with_vat_value = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True,
        verbose_name='Сумма по документу'
    )
    price_with_vat_verbose = models.CharField(
        max_length=512,
        blank=True,
        null=True,
        verbose_name='сумма прописью'
    )
    price_wo_vat_value = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True,
        verbose_name='Сумма без НДС'
    )
    price_wo_vat_verbose = models.CharField(
        max_length=512,
        blank=True,
        null=True,
        verbose_name='сумма без НДС прописью'
    )
    vat_value = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True,
        verbose_name='Сумма НДС'
    )
    vat_verbose = models.CharField(
        max_length=512,
        blank=True,
        null=True,
        verbose_name='НДС прописью'
    )
    date = models.DateField(
        verbose_name='Дата'
    )

    def get_absolute_url(self):
        return reverse_lazy('documents_app:document_update', kwargs={'pk':self.pk})

    class Meta:
        verbose_name = 'Счет'
        verbose_name_plural = 'Счета'

    def __str__(self):
        return '{} {}'.format(self.number,  self.date)