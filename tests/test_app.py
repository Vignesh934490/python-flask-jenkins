import unittest
from app import app

class FlaskTestCase(unittest.TestCase):
    # Test to ensure the Flask app returns 'Hello, Jenkins!' at the root URL
    def test_hello_world(self):
        tester = app.test_client(self)
        response = tester.get('/')
        self.assertEqual(response.data, b'Hello, Jenkins!')

if __name__ == '__main__':
    unittest.main()

