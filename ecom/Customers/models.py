from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    LIVE=1
    DELETE=0
    DELETE_CHOICES=((LIVE,'Live'),(DELETE,'Delete'))
    name=models.CharField(max_length=200)
    phone=models.CharField(max_length=12)
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='customer_profile')
    address=models.TextField()
    image=models.ImageField(upload_to='media/')
    priority=models.IntegerField(default=0)
    delete_status=models.IntegerField(choices=DELETE_CHOICES,default=LIVE)
    created_date=models.DateTimeField(auto_now_add=True)
    updates_at=models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name
