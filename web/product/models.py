from django.db import models

from warehouse.models import Warehouse


class Product(models.Model):
    ProductPK = models.BigAutoField(primary_key=True)
    ProductName = models.CharField(max_length=256)

    def __str__(self) -> str:
        return self.ProductName


class ProductStok(models.Model):
    ProductStokPK = models.BigAutoField(primary_key=True)
    WarehouseIDF = models.ForeignKey(Warehouse, on_delete=models.DO_NOTHING, verbose_name='ID Warehouse')
    ProductIDF = models.ForeignKey(Product, on_delete=models.DO_NOTHING, verbose_name='ID Produk')
    QtyDus = models.IntegerField(verbose_name='Quantity Dus')
    QtyPcs = models.IntegerField(verbose_name='Quantity Pcs')
