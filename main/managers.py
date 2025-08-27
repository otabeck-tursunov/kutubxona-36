from django.db import models


class TirikManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(tirik=True)