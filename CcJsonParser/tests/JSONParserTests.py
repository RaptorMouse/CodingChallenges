import unittest
from JSONParser import JsonParser as JP

class JSONTestMethods(unittest.TestCase):

    def test_JSON_success(self):
        self.assertEqual(JP.main("step1\\valid.json"), 0)

    def test_JSON_failure(self):
        self.assertEqual(JP.main("step1\\invalid.json"), 1)

if __name__ == '__main__':
    unittest.main()