from rest_framework import serializers
from events.models import Event
from events.utils import schedule_event_notification

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

class RegisterUserForEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('registered_users',)

    def validate(self, attrs):
        user =  self.context['request'].user
        instance = getattr(self, 'instance', None)
        if user in  instance.registered_users.all():
            raise serializers.ValidationError({"user": "User already registered"})

        return attrs

    def update(self, instance:Event, validated_data):
        user = self.context['request'].user
        instance.registered_users.add(user)
        schedule_event_notification(instance, user)
        instance.save()
        return instance