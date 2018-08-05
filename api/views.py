from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, DestroyAPIView
from restaurants.models import Restaurant
from .serializers import RestaurantListSerializer, RestaurantDetailSerilizer, RestaurantCreateSerilizer

class RestaurantListView(ListAPIView):
	queryset = Restaurant.objects.all()
	serializer_class = RestaurantListSerializer

# Complete me
class RestaurantDetailView(RetrieveAPIView):
	queryset = Restaurant.objects.all()
	serializer_class = RestaurantDetailSerilizer
	lookup_field = 'id'
	lookup_url_kwarg = 'restaurant_id'

# Complete me
class RestaurantUpdateView(RetrieveUpdateAPIView):
	queryset = Restaurant.objects.all()
	serializer_class = RestaurantCreateSerilizer
	lookup_field = 'id'
	lookup_url_kwarg = 'restaurant_id'

# Complete me
class RestaurantDeleteView(DestroyAPIView):
	queryset = Restaurant.objects.all()
	serializer_class = RestaurantListSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'restaurant_id'