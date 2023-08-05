import unittest

from pycodec.hash.sha1 import SHA1


class Testing_SHA1(unittest.TestCase):
    def setUp(self):
        """Currently nothing to do. Use it for initialization data before test"""
        pass

    def tearDown(self):
        """Currently nothing to do. Use it for reinitialization data after test"""
        pass

    def test__SHA1_Encrypt_PeriodicA__Valid(self):
        sha1 = SHA1.hash(bytes('The quick brown fox jumps over the lazy cog', encoding='ascii'))
        self.assertEqual(sha1, bytes.fromhex('e4c4d8f3bf76b692de791a173e05321150f7a345b46484fe427f6acc7ecc81be'))
