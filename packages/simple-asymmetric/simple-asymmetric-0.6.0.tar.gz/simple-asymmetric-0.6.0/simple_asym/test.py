import unittest
import pysodium
from .crypto import (
    generate_keys, export_private_key, export_public_key, import_key_pair,
    hash_password, rsa_decrypt, rsa_encrypt, authenticated_encryption, verify_owner
)
from .asymmetric_encryption import Asym
from .exceptions import (
    MissingRsaKeyPairException, MissingSymmetricKeyException)


class TestCrypto(unittest.TestCase):
    def test_make_and_export_RSA_key(self):
        key_pair = generate_keys()
        private_key = export_private_key(key_pair, "vacation")
        public_key = export_public_key(key_pair)
        self.assertEqual(len(private_key), 120)
        self.assertEqual(len(public_key), 44)

    def test_import_rsa_key(self):
        key_pair = generate_keys()
        private_key = export_private_key(key_pair)
        public_key = export_public_key(key_pair)
        imported_key_pair = import_key_pair(public_key, private_key)
        self.assertEqual(
            imported_key_pair['private_key'], key_pair['private_key'])
        self.assertEqual(
            imported_key_pair['public_key'], key_pair['public_key'])

    def test_import_rsa_key_from_base64(self):
        private_b64 = '2A28PjsDW/WpQqMXPLTIkL99VwnofGRqNL7wdJrzUyo='
        public_b64 = 'jim48h9bcjw85PcnaSjOAvg022kJ/Q4aTzxb8hPtGlE='
        imported_key_pair = import_key_pair(public_b64, private_b64)
        # Is the key usable?
        nonce = pysodium.randombytes(pysodium.crypto_box_NONCEBYTES)
        ciphertext = pysodium.crypto_box(
            'test',
            nonce,
            imported_key_pair['public_key'],
            imported_key_pair['private_key'],
        )

    def test_export_and_import_private_key_with_password(self):
        private_b64 = '2A28PjsDW/WpQqMXPLTIkL99VwnofGRqNL7wdJrzUyo='
        public_b64 = 'jim48h9bcjw85PcnaSjOAvg022kJ/Q4aTzxb8hPtGlE='
        password = 'hunter2'
        key_pair = import_key_pair(public_b64, private_b64)
        exported_public_key = export_public_key(key_pair)
        exported_private_key = export_private_key(key_pair, password)
        imported_key = import_key_pair(
            exported_public_key, exported_private_key, password)
        self.assertEqual(imported_key, key_pair)

    def test_hashes_password(self):
        password = 'hunter2'
        salt = bytes(
            [88, 240, 185, 66, 195, 101, 160, 138, 137, 78, 1, 2, 3, 4, 5, 6]
        )
        hash = hash_password(password, salt)
        self.assertEqual(hash[0], 49)

    def test_export_with_password(self):
        password = 'hunter2'
        key_pair = generate_keys()
        private_key = export_private_key(key_pair, password)
        self.assertIsNotNone(private_key)
    
    def test_identity(self):
        keys_bob = generate_keys()
        keys_alice = generate_keys()
        message = "bleh"
        ciphertext = authenticated_encryption(keys_bob['public_key'], keys_alice['private_key'], message)

        verified = verify_owner(keys_bob['public_key'], keys_bob['private_key'], ciphertext)
        self.assertFalse(verified)

        verified = verify_owner(keys_alice['public_key'], keys_bob['private_key'], ciphertext)
        self.assertTrue(verified)

    def test_identity_js_data(self):
        """ Test identity with data generated from JS version """
        public_key = bytes([103, 223, 142, 236, 93, 15, 73, 32, 221, 48, 28, 227, 36, 112, 225, 69, 51, 206, 100, 173, 212, 247, 163, 219, 255, 6, 236, 50, 94, 224, 47, 89])
        private_key = bytes([154, 145, 101, 104, 245, 114, 225, 1, 25, 50, 109, 117, 219, 34, 81, 43, 41, 83, 14, 244, 30, 79, 85, 230, 199, 253, 36, 176, 221, 172, 164, 136])
        ciphertext = bytes([69, 180, 118, 184, 3, 127, 140, 190, 165, 3, 151, 141, 62, 206, 199, 173, 75, 70, 225, 2, 105, 28, 1, 215, 224, 11, 30, 245, 118, 62, 137, 179, 234, 196, 6, 167, 196, 1, 45, 122, 209, 40, 167, 86])

        verified = verify_owner(public_key, private_key, ciphertext)
        self.assertTrue(verified)

    def test_rsa_encrypt_and_decrypt(self):
        key_pair = generate_keys()
        message = 'test Ơ'
        ciphertext = rsa_encrypt(key_pair['public_key'], message)
        self.assertNotEqual(ciphertext, message)
        decrypted_message = rsa_decrypt(
            key_pair['public_key'], key_pair['private_key'], ciphertext)
        self.assertEqual(decrypted_message, message)


class TestAsym(unittest.TestCase):
    asym: Asym = None

    def setUp(self):
        self.asym = Asym()

    def test_make_rsa_keys(self):
        keys = self.asym.make_rsa_keys()
        self.assertEqual(len(keys[0]), 44)
        self.assertEqual(len(keys[1]), 44)

    def test_make_rsa_keys_with_password(self):
        keys = self.asym.make_rsa_keys('123456')
        self.assertEqual(len(keys[0]), 120)
        self.assertEqual(len(keys[1]), 44)

    def test_import_rsa_key_pair(self):
        private_key_base64 = 'TCkVmbGlDxi9t+ZIYeYTgRLoHCe7kmW4AhfS8/VKqkI='
        public_key_base64 = 'wL+JHgcJs5aRYMjF8QmHcUVCWdE5ENzLVsKEf9V2UHM='
        keyPair = self.asym.set_key_pair(public_key_base64, private_key_base64)

    def test_import_rsa_key_pair_with_encrypted_private_key(self):
        private_key_base64 = 'HNP8i6zQS6Kj1b0tovnnySFCfLHWJ7ZBKfHCqperfAbgRXdlabRgRtTbb2ZyT25isGkg390tKGn+rE7emNgbkqvf9Qd6CgG37pclw0UUQy9TruasDA3/lQ=='
        public_key_base64 = 'KJ6WVf8VsH6D9842K+j0o8kGapyGSuT+MYwiw8MTdCY='
        password = '123456'

        # Try with bad password
        with self.assertRaises(Exception):
            self.asym.set_key_pair(
                public_key_base64, private_key_base64, "nope")

        key_pair = self.asym.set_key_pair(
            public_key_base64, private_key_base64, password)
        self.assertIsNotNone(key_pair)

    def test_encrypt_decrypt_using_rsa(self):
        plaintext = 'hi☢⛴'
        private_key_base64 = 'TCkVmbGlDxi9t+ZIYeYTgRLoHCe7kmW4AhfS8/VKqkI='
        public_key_base64 = 'wL+JHgcJs5aRYMjF8QmHcUVCWdE5ENzLVsKEf9V2UHM='

        self.asym.set_key_pair(public_key_base64, private_key_base64)
        ciphertext = self.asym.rsa_encrypt(
            self.asym.key_pair['public_key'], plaintext)
        self.assertNotEqual(ciphertext, plaintext)
        decrypted = self.asym.rsa_decrypt(ciphertext)
        self.assertEqual(decrypted, plaintext)

    def test_generate_symmetric_key(self):
        key = self.asym.make_symmetric_key()
        self.assertIsNotNone(key)

    def test_set_symmetric_key(self):
        key = self.asym.make_symmetric_key()
        self.asym.set_symmetric_key(key)
        self.assertIsNotNone(self.asym.symmetric_key)

    def test_get_and_set_encrypted_shared_symmetric_key(self):
        private_key_base64 = 'TCkVmbGlDxi9t+ZIYeYTgRLoHCe7kmW4AhfS8/VKqkI='
        public_key_base64 = 'wL+JHgcJs5aRYMjF8QmHcUVCWdE5ENzLVsKEf9V2UHM='

        self.asym.set_key_pair(public_key_base64, private_key_base64)
        key = self.asym.make_symmetric_key()
        encrypted_key = self.asym.get_encrypted_symmetric_key(
            self.asym.get_public_key())
        self.assertNotEqual(encrypted_key, key)
        self.asym.set_symmetric_key_from_encrypted(encrypted_key)
        self.assertEqual(self.asym.get_symmetric_key(), key)

    def test_encrypt_and_decrypt_using_symmetric_key(self):
        key = 'HMS11YymAKX5z6d6/hhdvyGtj7wiTfwzaO0O3ptSHZ4='
        message = 'hello'
        self.asym.set_symmetric_key(key)
        ciphertext = self.asym.encrypt(message)
        self.assertNotEqual(ciphertext, message)
        decrypted = self.asym.decrypt(ciphertext)
        self.assertEqual(decrypted, message)

    def test_bob_and_alice_integration_test(self):
        bob = Asym()
        alice = Asym()
        message = "hello"

        # Generate both keypairs
        bob.make_rsa_keys()
        alice.make_rsa_keys()

        # Generate one (to be shared) symmetric key
        bob.make_symmetric_key()

        # Key Exchange
        encrypted_symmetric_key = bob.get_encrypted_symmetric_key(
            alice.get_public_key())
        alice.set_symmetric_key_from_encrypted(encrypted_symmetric_key)

        # Send a message
        ciphertext = bob.encrypt(message)
        self.assertNotEqual(ciphertext, message)
        # It shold be base64 (not bytes)
        self.assertIsInstance(ciphertext, str)

        decrypted_message = alice.decrypt(ciphertext)
        self.assertEqual(decrypted_message, message)
