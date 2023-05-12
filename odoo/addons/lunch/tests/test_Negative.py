from odoo.tests.common import TransactionCase
import logging

class TestLunchNegative(TransactionCase):
    def setUp(self, *args, **kwargs):
        super(TestLunchNegative, self).setUp(*args, **kwargs)

    def test_invalid_supplier(self):
        """test invalid supplier creation"""

        partner_details = self.env['res.partner'].create({
            'name': 'Lunch Supplier',
        })
        supplier = self.env['lunch.supplier'].create({
            'partner_id': partner_details.id,
            'send_by': 'mail',
            'automatic_email_time': 12,
            'tz': 'Asia/Kolkata',
        })

        self.assertEqual(supplier.send_by, 'phone')
        logging.info("------Negative  Scenario-----")
        logging.info("------  Passed Test Case two ------")


