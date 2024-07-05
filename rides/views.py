from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import User, Ride, RideEvent
from .serializers import UserSerializer, RideSerializer, RideEventSerializer
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

class RidePagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class RideViewSet(viewsets.ModelViewSet):
    queryset = Ride.objects.all().prefetch_related('id_rider', 'id_driver').select_related('id_rider', 'id_driver')
    serializer_class = RideSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = RidePagination
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['pickup_time']
    search_fields = ['status', 'id_rider__email']

    def get_queryset(self):
        queryset = self.queryset
        status = self.request.query_params.get('status')
        email = self.request.query_params.get('email')
        if status:
            queryset = queryset.filter(status=status)
        if email:
            queryset = queryset.filter(id_rider__email=email)
        return queryset

class RideEventViewSet(viewsets.ModelViewSet):
    queryset = RideEvent.objects.all()
    serializer_class = RideEventSerializer
    permission_classes = [IsAuthenticated]
