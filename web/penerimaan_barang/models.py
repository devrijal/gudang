from django.db import models
from warehouse.models import Warehouse
from supplier.models import Supplier
from product.models import Product, ProductStok


class PenerimaanBarangHeader(models.Model):
    TrxInPK = models.BigAutoField(primary_key=True)
    TrxInNo = models.CharField(max_length=12)
    WhsIDF = models.ForeignKey(Warehouse, on_delete=models.DO_NOTHING, verbose_name='ID Warehouse')
    TrxInDate = models.DateField(verbose_name='Tanggal Penerimaan Barang')
    TrxInSuppIDf = models.ForeignKey(Supplier, on_delete=models.DO_NOTHING, verbose_name='ID Supplier')
    TrxInNotes = models.CharField(max_length=256)

    class Meta:
        verbose_name_plural = "penerimaan barang"

    def __str__(self) -> str:
        return self.TrxInNo


class PenerimaanBarangDetail(models.Model):
    TrxInDPK = models.BigAutoField(primary_key=True, verbose_name='ID Detail Penerimaan Barang')
    TrxInIDF = models.ForeignKey(PenerimaanBarangHeader, on_delete=models.CASCADE, verbose_name='Penerimaan Barang Header ID')
    TrxInDProductIDF = models.ForeignKey(Product, on_delete=models.DO_NOTHING, verbose_name='ID Produk')
    TrxInDQtyDus = models.IntegerField(verbose_name='Quantity (Dus)')
    TrxInDQtyPcs = models.IntegerField(verbose_name='Quantity (Pcs)')

    class Meta:
        verbose_name_plural = "Detail Pengeluaran Barang"

    def save(self, *args, **kwargs):

        warehouse = self.TrxInIDF.WhsIDF
        
        try:
            stok = ProductStok.objects.get(WarehouseIDF=warehouse, ProductIDF=self.TrxInDProductIDF)
        except ProductStok.DoesNotExist:
            stok = None

        if self.pk is None:
            super().save(*args, **kwargs)

            if stok:
                stok.QtyDus += self.TrxInDQtyDus
                stok.QtyPcs += self.TrxInDQtyPcs
            else:
                stok = ProductStok(
                    WarehouseIDF=warehouse, 
                    ProductIDF=self.TrxInDProductIDF, 
                    QtyDus=self.TrxInDQtyDus,
                    QtyPcs=self.TrxInDQtyPcs
                )
            
            stok.save()
        else:
            prev_val = PenerimaanBarangDetail.objects.get(pk=self.pk)
            super().save(*args, **kwargs)

            if self.TrxInDQtyDus > prev_val.TrxInDQtyDus:
                differences = prev_val.TrxInDQtyDus - self.TrxInDQtyDus
                stok.QtyDus += differences
            elif self.TrxInDQtyDus < prev_val.TrxInDQtyDus:
                differences = prev_val.TrxInDQtyDus - self.TrxInDQtyDus
                stok.QtyDus -= differences

            if self.TrxInDQtyPcs > prev_val.TrxInDQtyPcs:
                differences = prev_val.TrxInDQtyPcs - self.TrxInDQtyPcs
                stok.QtyPcs += differences
            elif self.TrxInDQtyPcs < prev_val.TrxInDQtyPcs:
                differences = prev_val.TrxInDQtyPcs - self.TrxInDQtyPcs
                stok.QtyPcs -= differences

            stok.save()

    def __str__(self) -> str:
        return "%s - %s - [%s Dus, %s Pcs]" % (self.TrxInIDF.TrxInNo, self.TrxInDProductIDF.ProductName, self.TrxInDQtyDus, self.TrxInDQtyPcs)
