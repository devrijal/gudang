from django.db import models

class Customer(models.Model):
    CustomerPK = models.AutoField(primary_key=True)
    CustomerName = models.CharField(max_length=128)

    def __str__(self) -> str:
        return self.CustomerName
