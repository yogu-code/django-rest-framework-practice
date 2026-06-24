from django.urls import path
from .views import product , product_pk

urlpatterns = [
    path("", product, name="product"),
    path("<int:pk>/", product_pk, name="product_pk")
]
