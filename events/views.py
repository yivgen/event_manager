from rest_framework import generics
from events.models import Event
from events.serializers import EventSerializer, RegisterUserForEventSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class EventList(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class RegisterUserForEvent(generics.UpdateAPIView):
    queryset = Event.objects.all()
    serializer_class = RegisterUserForEventSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
