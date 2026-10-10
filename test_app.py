import unittest
from app import *

class RedactionTests(unittest.TestCase):
    def test_email_removed(self):self.assertNotIn('alex@example.test',json.dumps(redact('alex@example.test')))
    def test_repeated_alias(self):self.assertEqual(redact('a@b.com a@b.com')['text'],'[EMAIL_1] [EMAIL_1]')
    def test_luhn(self):self.assertTrue(luhn('4111111111111111'));self.assertFalse(luhn('4111111111111112'))
    def test_ssn(self):self.assertEqual(redact('123-45-6789')['text'],'[SSN_1]')
    def test_safe_text(self):self.assertEqual(redact('hello world')['total'],0)
    def test_phone(self):self.assertEqual(redact('(202) 555-0123')['total'],1)

if __name__ == '__main__': unittest.main()
