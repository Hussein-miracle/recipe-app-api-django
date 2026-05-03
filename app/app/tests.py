"""
Sample Tests
"""

from django.test import SimpleTestCase

from . import calc


class CalcTests(SimpleTestCase):
    """Tests the 'calc' module """

    def test_add_numbers(self):
        """Test adding numbers together"""
        outcome = calc.add(5, 6)
        self.assertEqual(outcome, 11)

    def test_substract_numbers(self):
        """Test substract numbers"""
        value = calc.sub(6, 5)
        self.assertEqual(value, 1)
