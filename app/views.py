import logging

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from app import models
from app import serializers


logger = logging.getLogger(__name__)

CREATE_SERIALIZERS = {
    "AttributeValue": "AttributeValueSerializer",
    "AttributeName": "AttributeNameSerializer",
    "Attribute": "AttributeSerializer",
    "Product": "ProductSerializer",
    "ProductAttributes": "ProductAttributesSerializer",
    "Image": "ImageSerializer",
    "ProductImage": "ProductImageSerializer",
    "Catalog": "CatalogCreateSerializer",
}

RETRIEVE_SERIALIZERS = {
    "AttributeValue": "AttributeValueSerializer",
    "AttributeName": "AttributeNameSerializer",
    "Attribute": "AttributeSerializer",
    "Product": "ProductSerializer",
    "ProductAttributes": "ProductAttributesSerializer",
    "Image": "ImageSerializer",
    "ProductImage": "ProductImageSerializer",
    "Catalog": "CatalogRetrieveSerializer",
}

UPDATE_SERIALIZERS = {
    "AttributeValue": "AttributeValueSerializer",
    "AttributeName": "AttributeNameSerializer",
    "Attribute": "AttributeSerializer",
    "Product": "ProductSerializer",
    "ProductAttributes": "ProductAttributesSerializer",
    "Image": "ImageSerializer",
    "ProductImage": "ProductImageSerializer",
    "Catalog": "CatalogUpdateSerializer",
}


@api_view(["GET"])
def index(request):
    return Response("Server is running", status=status.HTTP_200_OK)


@api_view(["POST"])
def import_data(request):
    total_items_count = 0
    error_items_count = 0
    error_items = []

    serializer = serializers.ImportDataSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(
            {
                "message": "Invalid request data",
            },
            status=status.HTTP_400_BAD_REQUEST,
        )

    for item in request.data:
        total_items_count += 1
        try:
            model_name = list(item.keys())[0]
            model = getattr(models, model_name)

            data = item[model_name]

            try:
                instance = model.objects.get(id=data["id"])
                serializer = getattr(serializers, UPDATE_SERIALIZERS[model_name])
                serializer_instance = serializer(instance, data=data)
            except model.DoesNotExist:
                serializer = getattr(serializers, CREATE_SERIALIZERS[model_name])
                serializer_instance = serializer(data=data)

            serializer_instance.is_valid()
            serializer_instance.save()

        except Exception as ex:
            logger.exception(f"Error processing item: {item}. Error: {ex}")
            error_items_count += 1
            error_items.append(item)

    if not error_items:
        msg = "Import operation completed successfully"
    else:
        msg = "Import operation completed with partial success"

    return Response(
        {
            "message": msg,
            "total_items_count": total_items_count,
            "error_items_count": error_items_count,
            "error_items": error_items,
        },
        status=status.HTTP_200_OK,
    )


@api_view(["GET"])
def detail(request, model_name, _id=None):
    model = getattr(models, model_name, None)
    if not model:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = getattr(serializers, RETRIEVE_SERIALIZERS[model_name])

    if _id is None:
        queryset = model.objects.all()
        serializer = serializer(queryset, many=True)
    else:
        try:
            model_instance = model.objects.get(id=_id)
        except model.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = serializer(model_instance)

    return Response(serializer.data, status=status.HTTP_200_OK)
