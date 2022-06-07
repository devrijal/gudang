from django.db import models
from warehouse.models import Warehouse
from supplier.models import Supplier
from product.models import Product, ProductStok


class PengeluaranBarangHeader(models.Model):
    TrxOutPK = models.BigAutoField(primary_key=True)
    TrxOutNo = models.CharField(max_length=12)
    WhsIDF = models.ForeignKey(Warehouse, on_delete=models.CASCADE, verbose_name='ID Warehouse')
    TrxOutDate = models.DateField(verbose_name='Tanggal Pengeluaran Barang')
    TrxOutSuppIDF = models.ForeignKey(Supplier, on_delete=models.DO_NOTHING, verbose_name='Supplier ID')
    TrxOutNotes = models.CharField(max_length=256)

    class Meta:
        verbose_name_plural = "Pengeluaran Barang"


class PengeluaranBarangDetail(models.Model):
    TrxOutDPK = models.BigAutoField(primary_key=True, verbose_name='ID Detail Pengeluaran Barang')
    TrxOutIDF = models.ForeignKey(PengeluaranBarangHeader, on_delete=models.CASCADE, verbose_name='Pengeluaran Barang Header ID')
    TrxOutDProductIDF = models.ForeignKey(Product, on_delete=models.DO_NOTHING, verbose_name='ID Produk')
    TrxOutDQtyDus = models.IntegerField(verbose_name='Quantity (Dus)')
    TrxOutDQtyPcs = models.IntegerField(verbose_name='Quantity (Pcs)')

    class Meta:
        verbose_name_plural = "Detail Pengeluaran Barang"

    def save(self, *args, **kwargs):

        warehouse = self.TrxOutIDF.WhsIDF
        
        try:
            stok = ProductStok.objects.get(WarehouseIDF=warehouse, ProductIDF=self.TrxOutDProductIDF)
        except ProductStok.DoesNotExist:
            stok = None

        if self.pk is None:
            super().save(*args, **kwargs)

            if stok:
                stok.QtyDus -= self.TrxOutDQtyDus
                stok.QtyPcs -= self.TrxOutDQtyPcs
            
            stok.save()
        else:
            prev_val = PengeluaranBarangDetail.objects.get(pk=self.pk)
            super().save(*args, **kwargs)

            if self.TrxOutDQtyDus > prev_val.TrxOutDQtyDus:
                differences = prev_val.TrxOutDQtyDus - self.TrxOutDQtyDus
                stok.QtyDus -= differences
            elif self.TrxOutDQtyDus < prev_val.TrxOutDQtyDus:
                differences = prev_val.TrxOutDQtyDus - self.TrxOutDQtyDus
                stok.QtyDus += differences

            if self.TrxOutDQtyPcs > prev_val.TrxOutDQtyPcs:
                differences = prev_val.TrxOutDQtyPcs - self.TrxOutDQtyPcs
                stok.QtyPcs -= differences
            elif self.TrxOutDQtyPcs < prev_val.TrxOutDQtyPcs:
                differences = prev_val.TrxOutDQtyPcs - self.TrxOutDQtyPcs
                stok.QtyPcs += differences

            stok.save()
