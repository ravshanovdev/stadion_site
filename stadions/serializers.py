from rest_framework import serializers
from .models import Stadion, OrderStadion
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'role']


class StadionSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)

    class Meta:
        model = Stadion
        fields = "__all__"


class StadionListSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    manager = UserSerializer(read_only=True)

    class Meta:
        model = Stadion
        fields = "__all__"


class OrderStadionSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    stadion = StadionListSerializer(read_only=True)

    class Meta:
        model = OrderStadion
        fields = "__all__"
