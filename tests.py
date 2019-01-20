from http import HTTPStatus
import unittest

from app import create_app
from config import TestConfig


class TestApi(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestConfig)
        self.client = self.app.test_client()

    def test_health_check(self):
        smoke_resp = self.client.get('/smoke')
        self.assertEqual(smoke_resp.status_code, HTTPStatus.OK)


if __name__ == '__main__':
    unittest.main(verbosity=2)
