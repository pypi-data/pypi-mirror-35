import os
import unittest
import uuid
import time
import logging
from murano_client.client import OutboundPayload

class TestOutboundPayloads(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass
    @classmethod
    def tearDownClass(cls):
        pass
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def test_maxretries_default(self):
        self.assertEqual(OutboundPayload.MaxRetries, 10)
    def test_override_maxretries(self):
        OutboundPayload.override_maxretries(1)
        self.assertEqual(OutboundPayload.MaxRetries, 1)
    def test_inc_retries(self):
        tell = OutboundPayload(
            payload='dummy',
            timestamp=time.time(),
            outbound_protocol='https')
        tell.inc_retries()
        self.assertEqual(tell.retries(), 1)


def main():
    unittest.main()

if __name__ == "__main__":
    main()
