from django.db import models

from .mixins import ModifiedByMixin


class Hall(ModifiedByMixin):
    created_by = models.ForeignKey('authorize.User', on_delete=models.CASCADE)
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

