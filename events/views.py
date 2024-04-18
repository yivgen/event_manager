from rest_framework import generics
from events.models import Event
from events.serializers import EventSerializer, RegisterUserForEventSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q


class EventList(generics.ListCreateAPIView):
    serializer_class = EventSerializer

    def get_queryset(self):
        query = self.request.GET.get("q")
        if query:
            return Event.objects.filter(
                Q(title__icontains=query) | Q(description__icontains=query)
            )

        return Event.objects.all()

class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class RegisterUserForEvent(generics.UpdateAPIView):
    queryset = Event.objects.all()
    serializer_class = RegisterUserForEventSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
