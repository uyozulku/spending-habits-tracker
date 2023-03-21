# unit and integration tests for methods in methods.py

import unittest
import methods


class TestMethods(unittest.TestCase):
    # test get_access_token
    def test_get_access_token(self):
        # get access token
        access_token = methods.get_access_token()

        # assert access token is not empty
        self.assertNotEqual(access_token, '')

    # test get_accounts
    def test_get_accounts(self):
        # get access token
        access_token = methods.get_access_token()

        # get accounts
        accounts = methods.get_accounts(access_token)

        # assert accounts is not empty
        self.assertNotEqual(accounts, '')

    # test get_balance
    def test_get_balance(self):
        # get access token
        access_token = methods.get_access_token()

        # get balance
        balance = methods.get_balance(access_token)

        # assert balance is not empty
        self.assertNotEqual(balance, '')

    # test get_identity
    def test_get_identity(self):
        # get access token
        access_token = methods.get_access_token()

        # get identity
        identity = methods.get_identity(access_token)

        # assert identity is not empty
        self.assertNotEqual(identity, '')