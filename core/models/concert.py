from django.db import models

from .mixins import ModifiedByMixin


class Concert(ModifiedByMixin):

    date = models.DateField(blank=False, null=False)
    hall = models.ForeignKey('Hall', on_delete=models.CASCADE)
    base_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=False,
        null=False,
    )

    class Meta:
        db_table = 'concert'
        verbose_name = 'Concert'
        verbose_name_plural = 'Concert'

