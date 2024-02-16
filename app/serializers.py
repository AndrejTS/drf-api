from rest_framework import serializers

from .models import (
    AttributeValue,
    AttributeName,
    Attribute,
    Product,
    ProductAttributes,
    Image,
    ProductImage,
    Catalog,
)


class AttributeValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttributeValue
        fields = "__all__"


class AttributeNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttributeName
        fields = "__all__"


class AttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attribute
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class ProductAttributesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductAttributes
        fields = "__all__"


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = "__all__"


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = "__all__"


class CatalogCreateSerializer(serializers.ModelSerializer):
    products_ids = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(), many=True, required=False
    )
    attributes_ids = serializers.PrimaryKeyRelatedField(
        queryset=Attribute.objects.all(), many=True, required=False
    )

    class Meta:
        model = Catalog
        fields = ("id", "nazev", "obrazek_id", "products_ids", "attributes_ids")

    def create(self, validated_data):
        products_ids = validated_data.pop("products_ids", [])
        attribute_ids = validated_data.pop("attributes_ids", [])
        catalog = Catalog.objects.create(**validated_data)
        catalog.products.set(products_ids)
        catalog.attributes.set(attribute_ids)
        return catalog


class CatalogRetrieveSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)
    attributes = AttributeSerializer(many=True, read_only=True)

    class Meta:
        model = Catalog
        fields = "__all__"


class CatalogUpdateSerializer(serializers.ModelSerializer):
    products_ids = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(), many=True, required=False
    )
    attributes_ids = serializers.PrimaryKeyRelatedField(
        queryset=Attribute.objects.all(), many=True, required=False
    )

    class Meta:
        model = Catalog
        fields = ("id", "nazev", "obrazek_id", "products_ids", "attributes_ids")

    def update(self, instance, validated_data):
        products_ids = validated_data.pop("products_ids", [])
        attribute_ids = validated_data.pop("attributes_ids", [])
        instance = super().update(instance, validated_data)
        instance.products.set(products_ids)
        instance.attributes.set(attribute_ids)
        return instance
