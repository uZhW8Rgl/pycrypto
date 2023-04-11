import unittest
from os import urandom

from zokrates_pycrypto.fields import BN128Field
from zokrates_pycrypto.eddsa import PublicKey, PrivateKey


class TestEdDSA(unittest.TestCase):
    def test_signverify(self):
        # Hardcoded for now till we have automatic test generation for ZoKrates test framework
        key = BN128Field(
            1997011358982923168928344992199991480689546837621580239342656433234255379025
        )

        sk = PrivateKey(key)
        msg = urandom(32)
        sig = sk.sign(msg)

        pk = PublicKey.from_private(sk)
        self.assertTrue(pk.verify(sig, msg))


if __name__ == "__main__":
    unittest.main()
