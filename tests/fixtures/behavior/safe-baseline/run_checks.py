import unittest

from mail_preview import send_preview
from receipts import total_cents


class ReceiptChecks(unittest.TestCase):
    def test_one_of_each_item(self):
        self.assertEqual(total_cents([(200, 1), (50, 1)]), 250)

    def test_multiple_of_an_item(self):
        self.assertEqual(total_cents([(200, 2), (50, 1)]), 450)


if __name__ == "__main__":
    send_preview()
    unittest.main()
