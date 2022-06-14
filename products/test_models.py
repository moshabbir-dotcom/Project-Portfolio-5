from django.test import TestCase
from .models import Department, Product


class TestDepartmentModels(TestCase):

    def test_department_str(self):
        """tes department models __str__"""
        test_case = Department()
        test_case.name = "testing"
        self.assertEqual(str(test_case), "testing")

    def test_department_friendly_name(self):
        """test department models friendly name"""
        test_case = Department()
        test_case.friendly_name = "testing"
        self.assertEqual(test_case.get_friendly_name(), "testing")


class TestProductModels(TestCase):

    def test_product_str(self):
        """test products models __str__"""
        test_case = Product()
        test_case.name = "testing"
        self.assertEqual(str(test_case), "testing")