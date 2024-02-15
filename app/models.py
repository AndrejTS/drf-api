from django.db import models


class AttributeValue(models.Model):
    id = models.IntegerField(primary_key=True)
    hodnota = models.CharField(max_length=255)


class AttributeName(models.Model):
    id = models.IntegerField(primary_key=True)
    nazev = models.CharField(max_length=255, null=True)
    zobrazit = models.BooleanField(null=True)


class Attribute(models.Model):
    id = models.IntegerField(primary_key=True)
    nazev_atributu_id = models.ForeignKey(AttributeName, on_delete=models.CASCADE)
    hodnota_atributu_id = models.ForeignKey(
        AttributeValue, on_delete=models.SET_NULL, null=True
    )


class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    nazev = models.CharField(max_length=255, null=True)
    description = models.TextField(null=True)
    cena = models.DecimalField(max_digits=10, decimal_places=2)
    mena = models.CharField(max_length=3, null=True)
    is_published = models.BooleanField(null=True)
    attributes = models.ManyToManyField(
        Attribute, through="ProductAttributes", related_name="products"
    )


class ProductAttributes(models.Model):
    id = models.IntegerField(primary_key=True)
    attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class Image(models.Model):
    id = models.IntegerField(primary_key=True)
    nazev = models.CharField(max_length=255, null=True)
    obrazek = models.URLField()


class ProductImage(models.Model):
    id = models.IntegerField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    obrazek_id = models.ForeignKey(Image, on_delete=models.CASCADE)
    nazev = models.CharField(max_length=255)


class Catalog(models.Model):
    id = models.IntegerField(primary_key=True)
    nazev = models.CharField(max_length=255, null=True)
    obrazek_id = models.ForeignKey(Image, on_delete=models.SET_NULL, null=True)

    # tady bych to udělal spíše pomocí ManyToManyField,
    # ale budu se držet zadání
    # products = models.ManyToManyField(Product)
    # attributes = models.ManyToManyField(Attribute)
    products_ids = models.JSONField(null=True)
    attributes_ids = models.JSONField(null=True)
