INSTRUMENT_ENDPOINT = 'https://api.robinhood.com/instruments/'

def get_instrument(request, symbol, timeout=15):
    res = request.get(INSTRUMENT_ENDPOINT, params={'symbol': symbol}, timeout=timeout)
    res.raise_for_status()
    res = res.json()

    return res['results'][0]
