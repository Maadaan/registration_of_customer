from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=100 , null = True)
    phone = models.CharField(max_length= 25 , null = True)
    email = models.CharField(max_length=100 , null = True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    CATEGORY=(
            ('Indoor' , 'Indoor'),
            ('Outdoor' , 'Outdoor'),
            )
    name = models.CharField(max_length=100,null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=100,null=True,choices=CATEGORY)
    description = models.CharField(max_length=100,null=True)
    date_created= models.DateTimeField(auto_now_add=True,null=True)


# class Order(models.Model):
#         STATUS = (
#                 ('Pending' , 'Pending'),
#                 ('Out for delivery' , 'Out for delivery)',
#                 ('Delivered' , 'Delivered'),
#                 )

#         #Customer
#         #Product
#         date_created = models.DateTimeField(auto_now_add=True, null=True)
#         status = models.CharField(max_length=200, null=True, choices=STATUS)
class Order(models.Model):
    STATUS = (
            ('Pending', 'Pending'),
            ('Out for delivery', 'Out for delivery'),
            ('Delivered', 'Delivered'),
            )

    #customer =
    #product =
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
