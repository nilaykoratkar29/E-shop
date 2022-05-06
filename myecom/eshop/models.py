from django.db import models


# Create your models here.
class Products(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=200, default='')
    product_cat = models.CharField(max_length=50, default='')
    product_price = models.IntegerField(default='')
    desc = models.CharField(max_length=3000, default='')
    pro_date = models.DateField(default='')
    product_image = models.ImageField(upload_to='eshop/images', default='')

    def __str__(self):
        return self.product_name


class Orders(models.Model):
    orderid = models.AutoField
    ord_name = models.CharField(max_length=60, default='')
    ord_cat = models.CharField(max_length=50, default='')
    orderprice = models.IntegerField(default='')
    orderqty = models.IntegerField(default='')
    orderdate = models.DateField(default='')

    def __str__(self):
        return self.ord_name


class Contact(models.Model):
    name = models.CharField(max_length=50, default='')
    email = models.CharField(max_length=50, default='')
    phone = models.IntegerField(default=0)
    city = models.CharField(max_length=40, default='')
    state = models.CharField(max_length=40, default='')
    message = models.CharField(max_length=4000, default='')

    def __str__(self):
        return self.name
