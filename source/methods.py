# some helper functions
# 1) get access token
# 2) get transactions
# 3) get accounts


import plaid
import json
import os
from dotenv import load_dotenv

load_dotenv()

# get access token
def get_access_token():
    # get access token from plaid api
    # return access token

    # create client object
    client = plaid.Client(
        client_id=os.getenv('PLAID_CLIENT_ID'),
        secret=os.getenv('PLAID_SECRET'),
        environment=os.getenv('PLAID_ENV'),
        api_version='2020-09-14'
    )

    # create public token
    create_tkn_response = client.Sandbox.public_token.create(
        os.getenv('PLAID_INSTITUTION_ID'), ['transactions'])

    # exchange public token for access token
    exchange_response = client.Item.public_token.exchange(
        create_tkn_response['public_token'])

    # return access token
    return exchange_response['access_token']

# get transactions
def get_transactions(access_token):
    # get transactions from plaid api
    # return json object

    # create client object
    client = plaid.Client(
        client_id=os.getenv('PLAID_CLIENT_ID'),
        secret=os.getenv('PLAID_SECRET'),
        environment=os.getenv('PLAID_ENV'),
        api_version='2020-09-14'
    )

    # get transactions
    transactions_response = client.Transactions.get(access_token, '2020-01-01', '2020-09-14')

    # return json object
    return json.dumps(transactions_response['transactions'][:2], indent=4, sort_keys=True)


# get accounts
def get_accounts(access_token):
    # get accounts from plaid api
    # return json object

    # create client object
    client = plaid.Client(
        client_id=os.getenv('PLAID_CLIENT_ID'),
        secret=os.getenv('PLAID_SECRET'),
        environment=os.getenv('PLAID_ENV'),
        api_version='2020-09-14'
    )

    # get accounts
    accounts_response = client.Accounts.get(access_token)

    # return json object
    return json.dumps(accounts_response['accounts'][:2], indent=4, sort_keys=True)

# get balance
def get_balance(access_token):
    # get balance from plaid api
    # return json object

    # create client object
    client = plaid.Client(
        client_id=os.getenv('PLAID_CLIENT_ID'),
        secret=os.getenv('PLAID_SECRET'),
        environment=os.getenv('PLAID_ENV'),
        api_version='2020-09-14'
    )

    # get balance
    balance_response = client.Accounts.balance.get(access_token)

    # return json object
    return json.dumps(balance_response['accounts'][:2], indent=4, sort_keys=True)


# get identity
def get_identity(access_token):
    # get identity from plaid api
    # return json object

    # create client object
    client = plaid.Client(
        client_id=os.getenv('PLAID_CLIENT_ID'),
        secret=os.getenv('PLAID_SECRET'),
        environment=os.getenv('PLAID_ENV'),
        api_version='2020-09-14'
    )

    # get identity
    identity_response = client.Identity.get(access_token)

    # return json object
    return json.dumps(identity_response['accounts'][:2], indent=4, sort_keys=True)

# get income
def get_income(access_token):
    # get income from plaid api
    # return json object

    # create client object
    client = plaid.Client(
        client_id=os.getenv('PLAID_CLIENT_ID'),
        secret=os.getenv('PLAID_SECRET'),
        environment=os.getenv('PLAID_ENV'),
        api_version='2020-09-14'
    )

    # get income
    income_response = client.Income.get(access_token)

    # return json object
    return json.dumps(income_response['accounts'][:2], indent=4, sort_keys=True)
