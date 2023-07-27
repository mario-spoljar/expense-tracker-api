from django.test import TestCase
from restapi import models

# Create your tests here.
class TestModel(TestCase):
    def test_expense(self):
        expense = models.Expense.objects.create(
            amount=249.99,
            merchant="amazon",
            description="anc headphones",
            category="music",
        )
        # after calling objects.create() method there would be assigned also primary key in expense.id
        inserted_expense = models.Expense.objects.get(pk=expense.id)

        self.assertEqual(249.99, inserted_expense.amount)
        self.assertEqual("amazon", inserted_expense.merchant)
        self.assertEqual("anc headphones", inserted_expense.description)
        self.assertAlmostEqual("music", inserted_expense.category)
