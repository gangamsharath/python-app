import unittest
from webapp import app

class WebAppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_homepage(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Hello, World! Your Super", response.data)

    def test_aboutpage(self):
        response = self.app.get('/about')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Techmojo", response.data)



if __name__ == '__main__':
    unittest.main()