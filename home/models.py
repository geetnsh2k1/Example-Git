from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Response(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.TextField(blank=False, null=False)
    contact = models.IntegerField()
    sent = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    category = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
    
class Like(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    user = models.ManyToManyField(User, related_name='user', blank=True)
    count = models.IntegerField(default=0)

    def __str__(self):
        string = str(self.product.name) + "-" + str(self.count)
        return string