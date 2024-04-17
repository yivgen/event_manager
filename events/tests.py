from django.test import TestCase
from events.models import Event
from datetime import datetime, timezone
from django.db.utils import IntegrityError
from rest_framework.test import APIRequestFactory
from events.views import EventList, EventDetail

class EventModelTests(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.test_title = 'Test event'
        cls.test_title_updated = 'New test event'
        cls.test_description = 'This is a test event.'
        cls.test_date = datetime.now(tz=timezone.utc)
        cls.test_location = 'Kiev, Independence Square'
        cls.test_organizer = 'Django'

    def setUp(self) -> None:
        self.factory = APIRequestFactory()

    def test_create_event(self):
        event = Event.objects.create(
            title=self.test_title,
            description=self.test_description,
            date=self.test_date,
            location=self.test_location,
            organizer=self.test_organizer
        )

        self.assertEqual(event.title, self.test_title)
        self.assertEqual(event.description, self.test_description)
        self.assertEqual(event.date, self.test_date)
        self.assertEqual(event.location, self.test_location)
        self.assertEqual(event.organizer, self.test_organizer)

    def test_title_not_null_constraint(self):
        with self.assertRaises(IntegrityError):
            Event.objects.create(
                title=None,
                description=self.test_description,
                date=self.test_date,
                location=self.test_location,
                organizer=self.test_organizer
            )

    def test_organizer_not_null_constraint(self):
        with self.assertRaises(IntegrityError):
            Event.objects.create(
                title=self.test_title,
                description=self.test_description,
                date=self.test_date,
                location=self.test_location,
                organizer=None
            )

    def test_create_api(self):
        with self.assertRaises(Event.DoesNotExist):
            Event.objects.get(title=self.test_title)

        request = self.factory.post(f'/api/events/', {
            'title': self.test_title,
            'description': self.test_description,
            'date': self.test_date,
            'location': self.test_location,
            'organizer': self.test_organizer
        })

        resposne = EventList.as_view()(request)
        self.assertEqual(resposne.status_code, 201)
        Event.objects.get(title=self.test_title)

    def test_retrieve_api(self):
        event = Event.objects.create(
            title=self.test_title,
            description=self.test_description,
            date=self.test_date,
            location=self.test_location,
            organizer=self.test_organizer
        )

        request = self.factory.get(f'/api/events/')
        resposne = EventDetail.as_view()(request, pk=event.pk)

        self.assertEqual(resposne.status_code, 200)

    def test_update_api(self):
        with self.assertRaises(Event.DoesNotExist):
            Event.objects.get(title=self.test_title_updated)

        event = Event.objects.create(
            title=self.test_title,
            description=self.test_description,
            date=self.test_date,
            location=self.test_location,
            organizer=self.test_organizer
        )

        request = self.factory.put(f'/api/events/', {
            'title': self.test_title_updated,
            'description': self.test_description,
            'date': self.test_date,
            'location': self.test_location,
            'organizer': self.test_organizer
        })

        resposne = EventDetail.as_view()(request, pk=event.pk)
        self.assertEqual(resposne.status_code, 200)
        Event.objects.get(title=self.test_title_updated)
    
    def test_delete_api(self):
        event = Event.objects.create(
            title=self.test_title,
            description=self.test_description,
            date=self.test_date,
            location=self.test_location,
            organizer=self.test_organizer
        )

        request = self.factory.delete(f'/api/events/')
        response = EventDetail.as_view()(request, pk=event.pk)

        self.assertEqual(response.status_code, 204)
        with self.assertRaises(Event.DoesNotExist):
            Event.objects.get(pk=event.pk)