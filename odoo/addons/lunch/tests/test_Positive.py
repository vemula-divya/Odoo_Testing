from odoo.tests.common import TransactionCase
import logging


class TestNewSupplierProduct(TransactionCase):
    def setUp(self, *args, **kwargs):
        super(TestNewSupplierProduct, self).setUp(*args, **kwargs)

    def test_new_supplier_product(self):

        burger_category = self.env['lunch.product.category'].create({
            'name': 'Burger',
        })

        burger_king = self.env['res.partner'].create({
            'name': 'Burger King',
        })

        burger_supplier = self.env['lunch.supplier'].create({
            'partner_id': burger_king.id,
            'send_by': 'mail',
            'automatic_email_time': 12,
        })

        lunch_product = self.env['lunch.product'].create({
            'name': 'Whopper',
            'category_id': burger_category.id,
            'price': 20,
            'supplier_id': burger_supplier.id,
        })

        self.assertEqual(lunch_product.category_id.id, burger_category.id)
        self.assertEqual(lunch_product.name, 'Whopper')
        self.assertEqual(lunch_product.price, 20)
        logging.info("------Positive Scenario-----")
        logging.info("------  Passed Test Case two ------")
