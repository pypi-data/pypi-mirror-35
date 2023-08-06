OPTIONS_CHAIN_ENDPOINT = 'https://api.robinhood.com/options/chains/'
OPTIONS_INSTRUMENT_ENDPOINT = 'https://api.robinhood.com/options/instruments/'
OPTIONS_DETAIL_ENDPOINT = 'https://api.robinhood.com/options/instruments/%s/'
OPTIONS_MARKETDATA_ENDPOINT = 'https://api.robinhood.com/marketdata/options/%s/'


def get_options_chains(request, instrument_id, timeout=15):
    res = request.get(
        OPTIONS_CHAIN_ENDPOINT, 
        params={'equity_instrument_ids': instrument_id}, 
        timeout=timeout)
    res.raise_for_status()
    res = res.json()

    return res['results']


def get_options_instrument(request, chain_id, expiration_date, option_type, state, tradability, timeout=15):
    res = request.get(
        OPTIONS_INSTRUMENT_ENDPOINT, 
        params={
            'chain_id': chain_id,
            'expiration_dates': expiration_date,
            'type': option_type,
            'state': state,
            'tradability': tradability
        }, 
        timeout=timeout)
    res.raise_for_status()
    res = res.json()
    return res['results']


def get_options_detail(request, options_instrument_id, timeout=15):
    endpoint = OPTIONS_DETAIL_ENDPOINT % options_instrument_id
    res = request.get(endpoint, timeout=timeout)
    res.raise_for_status()
    res = res.json()
    return res


def get_options_marketdata(request, options_instrument_id, timeout=15):
    endpoint = OPTIONS_MARKETDATA_ENDPOINT % options_instrument_id
    res = request.get(endpoint, timeout=timeout)
    res.raise_for_status()
    res = res.json()
    return res