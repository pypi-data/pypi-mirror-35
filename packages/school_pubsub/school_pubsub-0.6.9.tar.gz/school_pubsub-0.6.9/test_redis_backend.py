"""
Test the PubNub backend
"""
from backends import RedisBackend
import unittest


class TestPubNubBackend(unittest.TestCase):
    def setUp(self):

        self.pb = RedisBackend('test-channel')

    def test_publish(self):
        example_payload = {"foo": "bar"}
        self.pb.publish('example.test', example_payload)

    # def test_subscribe(self):
    #     pb.subscribe()


if __name__ == '__main__':
    unittest.main()
