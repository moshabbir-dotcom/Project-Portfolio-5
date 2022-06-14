from django.test import TestCase


class TestViews(TestCase):
    """
    A class to test the basket views.
    """
    def test_show_cart(self):
        """
        Test case to ensure the show basket view
        uses correct template and returns
        correct response.
        """
        response = self.client.get('/basket/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'basket/basket.html')