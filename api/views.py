from django.http import JsonResponse
from .serializer import ProductSerializer
from .models import Product
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(["GET"])
def product(request):
    product = Product.objects.all()
    serializer = ProductSerializer(product, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def product_pk(request, pk):
    product = Product.objects.get(id=pk)
    serializer = ProductSerializer(product)
    return Response(serializer.data)
