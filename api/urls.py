from django.urls import path, include
from .views import ProductViewSet
from rest_framework import routers

route = routers.DefaultRouter()
route.register("", ProductViewSet)


# urlpatterns = [
#     path("", ProductDetailsNCreate.as_view(), name="product"),
#     # path("create/", ProductCreate.as_view(), name="product-create"),
#     # path("<int:pk>/", ProductPkGet.as_view(), name="product_pk"),
#     # path("order/", OrderGet.as_view(), name="order"),
#     # path("user-order/", UserOrder.as_view(), name="user-order"),
# ]

urlpatterns = [path("", include(route.urls))]
