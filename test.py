import unittest

from my_sum import my_sum

class TestMySum(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 3]
        result = my_sum(data)
        self.assertEqual(result, 6)
    
    def test_diff_list(self):
        data = [5,6,7]
        result = my_sum(data)
        self.assertEqual(result, 18)

if __name__ == '__main__':
    unittest.main()