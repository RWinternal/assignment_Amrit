from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    # price = models.FloatField()

    def __str__(self):
        return self.name

    def get_add_to_cart_url(self):
        return reverse("core:add-to-cart", kwargs={
            "pk": self.pk
        })


# Track quantity
class ItemQuantity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.item.name}"


class Cart(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    product = models.ManyToManyField(ItemQuantity)

    def __str__(self):
        return self.author.username
