from rest_framework import serializers
from .models import Product, Order, OrderItem


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("id", "name", "price", "stock")

    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError("Price cannot be less than 0")
        return value


class OrderItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source="product.name")
    product_price = serializers.CharField(source="product.price")

    class Meta:
        model = OrderItem
        fields = ("product_name", "product_price", "quantity" , "total_price")


class OrderSerializer(serializers.ModelSerializer):
    item = OrderItemSerializer(many=True, read_only=True)
    total_price = serializers.SerializerMethodField()

    def get_total_price(self, obj):
        order_items = obj.item.all()
        return sum(order_item.total_price for order_item in order_items)

    class Meta:
        model = Order
        fields = ("order_id", "user", "created_at", "status", "item", "total_price")
