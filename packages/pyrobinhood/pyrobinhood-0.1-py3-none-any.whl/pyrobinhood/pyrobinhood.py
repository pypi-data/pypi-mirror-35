import requests
from .auth_provider import AuthProvider

from .instrument import get_instrument 
from .account import get_accounts, get_positions, get_options_positions
from .options import get_options_chains, get_options_instrument, get_options_detail, get_options_marketdata
from .token import post_refresh_token

class PyRobinhood:

    def __init__(self, auth_provider):
        self.session = requests.session()
        self.headers = {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "en;q=1, fr;q=0.9, de;q=0.8, ja;q=0.7, nl;q=0.6, it;q=0.5",
            "X-Robinhood-API-Version": "1.0.0",
            "Connection": "keep-alive",
            "User-Agent": "Robinhood/823 (iPhone; iOS 7.1.2; Scale/2.00)"
        }
        self.session.headers = self.headers
        self.auth_provider = auth_provider

        self.token = auth_provider.get_auth_data()['access_token']
        self.refresh_token = auth_provider.get_auth_data()['refresh_token']

        self.__auth_failed = False

    def __non_auth_request__(self, method, *args, **kwargs):
        if 'authorization' in self.session.headers:
            del self.session.headers['authorization']
        return method(self.session, *args, **kwargs)

    def __refresh_token__(self):
        refresh_token = self.auth_provider.get_auth_data()['refresh_token']
        client_id = self.auth_provider.get_auth_data()['client_id']
        res = post_refresh_token(self.session, client_id, refresh_token)

        self.token = res['access_token']
        res['client_id'] = client_id
        self.auth_provider.update_auth_data(res)

    def __auth_request__(self, method, *args, **kwargs):
        try:
            self.session.headers.update({ 'authorization': 'Bearer ' + self.token })
            res = method(self.session, *args, **kwargs)
            self.__auth_failed = False
            return res
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 401 and not self.__auth_failed:
                self.__auth_failed = True
                self.__refresh_token__()
                return self.__auth_request__(method, *args, **kwargs)
            else:
                raise e

    ####### Instrument #######
    def get_instrument(self, symbol):
        return self.__non_auth_request__(get_instrument, symbol)

    ####### Account #######
    def get_accounts(self):
        return self.__auth_request__(get_accounts)

    def get_positions(self, nonzero=True):
        return self.__auth_request__(get_positions, nonzero)

    def get_options_positions(self, nonzero=True):
        return self.__auth_request__(get_options_positions, nonzero)

    ####### Options #######
    def get_options_chains(self, instrument_id):
        return self.__non_auth_request__(get_options_chains, instrument_id)

    def get_options_instrument(self, chain_id, exp_date, option_type, state='active', tradability='tradable'):
        return self.__non_auth_request__(get_options_instrument, chain_id, exp_date, option_type, state, tradability)

    def get_options_detail(self, options_instrument_id):
        return self.__non_auth_request__(get_options_detail, options_instrument_id)

    def get_options_marketdata(self, options_instrument_id):
        return self.__auth_request__(get_options_marketdata, options_instrument_id)