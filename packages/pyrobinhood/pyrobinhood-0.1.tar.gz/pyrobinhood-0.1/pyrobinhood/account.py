ACCOUNTS_ENDPOINT = 'https://api.robinhood.com/accounts/'
POSITION_ENDPOINT = 'https://api.robinhood.com/positions/'
OPTIONS_POSITION_ENDPOINT = 'https://api.robinhood.com/options/aggregate_positions/'


def get_accounts(request, timeout=15):
    res = request.get(ACCOUNTS_ENDPOINT, timeout=timeout)
    res.raise_for_status()
    res = res.json()

    return res['results']


def get_positions(request, nonzero, timeout=15):
    nonzero_str = 'true' if nonzero else 'false'
    res = request.get(POSITION_ENDPOINT, params={'nonzero': nonzero_str}, timeout=timeout)
    res.raise_for_status()
    res = res.json()

    return res['results']


def get_options_positions(request, nonzero, timeout=15):
    nonzero_str = 'true' if nonzero else 'false'
    res = request.get(
        OPTIONS_POSITION_ENDPOINT,
        params={'nonzero': nonzero_str},
        timeout=timeout)
    res.raise_for_status()
    res = res.json()

    return res['results']