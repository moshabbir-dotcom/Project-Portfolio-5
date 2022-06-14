from django.test import TestCase
from .forms import OrderForm


class TestOrderFormRequired(TestCase):
    """
    Class to test checkout required fields.
    """
    def test_full_name_required(self):
        """
        Test full name field is required.
        """
        data = {
            'full_name': '',
            'email': 'test@tester.com',
            'phone_number': '123456789',
            'street_address1': 'street1',
            'street_address2': 'street2',
            'town_or_city': 'London',
            'postcode': 'HA1 1PE',
            'country': 'United Kingdom',
            'county': 'Harrow',
        }
        form = OrderForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('full_name', form.errors.keys())
        self.assertEqual(
            form.errors['full_name'][0],
            'This field is required.'
        )

    def test_email_required(self):
        """
        Test email field is required.
        """
        data = {
            'full_name': 'test',
            'email': '',
            'phone_number': '123456789',
            'street_address1': 'street1',
            'street_address2': 'street2',
            'town_or_city': 'London',
            'postcode': 'HA1 1PE',
            'country': 'United Kingdom',
            'county': 'Harrow',
        }
        form = OrderForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors.keys())
        self.assertEqual(
            form.errors['email'][0],
            'This field is required.'
        )

    def test_street_address1_required(self):
        """
        Test street1 field is required.
        """
        data = {
            'full_name': 'test',
            'email': 'test@tester.com',
            'phone_number': '123456789',
            'street_address1': '',
            'street_address2': 'street2',
            'town_or_city': 'London',
            'postcode': 'HA1 1PE',
            'country': 'United Kingdom',
            'county': 'Harrow',
        }
        form = OrderForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('street_address1', form.errors.keys())
        self.assertEqual(
            form.errors['street_address1'][0],
            'This field is required.'
        )

    # def test_postcode_required(self):
    #     """
    #     Test postcode field is required.
    #     """
    #     data = {
    #         'full_name': 'test',
    #         'email': 'test@tester.com',
    #         'phone_number': '123456789',
    #         'street_address1': 'street1',
    #         'street_address2': 'street2',
    #         'town_or_city': 'London',
    #         'postcode': '',
    #         'country': 'United Kingdom',
    #         'county': 'Harrow',
    #     }
    #     form = OrderForm(data=data)
    #     self.assertFalse(form.is_valid())
    #     self.assertIn('postcode', form.errors.keys())
    #     self.assertEqual(
    #         form.errors['postcode'][0],
    #         'This field is required.'
    #     )
