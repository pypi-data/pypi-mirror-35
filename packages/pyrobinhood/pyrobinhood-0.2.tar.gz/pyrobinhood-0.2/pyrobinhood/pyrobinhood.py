import logging
import urllib.parse

import requests

from .account import get_accounts, get_options_positions, get_positions
from .auth_provider import AuthProvider
from .authentication import login
from .instrument import get_instrument
from .options import (get_options_chains, get_options_detail,
                      get_options_instrument, get_options_marketdata)
from .order import (cancel_options_order, cancel_order, get_options_order,
                    get_order, place_options_order, place_order)
from .quote import get_historicals, get_quote
from .token import post_refresh_token

ROBINHOOD_BASE_URL = 'https://api.robinhood.com'


class PyRobinhood:

    def __init__(self, auth_provider, logger=None):
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
        self.auth_provider: AuthProvider = auth_provider

        if logger is None:
            self.logger = logging.getLogger('pyrobinhood')
            self.logger.setLevel('ERROR')
        else:
            self.logger = logger

        # init token credentials
        auth_data = auth_provider.get_auth_data()
        if 'access_token' in auth_data: 
            self.token = auth_data['access_token']
        else:
            self.__oauth_login__()

        self.__token_auth_failed = False
        self.__login_auth_failed = False

    def __non_auth_request__(self, method, *args, **kwargs):
        if 'authorization' in self.session.headers:
            del self.session.headers['authorization']
        return method(self.session, *args, **kwargs)

    def __oauth_login__(self):
        self.logger.debug('Trying OAuth login')
        auth_data = self.auth_provider.get_auth_data()
        credential = self.login(auth_data['username'], auth_data['password'], auth_data['client_id'])
        self.token = credential['access_token']

        # update auth data
        auth_data['access_token'] = credential['access_token']
        auth_data['refresh_token'] = credential['refresh_token']
        self.auth_provider.update_auth_data(auth_data)
        self.logger.debug('OAuth login OK')

    def __refresh_token__(self):
        try:
            self.logger.debug('Trying to refresh access token')
            refresh_token = self.auth_provider.get_auth_data()['refresh_token']
            client_id = self.auth_provider.get_auth_data()['client_id']
            res = post_refresh_token(self.session, client_id, refresh_token)
            self.token = res['access_token']

            # update auth data
            auth_data = self.auth_provider.get_auth_data()
            auth_data['access_token'] = res['access_token']
            auth_data['refresh_token'] = res['refresh_token']
            self.auth_provider.update_auth_data(auth_data)
            self.logger.debug('Refresh access token OK')
        except Exception:
            self.logger.debug('Refresh access token failed, fall back to oauth login')
            self.__oauth_login__()

    def __auth_request__(self, method, *args, **kwargs):
        try:
            self.session.headers.update(
                {'authorization': 'Bearer ' + self.token})
            res = method(self.session, *args, **kwargs)
            self.__token_auth_failed = False
            self.__login_auth_failed = False
            return res
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 401 or e.response.status_code == 403:
                self.logger.debug('Request auth failed')
                if not self.__token_auth_failed:
                    self.__token_auth_failed = True
                    self.__refresh_token__()
                    return self.__auth_request__(method, *args, **kwargs)
                elif not self.__login_auth_failed:
                    self.__login_auth_failed = True
                    self.__oauth_login__()
                    return self.__auth_request__(method, *args, **kwargs)
                else:
                    self.logger.error('ALL AUTH methods failed!')
                    raise e
            else:
                raise e

    ####### General HTTP methods #######

    def __get__(self, request, url, timeout=10):
        res = request.get(url, timeout=timeout)
        res.raise_for_status()
        res = res.json()
        return res

    def nonauth_get(self, url_path):
        if url_path.startswith(ROBINHOOD_BASE_URL):
            url = url_path
        else:
            url = urllib.parse.urljoin(ROBINHOOD_BASE_URL, url_path)

        return self.__non_auth_request__(self.__get__, url)

    def auth_get(self, url_path):
        if url_path.startswith(ROBINHOOD_BASE_URL):
            url = url_path
        else:
            url = urllib.parse.urljoin(ROBINHOOD_BASE_URL, url_path)

        return self.__auth_request__(self.__get__, url)

    ####### Instrument #######

    def get_instrument(self, symbol):
        return self.__non_auth_request__(get_instrument, symbol)

    ####### Authentication #######
    def login(self,
              username,
              password,
              client_id,
              grant_type='password',
              expires_in=86400,
              scope='internal',
              timeout=15):
        return self.__non_auth_request__(login, username, password, client_id, grant_type, expires_in, scope)

        ####### Quote #######
    def get_quote(self, symbol):
        return self.__non_auth_request__(get_quote, symbol)

    def get_historicals(self, symbol, interval='day', span='year'):
        return self.__non_auth_request__(get_historicals, symbol, interval, span)

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

    ####### Orders #######
    def get_order(self, order_id):
        return self.__auth_request__(get_order, order_id)

    def place_order(self,
                    account,
                    instrument,
                    symbol,
                    price,
                    quantity,
                    side,
                    order_type='market',
                    time_in_force='gfd',
                    trigger='immediate',
                    timeout=15):
        return self.__auth_request__(place_order,
                                     account, instrument, symbol,
                                     price, quantity, side, order_type,
                                     time_in_force, trigger)

    def cancel_order(self, order_id):
        return self.__auth_request__(cancel_order, order_id)

    def get_options_order(self, order_id):
        return self.__auth_request__(get_options_order, order_id)

    def place_options_order(self,
                            account,
                            direction,
                            leg,
                            price,
                            quantity,
                            order_type='market',
                            time_in_force='gfd',
                            trigger='immediate',
                            ref_id=None):
        return self.__auth_request__(place_options_order,
                                     account, direction, leg,
                                     price, quantity, order_type,
                                     time_in_force, trigger, ref_id)

    def cancel_options_order(self, order_id):
        return self.__auth_request__(cancel_options_order, order_id)
