
import unittest
from whowantgroup import app

class WWGTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_hi(self):
        rv = self.app.get('/hi')
        print(rv.data.decode('utf-8'))
        assert b'hi' in rv.data

if __name__ == '__main__':
    unittest.main()