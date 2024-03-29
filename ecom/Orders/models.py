from django.db import models
from Customers.models import Customer
from Products.models import Products
# Create your models here.
class Order(models.Model):
    LIVE=1
    DELETE=0
    DELETE_CHOICES=((LIVE,'Live'),(DELETE,'Delete'))
    owner=models.ForeignKey(Customer,on_delete=models.SET_NULL,related_name='ordrs',null=True)
    CART_STAGE=0
    ORDER_CONFIRMED=1
    ORDER_REJECTED=4
    ORDER_PROCESSED=2
    ORDER_DELIVERED=3
    STATUS_CHOICES=(
                    (ORDER_CONFIRMED,'ORDER_CONFIRMED'),
                    (ORDER_REJECTED,'ORDER_REJECTED'),
                    (ORDER_PROCESSED,'ORDER_PROCESSED'),
                    (ORDER_DELIVERED,'ORDER_DELIVERED')
                    
                    )
    order_status=models.IntegerField(choices=STATUS_CHOICES,default=CART_STAGE)
    delete_status=models.IntegerField(choices=DELETE_CHOICES,default=LIVE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
class OrderItem(models.Model):
    product=models.ForeignKey(Products,on_delete=models.SET_NULL,related_name='added_carts',null=True)
    quantity=models.IntegerField(default=1)
    owner=models.ForeignKey(Order,on_delete=models.CASCADE,related_name='added_items')
