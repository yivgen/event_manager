from django.test import TestCase
from events.models import Event
from datetime import datetime, timezone
from django.db.utils import IntegrityError

class EventTests(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.test_title = 'Test event'
        cls.test_description = 'This is a test event.'
        cls.test_date = datetime.now(tz=timezone.utc)
        cls.test_location = 'Kiev, Independence Square'
        cls.test_organizer = 'Django'        

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
