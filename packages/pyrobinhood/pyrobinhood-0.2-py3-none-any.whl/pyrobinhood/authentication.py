OAUTH_TOKEN_ENDPOINT = "https://api.robinhood.com/oauth2/token/"


def login(request, 
          username, 
          password, 
          client_id, 
          grant_type='password', 
          expires_in=86400, 
          scope='internal',
          timeout=15):
    login_credentials = {
        'username': username,
        'password': password,
        'client_id': client_id,
        'grant_type': grant_type,
        'expires_in': expires_in,
        'scope': scope
    }

    res = request.post(OAUTH_TOKEN_ENDPOINT, json=login_credentials, timeout=timeout)
    res.raise_for_status()
    res = res.json()

    return res
