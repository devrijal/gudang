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
            name='PenerimaanBarangHeader',
            fields=[
                ('TrxInPK', models.BigAutoField(primary_key=True, serialize=False)),
                ('TrxInNo', models.CharField(max_length=12)),
                ('TrxInDate', models.DateField(verbose_name='Tanggal Penerimaan Barang')),
                ('TrxInNotes', models.CharField(max_length=256)),
                ('TrxInSuppIDf', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='supplier.supplier', verbose_name='ID Supplier')),
                ('WhsIdf', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='warehouse.warehouse', verbose_name='ID Warehouse')),
            ],
        ),
        migrations.CreateModel(
            name='PenerimaanBarangDetail',
            fields=[
                ('TrxInDPK', models.BigAutoField(primary_key=True, serialize=False, verbose_name='ID Detail Penerimaan Barang')),
                ('TrxInDQtyDus', models.IntegerField(verbose_name='Quantity (Dus)')),
                ('TrxInDQtyPcs', models.IntegerField(verbose_name='Quantity (Pcs)')),
                ('TrxInDProductIDF', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='product.product', verbose_name='ID Produk')),
                ('TrxInIDF', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='penerimaan_barang.penerimaanbarangheader', verbose_name='Penerimaan Barang Header ID')),
            ],
        ),
    ]
