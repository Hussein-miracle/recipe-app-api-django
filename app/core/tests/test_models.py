from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelsTests(TestCase):
    """Tests models"""

    def test_create_user_with_email_successful(self):
        """Tests creating an user with email is succesful"""
        email = 'test@example.com'
        password = "Password@123"
        user = get_user_model().objects.create_user(email=email, password=password)
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_is_normalized(self):
        """Tests emails is normalized for new users"""
        sample_emails = [
            ['test1@EXAMPLE.com', 'test1@example.com'],
            ['Test2@Example.com', 'Test2@example.com'],
            ['TEST3@EXAMPLE.COM', 'TEST3@example.com'],
            ['TEST4@EXAMPLE.com', 'TEST4@example.com'],
            ['TEST5@example.COM', 'TEST5@example.com'],
        ]

        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(email, "sample123")
            self.assertEqual(user.email, expected)

    def test_new_user_without_email_raises_error(self):
        """Tests that creating a new user without email raises error"""

        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', 'test123')

    def test_create_superuser(self):
        """Tests create superuser/admin"""
        user = get_user_model().objects.create_superuser(
            "test@example.com", 'Password123!')
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
