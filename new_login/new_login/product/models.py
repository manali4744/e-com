from django.db import models
from app.models import User, Customer
from django.core.validators import RegexValidator
# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=250, null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=250, null=True)
    subcategory = models.CharField(max_length=255, null=True)
    category_brand = models.CharField(max_length=255, null=True)
    description = models.CharField(max_length=250, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    total_sales = models.IntegerField(null=True, default=400, blank=True)
    update_at = models.DateTimeField(auto_now=True)
    product_img = models.ImageField(null= True, blank= True)

    def __str__(self):
        return str(self.name)

    class Meta:
        unique_together = [['name', 'price', 'category']]

class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Out of delivery', 'Out of delivery'),
        ('Delivered', 'Delivered'),
    )
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=250, null=True, choices=STATUS, default='Pending')
    quantity = models.SmallIntegerField(default=1)

    def __str__(self):
        return str(self.product.name)
    
class Cart(models.Model):
    customer = models.OneToOneField(Customer, null=True, on_delete=models.SET_NULL)
    cart = models.ManyToManyField(Product)

    def __str__(self) -> str:
        return str(self.customer)
    


    

    