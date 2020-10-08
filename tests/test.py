import unittest

import requests


class BasicTests(unittest.TestCase):
    def addition_test(self):
        # Given
        num1 = 100
        num2 = 200

        # When
        response = requests.post("http://127.0.0.1:5000/api/addition",
                                 data={'num1': num1,
                                       'num2': num2})

        res_json = response.json()
        result = res_json['result']

        # Then
        self.assertEqual(result, 300)


if __name__ == "__main__":
    unittest.main()