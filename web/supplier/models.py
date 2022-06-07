from django.db import models

class Supplier(models.Model):
    SupplierPK = models.AutoField(primary_key=True)
    SupplierName = models.CharField(max_length=128)

    def __str__(self) -> str:
        return self.SupplierName