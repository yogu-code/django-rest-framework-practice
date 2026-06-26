from .serializer import ProductSerializer, OrderItemSerializer, OrderSerializer
from .models import Product, Order, OrderItem
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import mixins
from rest_framework.viewsets import ViewSet , ModelViewSet , ReadOnlyModelViewSet
from django.shortcuts import get_object_or_404
from rest_framework.viewsets import GenericViewSet

# ----------------- API View ----------------------

# APIView allows you to create View by two way : classes and function

# APIView via class
# class ProductApi(APIView):
#     def get(self, request):
#         product = Product.objects.all()
#         serialize = ProductSerializer(product, many=True)
#         return Response(serialize.data)

#     def post(self, request):
#         serialize = ProductSerializer(data=request.data)

#         if serialize.is_valid():
#             serialize.save()
#             return Response(serialize.data, status=status.HTTP_201_CREATED)
#         return Response(serialize.error_messages, status=status.HTTP_400_BAD_REQUEST)


# APIView via function
# @api_view(["GET"])
# def productsDetail(request):
#     product = Product.objects.all()
#     serialize = ProductSerializer(product, many=True)
#     return Response(serialize.data)


# @api_view(["POST"])
# def productCreate(request):
#     serialize = ProductSerializer(data=request.data)

#     if serialize.is_valid():
#         serialize.save()
#         return Response(serialize.data, status=status.HTTP_201_CREATED)
#     return Response(serialize.error_messages, status=status.HTTP_400_BAD_REQUEST)


# ----------------- Generic View ----------------------


# generic view

# class ProductDetail(generics.ListAPIView):
#     model = Product
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

# class ProductCreate(generics.CreateAPIView):
#     model = Product
#     serializer_class = ProductSerializer


# same gneric classes but combine with mixins like ListAPIView + CreateAPIView = ListCreateAPIView

# class ProductDetailsNCreate(generics.ListCreateAPIView):
#     model = Product
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer


# same as above just did that manually

# class ProductDetailsNCreate(
#     mixins.ListModelMixin,
#     mixins.CreateModelMixin,
#     generics.GenericAPIView,
# ):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)


# ----------------- Generic View ----------------------
# There are four types of ViewSets, from the most basic to the most powerful:

# ViewSet
# GenericViewSet
# ReadOnlyModelViewSet
# ModelViewSet


# ViewSet
# class ProductViewSet(ViewSet):
#     queryset = Product.objects.all()

#     def list(self, request):
#         serialize = ProductSerializer(self.queryset, many=True)
#         return Response(serialize.data)

#     def retrieve(self, request, pk=None):
#         item = get_object_or_404(Product, pk=pk)
#         serializer = ProductSerializer(item)
#         return Response(serializer.data)



# GenericViewSet
# class ProductViewSet(GenericViewSet):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

#     def list(self, request):
#         serialize = self.get_serializer(self.get_queryset(), many=True)
#         return Response(serialize.data)

#     def create(self, request):
#         serialize = self.get_serializer(data=request.data)

#         if serialize.is_valid():
#             serialize.save()
#             return Response(serialize.data, status=status.HTTP_201_CREATED)
#         return Response(serialize.error_message, status=status.HTTP_400_BAD_REQUEST)



# ModelViewSet
class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()



#ReadOnlyModelViewSet
# class ProductViewSet(ReadOnlyModelViewSet):
#     serializer_class = ProductSerializer
#     queryset = Product.objects.all()