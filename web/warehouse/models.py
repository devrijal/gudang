from django.db import models


class Warehouse(models.Model):
    WhsPK = models.AutoField(primary_key=True)
    WhsName = models.CharField(max_length=8)

    def __str__(self) -> str:
        return self.WhsName
