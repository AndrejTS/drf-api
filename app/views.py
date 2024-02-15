import logging

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from app import models
from app import serializers


logger = logging.getLogger(__name__)


@api_view(["GET"])
def index(request):
    return Response("Server is running", status=status.HTTP_200_OK)


@api_view(["POST"])
def import_data(request):
    for item in request.data:
        try:
            model_name = list(item.keys())[0]
            model = getattr(models, model_name)
            serializer = getattr(serializers, f"{model_name}Serializer")

            data = item[model_name]

            try:
                instance = model.objects.get(id=data["id"])
                serializer_instance = serializer(instance, data=data)
            except model.DoesNotExist:
                serializer_instance = serializer(data=data)

            serializer_instance.is_valid()
            serializer_instance.save()

        except Exception as ex:
            logger.error(f"Error processing item: {item}. Error: {ex}")

    return Response(status=status.HTTP_201_CREATED)


@api_view(["GET"])
def detail(request, model_name, _id=None):
    model = getattr(models, model_name, None)
    if not model:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = getattr(serializers, f"{model_name}Serializer")

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
