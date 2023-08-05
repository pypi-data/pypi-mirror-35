import unittest

from pycodec.hash.sha2 import SHA2


class Testing_SHA2(unittest.TestCase):
    def setUp(self):
        """Currently nothing to do. Use it for initialization data before test"""
        pass

    def tearDown(self):
        """Currently nothing to do. Use it for reinitialization data after test"""
        pass

    def test__SHA224_Encrypt_PeriodicA__Valid(self):
        sha_224 = SHA2.hash_sha224(bytes('The quick brown fox jumps over the lazy cog', encoding='ascii'))
        self.assertEqual(sha_224, bytes.fromhex('fee755f44a55f20fb3362cdc3c493615b3cb574ed95ce610ee5b1e9b'))

    def test__SHA256_Encrypt_PeriodicA__Valid(self):
        sha_256 = SHA2.hash_sha256(bytes('The quick brown fox jumps over the lazy cog', encoding='ascii'))
        self.assertEqual(sha_256, bytes.fromhex('e4c4d8f3bf76b692de791a173e05321150f7a345b46484fe427f6acc7ecc81be'))

    def test__SHA384_Encrypt_PeriodicA__Valid(self):
        sha_384 = SHA2.hash_sha384(bytes('The quick brown fox jumps over the lazy cog', encoding='ascii'))
        self.assertEqual(sha_384, bytes.fromhex('098cea620b0978caa5f0befba6ddcf22764bea977e1c70b3483edfdf1de25f4b40d6cea3cadf00f809d422feb1f0161b'))

    def test__SHA512_224_Encrypt_PeriodicA__Valid(self):
        sha512_224 = SHA2.hash_sha512_224(bytes('The quick brown fox jumps over the lazy cog', encoding='ascii'))
        self.assertEqual(sha512_224, bytes.fromhex('2b9d6565a7e40f780ba8ab7c8dcf41e3ed3b77997f4c55aa987eede5'))

    def test__SHA512_256_Encrypt_PeriodicA__Valid(self):
        sha512_256 = SHA2.hash_sha512_256(bytes('The quick brown fox jumps over the lazy cog', encoding='ascii'))
        self.assertEqual(sha512_256, bytes.fromhex('cc8d255a7f2f38fd50388fd1f65ea7910835c5c1e73da46fba01ea50d5dd76fb'))

    def test__SHA512_Encrypt_PeriodicA__Valid(self):
        sha_512 = SHA2.hash_sha512(bytes('The quick brown fox jumps over the lazy cog', encoding='ascii'))
        self.assertEqual(sha_512, bytes.fromhex('3eeee1d0e11733ef152a6c29503b3ae20c4f1f3cda4cb26f1bc1a41f91c7fe4ab3bd86494049e201c4bd5155f31ecb7a3c8606843c4cc8dfcab7da11c8ae5045'))
