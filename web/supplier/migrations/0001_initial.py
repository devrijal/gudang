# Generated by Django 3.2.13 on 2022-06-07 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('SupplierPK', models.AutoField(primary_key=True, serialize=False)),
                ('SupplierName', models.CharField(max_length=128)),
            ],
        ),
    ]