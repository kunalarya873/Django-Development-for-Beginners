import uuid

from django.db import models


class Product(models.Model):
    IN_STOCK = "IS"
    OUT_OF_STOCK = "OOS"
    BACKORDERED = "BO"

    STOCK_STATUS = {
        IN_STOCK: "In Stock",
        OUT_OF_STOCK: "Out of stock",
        BACKORDERED: "Back Ordered",
    }

    pid = models.CharField(max_length=255)
    name = models.CharField(max_length=100, unique=True, help_text='Enter a category name.')
    slug = models.SlugField(unique=True, editable=False)
    description = models.TextField(null=True)
    is_digtial = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    is_active = models.BooleanField(default=False)
    stock_status = models.CharField(
        max_length=3,
        choices=STOCK_STATUS,
        default=OUT_OF_STOCK,
    )
    category = models.ForeignKey("Category", on_delete=models.SET_NULL, null=True)
    seasonal_event = models.ForeignKey(
        "SeasonalEvents", on_delete=models.SET_NULL, null=True
    )
    product_type = models.ManyToManyField("ProductType", related_name="product")


class ProductLine(models.Model):
    price = models.DecimalField(decimal_places=2, max_digits=10)
    sku = models.UUIDField(default=uuid.uuid4)
    stock_qty = models.IntegerField(default=0)
    is_active = models.BooleanField(default=False)
    order = models.IntegerField()
    weight = models.FloatField()
    image = models.ForeignKey("ProductImage", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, models.SET_NULL, null=True)
    attribute = models.ManyToManyField("AttributeValue", related_name="productline")


class ProductImage(models.Model):
    name = models.CharField(max_length=100, unique=True)
    alternative_text = models.CharField(max_length=100)
    url = models.ImageField(unique=True)
    order = models.IntegerField()


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)
    is_active = models.BooleanField(default=False)
    parent = models.ForeignKey("self", on_delete=models.PROTECT, null=True)


class SeasonalEvents(models.Model):
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    name = models.CharField(max_length=100, unique=True)


class Attribute(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(null=True)
    is_active = models.BooleanField(default=False)


class ProductType(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    parent = models.ForeignKey("self", on_delete=models.PROTECT, null=True)


class AttributeValue(models.Model):
    id = models.BigAutoField(primary_key=True)
    attribute_value = models.CharField(max_length=100)
    attribute = models.ForeignKey("Attribute", on_delete=models.CASCADE, null=True)


class ProductLine_AttributeValue(models.Model):
    attribute_value = models.ForeignKey(
        "AttributeValue", on_delete=models.CASCADE, null=True
    )
    product_type = models.ForeignKey("ProductType", on_delete=models.CASCADE, null=True)


class Product_ProductType(models.Model):
    product = models.ForeignKey("Product", on_delete=models.CASCADE, null=True)
    product_type = models.ForeignKey("ProductType", on_delete=models.CASCADE, null=True)


class StockControl(models.Model):
    stock_qty = models.IntegerField()
    name = models.CharField(max_length=100)
    stock_product = models.OneToOneField(Product, models.CASCADE, null=True)
