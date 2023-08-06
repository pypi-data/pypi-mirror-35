import uuid


STOCK_ORDER_ENDPOINT = 'https://api.robinhood.com/orders/'
STOCK_ORDER_CANCEL_ENDPOINT = 'https://api.robinhood.com/orders/%s/cancel/'
OPTIONS_ORDER_ENDPOINT = 'https://api.robinhood.com/options/orders/'
OPTIONS_ORDER_CANCEL_ENDPOINT = 'https://api.robinhood.com/options/orders/%s/cancel/'

def get_order(request, order_id, timeout=5):
    url = '%s%s/' % (STOCK_ORDER_ENDPOINT, order_id)
    res = request.get(url, timeout=timeout)
    res.raise_for_status()
    res = res.json()

    return res

def place_order(request, 
                account, 
                instrument, 
                symbol, 
                price, 
                quantity,
                side, 
                order_type='market',
                time_in_force='gfd',
                trigger='immediate',
                timeout=5):
    order = {
        'account': account,
        'instrument': instrument,
        'symbol': symbol,
        'price': price,
        'quantity': quantity,
        'side': side,
        'type': order_type,
        'time_in_force': time_in_force,
        'trigger': trigger
    }

    res = request.post(STOCK_ORDER_ENDPOINT, json=order, timeout=timeout)
    res.raise_for_status()
    res = res.json()

    return res

def cancel_order(request, order_id, timeout=15):
    url = STOCK_ORDER_CANCEL_ENDPOINT % order_id
    res = request.post(url, timeout=timeout)
    res.raise_for_status()
    res = res.json()

    return res

def get_options_order(request, order_id, timeout=5):
    url = '%s%s/' % (OPTIONS_ORDER_ENDPOINT, order_id)
    res = request.get(url, timeout=timeout)
    res.raise_for_status()
    res = res.json()

    return res

def place_options_order(request, account, direction, leg, price, quantity, 
                        order_type='market', time_in_force='gfd', trigger='immediate', ref_id=None, timeout=15):
    if ref_id is None:
        ref_id = str(uuid.uuid4())

    order = {
        'account': account,
        'direction': direction,
        'legs': [leg],
        'price': price,
        'quantity': quantity,
        'type': order_type,
        'time_in_force': time_in_force,
        'trigger': trigger,
        'ref_id': ref_id
    }

    res = request.post(OPTIONS_ORDER_ENDPOINT, json=order, timeout=timeout)
    res.raise_for_status()
    res = res.json()

    return res

def cancel_options_order(request, order_id, timeout=15):
    url = OPTIONS_ORDER_CANCEL_ENDPOINT % order_id
    res = request.post(url, timeout=timeout)
    res.raise_for_status()
    res = res.json()

    return res
