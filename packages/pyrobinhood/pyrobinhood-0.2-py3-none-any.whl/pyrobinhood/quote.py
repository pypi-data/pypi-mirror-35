QUOTE_ENDPOINT = 'https://api.robinhood.com/quotes/%s/'
HISTORICAL_ENDPOINT = 'https://api.robinhood.com/quotes/historicals/%s/'


def get_quote(request, symbol, timeout=15):
    url = QUOTE_ENDPOINT % symbol
    res = request.get(url, timeout=timeout)
    res.raise_for_status()
    res = res.json()

    return res

def get_historicals(request, symbol, interval, span, timeout=15):
    url = HISTORICAL_ENDPOINT % symbol
    res = request.get(url, params={'interval': interval, 'span': span}, timeout=timeout)
    res.raise_for_status()
    res = res.json()

    return res['historicals']