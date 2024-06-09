from django.db import models

from .mixins import ModifiedByMixin


class Chair(ModifiedByMixin):

    salon = models.ForeignKey('Hall', on_delete=models.CASCADE)
    chair_number = models.PositiveIntegerField()
    chair_row = models.PositiveIntegerField()
    extra_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
    )

    class Meta:
        db_table = 'chair'
        verbose_name = 'Chair'
        verbose_name_plural = 'Chair'

