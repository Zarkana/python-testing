import unittest


class MyCoolClass(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('foo'.upper(),'FOO')

    def test_upperish(self):
        self.assertEqual('foo'.upper(),'FOS')

    def test_uppersish(self):
        self.assertEqual('foo'.upper(),'FOO')

if __name__ == '__main__':
    unittest.main()
