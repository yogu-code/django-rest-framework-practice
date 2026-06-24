from django.urls import path
from .views import product , product_pk , orders

urlpatterns = [
    path("", product, name="product"),
    path("<int:pk>/", product_pk, name="product_pk"),
    path("order/", orders, name="order")
]
