import unittest
import os.path
import paramiko

from tornado.httputil import HTTPServerRequest
from tests.utils import read_file
from webssh.handler import MixinHandler, IndexHandler, parse_encoding
from webssh.settings import base_dir


class TestHandler(unittest.TestCase):

    def test_parse_encoding(self):
        data = ''
        self.assertIsNone(parse_encoding(data))
        data = 'UTF-8'
        self.assertEqual(parse_encoding(data), 'UTF-8')
        data = 'en_US.UTF-8'
        self.assertEqual(parse_encoding(data), 'UTF-8')
        data = 'LANG=en_US.UTF-8\nLANGUAGE=\nLC_CTYPE="en_US.UTF-8"\n'
        self.assertEqual(parse_encoding(data), 'UTF-8')
        data = 'LANGUAGE=\nLC_CTYPE="en_US.UTF-8"\n'
        self.assertEqual(parse_encoding(data), 'UTF-8')


class TestMixinHandler(unittest.TestCase):

    def test_get_real_client_addr(self):
        handler = MixinHandler()
        handler.request = HTTPServerRequest(uri='/')
        self.assertIsNone(handler.get_real_client_addr())

        ip = '127.0.0.1'
        handler.request.headers.add('X-Real-Ip', ip)
        self.assertEqual(handler.get_real_client_addr(), False)

        handler.request.headers.add('X-Real-Port', '12345x')
        self.assertEqual(handler.get_real_client_addr(), False)

        handler.request.headers.update({'X-Real-Port': '12345'})
        self.assertEqual(handler.get_real_client_addr(), (ip, 12345))

        handler.request.headers.update({'X-Real-ip': None})
        self.assertEqual(handler.get_real_client_addr(), False)

        handler.request.headers.update({'X-Real-Port': '12345x'})
        self.assertEqual(handler.get_real_client_addr(), False)


class TestIndexHandler(unittest.TestCase):

    def test_get_specific_pkey_with_plain_key(self):

        fname = 'test_rsa.key'
        cls = paramiko.RSAKey
        key = read_file(os.path.join(base_dir, 'tests', fname))
        pkey = IndexHandler.get_specific_pkey(cls, key, None)
        self.assertIsInstance(pkey, cls)
        pkey = IndexHandler.get_specific_pkey(cls, key, 'iginored')
        self.assertIsInstance(pkey, cls)
        pkey = IndexHandler.get_specific_pkey(cls, 'x'+key, None)
        self.assertIsNone(pkey)

    def test_get_specific_pkey_with_encrypted_key(self):
        fname = 'test_rsa_password.key'
        cls = paramiko.RSAKey
        password = 'television'

        key = read_file(os.path.join(base_dir, 'tests', fname))
        pkey = IndexHandler.get_specific_pkey(cls, key, password)
        self.assertIsInstance(pkey, cls)
        pkey = IndexHandler.get_specific_pkey(cls, 'x'+key, None)
        self.assertIsNone(pkey)

        with self.assertRaises(ValueError):
            pkey = IndexHandler.get_specific_pkey(cls, key, None)

    def test_get_pkey_obj_with_plain_key(self):
        fname = 'test_ed25519.key'
        cls = paramiko.Ed25519Key
        key = read_file(os.path.join(base_dir, 'tests', fname))
        pkey = IndexHandler.get_pkey_obj(key, None)
        self.assertIsInstance(pkey, cls)
        pkey = IndexHandler.get_pkey_obj(key, 'iginored')
        self.assertIsInstance(pkey, cls)
        with self.assertRaises(ValueError):
            pkey = IndexHandler.get_pkey_obj('x'+key, None)

    def test_get_pkey_obj_with_encrypted_key(self):
        fname = 'test_ed25519_password.key'
        password = 'abc123'
        cls = paramiko.Ed25519Key
        key = read_file(os.path.join(base_dir, 'tests', fname))
        pkey = IndexHandler.get_pkey_obj(key, password)
        self.assertIsInstance(pkey, cls)
        with self.assertRaises(ValueError):
            pkey = IndexHandler.get_pkey_obj(key, 'wrongpass')
        with self.assertRaises(ValueError):
            pkey = IndexHandler.get_pkey_obj('x'+key, password)
