# Generated by Django 3.2.13 on 2022-06-07 19:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pengeluaran_barang', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pengeluaranbarangdetail',
            options={'verbose_name_plural': 'Detail Pengeluaran Barang'},
        ),
        migrations.AlterModelOptions(
            name='pengeluaranbarangheader',
            options={'verbose_name_plural': 'Pengeluaran Barang'},
        ),
    ]
