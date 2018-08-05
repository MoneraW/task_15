from rest_framework import serializers
from restaurants.models import Restaurant

class RestaurantListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = [ 'id',
        	'name',
        	'opening_time',
        	'closing_time',
        	]

class RestaurantDetailSerilizer(serializers.ModelSerializer):
	class Meta:
		model = Restaurant
		fields = ['id', 'owner', 'name', 'description', 'opening_time', 'closing_time',]


class RestaurantCreateSerilizer(serializers.ModelSerializer):
	class Meta:
		model = Restaurant
		fields = ['name', 'description', 'opening_time', 'closing_time',]