import unittest
from my_awesome_lib.data_utils import flatten_list, remove_duplicates

class TestDataUtils(unittest.TestCase):
    def test_flatten_list_basic(self):
        self.assertEqual(flatten_list([[1, 2], [3, 4]]), [1, 2, 3, 4])

    def test_flatten_list_empty(self):
        self.assertEqual(flatten_list([]), [])

    def test_flatten_list_nested_empty(self):
        self.assertEqual(flatten_list([[], []]), [])

    def test_flatten_list_single_element(self):
        self.assertEqual(flatten_list([[1], [2], [3]]), [1, 2, 3])

    def test_remove_duplicates_basic(self):
        result = remove_duplicates([1, 2, 2, 3, 3, 3])
        self.assertEqual(set(result), {1, 2, 3})

    def test_remove_duplicates_empty(self):
        self.assertEqual(remove_duplicates([]), [])

    def test_remove_duplicates_strings(self):
        result = remove_duplicates(["a", "b", "a"])
        self.assertEqual(set(result), {"a", "b"})

if __name__ == '__main__':
    unittest.main()
