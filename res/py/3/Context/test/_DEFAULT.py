import unittest

class TestSome(unittest.TestCase):
    def test_some_0(self):
        expected = 1
        actual = 1
        self.assertEqual(expected, actual)

    def test_some_1(self):
        with self.assertRaises(Exception) as e:
            raise Exception('ERROR MESSAGE')
        self.assertEqual('ERROR MESSAGE', e.exception.args[0])
            

if __name__ == "__main__":
    unittest.main()
