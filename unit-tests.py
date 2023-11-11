import unittest
import pytest

def sum_list(lst):
    return sum(lst)

def get_value_from_dict(dictionary, key):
    return dictionary.get(key, None)

def concatenate_strings(string_list):
    return ''.join(string_list)

class TestDataCollectionsFunctions(unittest.TestCase):

    @pytest.mark.parametrize("input_list, expected_sum", [([1, 2, 3], 6), ([4, 5, 6], 15), ([], 0)])
    def test_sum_list(self, input_list, expected_sum):
        result = sum_list(input_list)
        self.assertEqual(result, expected_sum)

    @pytest.mark.parametrize("input_dict, key, expected_value", [({"a": 1, "b": 2}, "a", 1), ({"x": 10, "y": 20}, "z", None), ({}, "key", None)])
    def test_get_value_from_dict(self, input_dict, key, expected_value):
        result = get_value_from_dict(input_dict, key)
        self.assertEqual(result, expected_value)

    @pytest.mark.parametrize("input_strings, expected_result", [(['Hello', ' ', 'World'], 'Hello World'), (['Python', ' is ', 'awesome'], 'Python is awesome'), ([], '')])
    def test_concatenate_strings(self, input_strings, expected_result):
        result = concatenate_strings(input_strings)
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()