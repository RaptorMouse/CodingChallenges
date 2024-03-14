import unittest
import JSONParser

class JSONTestMethods(unittest.TestCase):

    def test_JSON_success(self):
        self.assertEqual(JSONParser.main("step1\\valid.json"), 0)

    def test_JSON_failure(self):
        self.assertNotEqual(JSONParser.main("step1\\invalid.json"), 0)

if __name__ == '__main__':
    unittest.main()