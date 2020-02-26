import unittest
import ProjectA as prog

class TestMyProgram(unittest.TestCase) :
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'Foo')

    def test_isupper(self):
        self.assertTrue('Foo'.isupper())
        self.assertFalse('Foo'.isupper())

if __name__ == '__main__':
    unittest.main()