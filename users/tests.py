from django.test import TestCase
from django.contrib.auth import get_user_model
from django.db.utils import IntegrityError

class UserTests(TestCase):
    def setUp(self) -> None:
        self.test_email = "test@user.com"
        self.test_superuser_email = "super@user.com"
        self.test_duplicate_email = "duplicate@user.com"
        self.test_password = "test"

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
