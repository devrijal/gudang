# Generated by Django 3.2.13 on 2022-06-07 18:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('supplier', '0001_initial'),
        ('product', '0001_initial'),
        ('warehouse', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PengeluaranBarangHeader',
            fields=[
                ('TrxOutPK', models.BigAutoField(primary_key=True, serialize=False)),
                ('TrxOutNo', models.CharField(max_length=12)),
                ('TrxOutDate', models.DateField(verbose_name='Tanggal Pengeluaran Barang')),
                ('TrxInNotes', models.CharField(max_length=256)),
                ('TrxOutSuppIDf', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='supplier.supplier', verbose_name='Supplier ID')),
                ('WhsIdf', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='warehouse.warehouse', verbose_name='ID Warehouse')),
            ],
        ),
        migrations.CreateModel(
            name='PengeluaranBarangDetail',
            fields=[
                ('TrxOutDPK', models.BigAutoField(primary_key=True, serialize=False, verbose_name='ID Detail Pengeluaran Barang')),
                ('TrxOutDQtyDus', models.IntegerField(verbose_name='Quantity (Dus)')),
                ('TrxOutDQtyPcs', models.IntegerField(verbose_name='Quantity (Pcs)')),
                ('TrxOutDProductIDF', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='product.product', verbose_name='ID Produk')),
                ('TrxOutIDF', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pengeluaran_barang.pengeluaranbarangheader', verbose_name='Pengeluaran Barang Header ID')),
            ],
        ),
    ]