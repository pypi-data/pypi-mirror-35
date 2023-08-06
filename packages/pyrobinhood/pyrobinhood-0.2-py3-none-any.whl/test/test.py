import os
import time
import logging
import pytest
from pyrobinhood import PyRobinhood, AuthProvider


AUTH_DATA = {
    'username': os.environ['RB_USERNAME'],
    'password': os.environ['RB_PASSWORD'],
    'client_id': os.environ['RB_CLIENT_ID'],
    'access_token': 'foo'   # this will force to test refresh token logic
}

class TestAuthProvider(AuthProvider):
    def get_auth_data(self):
        return AUTH_DATA

    def update_auth_data(self, data):
        global AUTH_DATA
        AUTH_DATA = data

rb = PyRobinhood(TestAuthProvider(), logger=logging.getLogger('pyrobinhood'))

def test_general_http_methods():
    nonauth_url_path = '/instruments/dca63351-2a9c-4c57-b7dd-cfb3be9fd9c9/'
    res = rb.nonauth_get(nonauth_url_path)
    assert 'symbol' in res
    assert 'name' in res
    assert 'id' in res

    nonauth_full_url = 'https://api.robinhood.com/instruments/dca63351-2a9c-4c57-b7dd-cfb3be9fd9c9/'
    res = rb.nonauth_get(nonauth_full_url)
    assert 'symbol' in res
    assert 'name' in res
    assert 'id' in res

def test_get_instrument():
    # valid symbol
    res = rb.get_instrument('AAPL')
    assert 'id' in res
    assert 'symbol' in res
    assert res['symbol'] == 'AAPL'

    # invalid symbol
    with pytest.raises(Exception):
        rb.get_instrument('HAHAHA')

def test_get_quote():
    symbol = 'BABA'
    res = rb.get_quote(symbol)

    assert 'ask_price' in res
    assert 'ask_size' in res
    assert 'bid_price' in res
    assert 'bid_size' in res

def test_get_historicals():
    symbol = 'GE'
    res = rb.get_historicals(symbol)

    for h in res:
        assert "begins_at" in h
        assert "open_price" in h
        assert "close_price" in h
        assert "high_price" in h
        assert "low_price" in h
        assert "volume" in h

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

@pytest.mark.skipif('SKIP_RESET' in os.environ, reason='skip reset token')
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

def test_stock_order():
    # try to buy AAPL at $50
    symbol = 'AAPL'
    account = rb.get_accounts()[0]['url']
    instrument = rb.get_instrument(symbol)['url']

    order = rb.place_order(account, instrument, symbol, '50.00',
                           '1.0', 'buy')
    
    assert 'id' in order
    assert 'instrument' in order and order['instrument'] == instrument
    assert 'side' in order and order['side'] == 'buy'
    assert 'quantity' in order and float(order['quantity']) == 1

    # cancel that order
    order_id = order['id']
    rb.cancel_order(order_id)

    # confirm cancelled
    time.sleep(1)
    order = rb.get_order(order_id)
    assert 'state' in order and order['state'] == 'cancelled'

def test_options_order():
    # try to buy QQQ $170 CALL 2019-06-21 at $1.0
    leg = {
        'option': 'https://api.robinhood.com/options/instruments/c2021ed5-93dd-4387-9745-f990cf530bd6/',
        'position_effect': 'open',
        'side': 'buy',
        'ratio_quantity': 1
    }
    account = rb.get_accounts()[0]['url']

    order = rb.place_options_order(account, 'debit', leg, 1.00, 1, order_type='limit')

    assert 'id' in order
    assert 'chain_id' in order
    assert order['chain_symbol'] == 'QQQ'
    assert order['direction'] == 'debit'
    assert float(order['quantity']) == 1

    # cancel that order
    order_id = order['id']
    rb.cancel_options_order(order_id)

    # confirm cancelled
    time.sleep(1)
    order = rb.get_options_order(order_id)
    assert order['state'] == 'cancelled'
