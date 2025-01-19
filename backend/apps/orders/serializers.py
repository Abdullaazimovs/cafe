from rest_framework import serializers
from apps.dishes.models import Dishes
from apps.orders.models import Order, OrderDish


class OrderCreateSerializer(serializers.ModelSerializer):
    dishes = serializers.PrimaryKeyRelatedField(queryset=Dishes.objects.all(), many=True, required=False)

    class Meta:
        model = Order
        fields = ['table', 'dishes', 'status', 'total_price']

    def validate(self, data):
        order = Order(**data)  # Create an unsaved instance of the model
        order.clean()  # This will call the clean method and raise ValidationError if any
        return data

    def create(self, validated_data):
        dishes = validated_data.pop('dishes', [])
        table = validated_data.pop('table')

        order = Order.objects.create(table=table, **validated_data)

        if dishes:
            order.dishes.set(dishes)

        order.save()
        return order


class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dishes
        fields = ['id', 'name', 'price']


class OrderDishSerializer(serializers.ModelSerializer):
    dish = DishSerializer()

    class Meta:
        model = OrderDish
        fields = ['dish', 'quantity']
