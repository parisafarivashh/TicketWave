from django.db import models

from .mixins import ModifiedByMixin


class Hall(ModifiedByMixin):

    title = models.CharField(
        max_length=128,
        unique=True,
        null=False,
        blank=False,
    )

    class Meta:
        db_table = 'hall'
        verbose_name = 'Hall'
        verbose_name_plural = 'Hall'

