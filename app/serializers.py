from .models import Restaurant, Menu, CustomUser, Vote
from rest_framework import serializers


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'password')

    # TODO: it doest return password, but it shows the field in swagger
    def to_representation(self, instance):
        # Call the parent class' to_representation method
        data = super().to_representation(instance)
        # Remove the 'password' field from the serialized data
        data.pop('password', None)
        return data


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'


class MenuSerializer(serializers.ModelSerializer):
    likes_count = serializers.SerializerMethodField()
    dislikes_count = serializers.SerializerMethodField()

    class Meta:
        model = Menu
        fields = ('id', 'restaurant', 'day', 'items', 'likes_count', 'dislikes_count')

    def get_likes_count(self, obj):
        return Vote.objects.filter(menu=obj, vote=True).count()

    def get_dislikes_count(self, obj):
        return Vote.objects.filter(menu=obj, vote=False).count()


class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ('vote',)
