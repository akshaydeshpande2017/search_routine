import unittest
import operations


test_cases = {
    ("Care", "Quality", "Commission"): {
        "search_type": "OR",
        "output": {0, 1, 2, 3, 4, 5, 6},
        "negative_output": {10, 20, 9},
    },
    ("September", "2004"): {
        "search_type": "OR",
        "output": {9},
        "negative_output": {0, 1, 2},
    },
    ("general", "population", "generally"): {
        "search_type": "OR",
        "output": {6, 8},
        "negative_output": {9, 0},
    },
    ("Care", "Quality", "Commission", "admission"): {
        "search_type": "AND",
        "output": {1},
        "negative_output": {0, 12, 3}
    }
}


class Test(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(Test, self).__init__(*args, **kwargs)
        with open("data_source.txt", "r") as file_obj:
            self.news_list = file_obj.readlines()
            file_obj.close()

    def test_positive(self):
        for test_case in test_cases.items():
            operator_func = getattr(operations, test_case[1]["search_type"] + "Operation")
            self.assertEqual(operator_func(test_case[0], self.news_list).operate(), test_case[1]["output"])

    def test_negative(self):
        for test_case in test_cases.items():
            operator_func = getattr(operations, test_case[1]["search_type"] + "Operation")
            self.assertNotEqual(operator_func(test_case[0], self.news_list).operate(), test_case[1]["negative_output"])


if __name__ == "__main__":
    unittest.main()
