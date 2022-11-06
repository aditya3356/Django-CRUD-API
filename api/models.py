from django.db import models

ACTIVITY_TYPE = (("SALE", "Sale"), ("SERVICE", "Service"))


class Customer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=254, unique=True)

    def __str__(self) -> str:
        return self.email


class Product(models.Model):
    asin = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    quantity = models.PositiveIntegerField()
    price = models.PositiveIntegerField()

    def __str__(self) -> str:
        return self.asin


class Activity(models.Model):
    type = models.CharField(choices=ACTIVITY_TYPE, max_length=7)
    customer_id = models.ForeignKey(Customer, on_delete=models.RESTRICT)
    product_id = models.ForeignKey(Product, on_delete=models.RESTRICT)
    date = models.DateField()
    amount = models.PositiveIntegerField()
