from django.test import TestCase
from django.contrib.auth import get_user_model

from decimal import Decimal

from core import models


def create_user(email="user@example.com", password="test123"):
    """Creates and return a new user"""
    return get_user_model().objects.create_user(email=email, password=password)


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

    def test_create_recipe(self):
        """Tests create recipe success"""

        user = get_user_model().objects.create_user('test@example.com', 'testpass123')

        recipe = models.Recipe.objects.create(
            user=user,
            title="Sample recipe name",
            time_minutes=5,
            price=Decimal('5.50'),
            description='Sample recipe description'
        )

        self.assertEqual(str(recipe), recipe.title)

    def test_create_tag(self):
        """Test creating tag is successfull"""

        user = create_user()
        tag = models.Tag.objects.create(user=user, name="Tag-1")
        self.assertEqual(str(tag), tag.name)

    def test_create_ingredient(self):
        """Test creating an ingredient is successful."""
        user = create_user()
        ingredient = models.Ingredient.objects.create(
            user=user,
            name='Ingredient1'
        )

        self.assertEqual(str(ingredient), ingredient.name)
