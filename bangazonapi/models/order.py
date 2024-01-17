from django.db import models

class Order(models.Model):
    order_name = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    completion_status = models.BooleanField(default=False)
    phone_number = models.IntegerField(default=1111111)
    email = models.CharField(max_length=50)
    order_type = models.CharField(max_length=50)
    payment_type = models.CharField(max_length=50)
    date = models.DateField(default='2000-01-01')
    user_id = models.IntegerField(default=0)
    tip = models.DecimalField(max_digits=5, decimal_places=2)
    order_total = models.DecimalField(max_digits=6, decimal_places=2)
    items = models.ManyToManyField('Item', through='OrderItem')
    
