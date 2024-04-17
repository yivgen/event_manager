from django.test import TestCase
from django.contrib.auth import get_user_model
from django.db.utils import IntegrityError
from rest_framework.test import APIRequestFactory
from users.views import RegisterView

class UserTests(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.test_email = "test@user.com"
        cls.test_superuser_email = "super@user.com"
        cls.test_duplicate_email = "duplicate@user.com"
        cls.test_password = "test1234"

    def test_create_user(self):
        User = get_user_model()
        test_user = User.objects.create_user(email=self.test_email, password=self.test_password)
        self.assertEqual(test_user.email, self.test_email)
        self.assertTrue(test_user.check_password(self.test_password))

    def test_create_superuser(self):
        User = get_user_model()
        test_user = User.objects.create_superuser(
            email=self.test_superuser_email, 
            password=self.test_password
        )
        self.assertEqual(test_user.email, self.test_superuser_email)
        self.assertTrue(test_user.check_password(self.test_password))

    def test_email_unique_constraint(self):
        User = get_user_model()
        User.objects.create_user(email=self.test_duplicate_email, password=self.test_password)

        with self.assertRaises(IntegrityError):
            User.objects.create_user(email=self.test_duplicate_email, password=self.test_password)

class UserRegistrationTests(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.test_email = "test@user.com"
        cls.test_superuser_email = "super@user.com"
        cls.test_duplicate_email = "duplicate@user.com"
        cls.test_password = "TeSt1423"

    def setUp(self) -> None:
        self.factory = APIRequestFactory()

    def test_register_user(self):
        User = get_user_model()

        with self.assertRaises(User.DoesNotExist):
            User.objects.get(email=self.test_email)

        request = self.factory.post('/register/', {
            'email': self.test_email,
            'password': self.test_password,
            'password2': self.test_password
        })
        response = RegisterView.as_view()(request)

        self.assertEqual(response.status_code, 201)
        User.objects.get(email=self.test_email)