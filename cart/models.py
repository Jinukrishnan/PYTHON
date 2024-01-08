from django.db import models
from newapp.models import Product
# Create your models here.
class Cart(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    active=models.BooleanField(default=True)
    user_id=models.IntegerField()

    class Meta:
        db_table='Cart'
    def sub_total(self):
        return self.product.price*self.quantity
def __str__(self):
    return self.product
