from django.test import TestCase
from .models import Order


class TestCheckoutViews(TestCase):
    """
    Class to contain test cases for the
    checkout models.
    """
    def test_checkout_view(self):
        """
        Test case to ensure checkout view is
        using correct template with response
        """
        response = self.client.get('/checkout/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/products/')

    def test_checkout_success_view(self):
        """
        Test case to ensure the checkout
        success view is working.
        """
        order = Order.objects.create(
            full_name='Test Customer',
            email='test@test.com',
            postcode='HA1 1PE',
            town_or_city='London',
            street_address1='Street 1',
            street_address2='Street 2',
            county='Harrow',
            grand_total=34.99,
            delivery_cost=5.00,
            order_total=29.99,
        )
        response = self.client.get(
            f'/checkout/checkout_success/{order.order_number}'
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('checkout/checkout_success.html')