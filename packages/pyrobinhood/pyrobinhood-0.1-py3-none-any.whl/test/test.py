import os
import pytest
from pyrobinhood import PyRobinhood, AuthProvider


AUTH_DATA = {
    'access_token': os.environ['RB_TOKEN'],
    'refresh_token': os.environ['RB_REFRESH_TOKEN'],
    'client_id': os.environ['RB_CLIENT_ID']
}

class TestAuthProvider(AuthProvider):
    def get_auth_data(self):
        return AUTH_DATA

    def update_auth_data(self, data):
        AUTH_DATA = data

rb = PyRobinhood(TestAuthProvider())

def test_get_instrument():
    # valid symbol
    res = rb.get_instrument('AAPL')
    assert 'id' in res
    assert 'symbol' in res
    assert res['symbol'] == 'AAPL'

    # invalid symbol
    with pytest.raises(Exception):
        rb.get_instrument('HAHAHA')


def test_get_accounts():
    res = rb.get_accounts()
    assert len(res) >= 1

def test_get_positions():
    res = rb.get_positions()
    for p in res:
        assert 'instrument' in p
        assert 'quantity' in p
        assert 'average_buy_price' in p

def test_get_options_positions():
    res = rb.get_options_positions()
    for p in res:
        assert 'id' in p
        assert 'chain' in p
        assert 'symbol' in p
        assert 'quantity' in p
        assert 'strategy' in p

## Access Token will be reset here

def test_refresh_token():
    old_token = rb.token
    rb.__refresh_token__()
    new_token = rb.token
    assert old_token != new_token

def test_get_options_chains():
    symbol = 'MSFT'
    instrument = rb.get_instrument(symbol)
    instrument_id = instrument['id']

    results = rb.get_options_chains(instrument_id)
    for res in results:
        assert 'symbol' in res
        assert 'expiration_dates' in res

    target_result = [res for res in results if res['symbol'] == symbol]
    assert len(target_result) == 1    

def test_get_options_instrument():
    symbol = 'QQQ'
    stock_instrument_id = rb.get_instrument(symbol)['id']
    chains = rb.get_options_chains(stock_instrument_id)
    chain = [res for res in chains if res['symbol'] == symbol][0]

    exp_date = chain['expiration_dates'][0]
    option_type = 'call'

    results = rb.get_options_instrument(chain['id'], exp_date, option_type)
    for res in results:
        assert 'chain_id' in res and res['chain_id'] == chain['id']
        assert 'chain_symbol' in res and res['chain_symbol'] == symbol
        assert 'type' in res and res['type'] == option_type
        assert 'tradability' in res and res['tradability'] == 'tradable'
        assert 'strike_price' in res
        assert 'id' in res

def __get_random_options(symbol, option_type):
    stock_instrument_id = rb.get_instrument(symbol)['id']
    chains = rb.get_options_chains(stock_instrument_id)
    chain = [res for res in chains if res['symbol'] == symbol][0]
    exp_date = chain['expiration_dates'][0]

    results = rb.get_options_instrument(chain['id'], exp_date, option_type)
    return results[0]['id'], exp_date

def test_get_options_detail():
    symbol = 'FB'
    option_type = 'call'
    options_instrument_id, exp_date = __get_random_options(symbol, option_type)
    res = rb.get_options_detail(options_instrument_id)
    assert 'chain_symbol' in res and res['chain_symbol'] == symbol
    assert 'expiration_date' in res and res['expiration_date'] == exp_date
    assert 'id' in res and res['id'] == options_instrument_id
    assert 'type' in res and res['type'] == option_type
    assert 'tradability' in res and res['tradability'] == 'tradable'

def test_get_options_marketdata():
    symbol = 'FB'
    option_type = 'call'
    options_instrument_id, _ = __get_random_options(symbol, option_type)
    res = rb.get_options_marketdata(options_instrument_id)
    assert 'ask_price' in res
    assert 'bid_price' in res
    assert 'volume' in res
    assert 'previous_close_price' in res
