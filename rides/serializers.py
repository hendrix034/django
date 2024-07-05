from rest_framework import serializers
from .models import User, Ride, RideEvent

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class RideEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = RideEvent
        fields = '__all__'

class RideSerializer(serializers.ModelSerializer):
    id_rider = UserSerializer()
    id_driver = UserSerializer()
    events = RideEventSerializer(many=True)
    todays_ride_events = serializers.SerializerMethodField()

    class Meta:
        model = Ride
        fields = '__all__'

    def get_todays_ride_events(self, obj):
        today = timezone.now()
        yesterday = today - timedelta(days=1)
        events = obj.events.filter(created_at__range=(yesterday, today))
        return RideEventSerializer(events, many=True).data
