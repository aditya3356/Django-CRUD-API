from rest_framework.serializers import ModelSerializer

from api.models import Activity, Customer, Product


class CustomerSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class ActivitySerializer(ModelSerializer):
    class Meta:
        model = Activity
        fields = "__all__"
