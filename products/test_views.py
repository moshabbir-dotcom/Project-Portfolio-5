from django.test import TestCase

from django.shortcuts import reverse
from django.contrib.messages import get_messages
from .models import Department, Product


class TestProductsViews(TestCase):

    fixtures = [
        'departments.json',
        'products.json'
    ]

    def test_products_page_url_exists(self):
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)

    def test_the_products_url_is_accessible_by_name(self):
        response = self.client.get(reverse('products'))
        self.assertEqual(response.status_code, 200)

    def test_products_page_template(self):
        response = self.client.get(reverse('products'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')

    def test_sort_name_function(self):
        department_name = 'oily'
        sort_array = ['name', 'department']
        for sort in sort_array:
            direction = 'asc'
            current_sorting = f'{sort}_{direction}'
            response = self.client.get(
                f'/products/?department={department_name}'
                f'&sort={sort}&direction={direction}')
        self.assertEqual(current_sorting, f'{sort}_asc')
        self.assertEqual(response.status_code, 200)

    def test_product_detail_page_url_exists(self):
        response = self.client.get('/products/1/')
        self.assertEqual(response.status_code, 200)

    def test_the_product_detail_url_is_accessible_by_name(self):
        response = self.client.get(reverse('product_detail', args="1"))
        self.assertEqual(response.status_code, 200)

    def test_product_detail_page_template(self):
        response = self.client.get('/products/1/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_detail.html')