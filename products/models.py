from django.db import models
from base.models import BaseModel





class category(BaseModel):
    category_name = models.CharField(max_length=100)
    category_image = models.ImageField(upload = "categories")


class product(BaseModel):
    product_name = models.CharField(max_length=100)
    category = models.ForeignKey(category , on_delete=models.CASCADE , related_name="products")
    price = models.IntegerField()
    