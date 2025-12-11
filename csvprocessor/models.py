from django.db import models

# Create your models here.


#product model to keep csv entres
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    stock = models.IntegerField()
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)

    __table__ = 'products'

    class Meta:
        db_table = 'products'
        indexes = [
            models.Index(fields=['category']),
            models.Index(fields=['price']),
        ]