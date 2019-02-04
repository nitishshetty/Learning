import unittest


def iseven(number):
    if number % 2 == 0:
        return True
    else:
        return False


class TestIsEvenMethod(unittest.TestCase):

    def test_isEven1(self):
        res = iseven(5)
        self.assertEqual(res, False)

    def test_isEven2(self):
        res = iseven(10)
        self.assertEqual(res, True)

    def test_isEven3(self):
        res = iseven('hello')
        self.assertRaises(TypeError, "Type Error")


if __name__ == '__main__':
    unittest.main()
