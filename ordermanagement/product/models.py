from django.db import models


class BaseModel(models.Model):
    """This model is used for every model in same fields"""
    is_active = models.BooleanField(default=True)
    is_delete = models.BooleanField(default=False)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(BaseModel):
    """This model is used for store category data"""
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "category"


class Product(BaseModel):
    """This model is used for store product details"""
    name = models.CharField(max_length=256)
    brand_name = models.CharField(max_length=256)
    price = models.IntegerField()
    stoke = models.SmallIntegerField()
    image = models.ImageField(upload_to='product_image/', max_length=1024)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "product"
