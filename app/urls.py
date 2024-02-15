from django.urls import path

from app import views


urlpatterns = [
    path("", views.index),
    path("import", views.import_data),
    path("detail/<str:model_name>", views.detail),
    path("detail/<str:model_name>/<int:_id>", views.detail),
]
