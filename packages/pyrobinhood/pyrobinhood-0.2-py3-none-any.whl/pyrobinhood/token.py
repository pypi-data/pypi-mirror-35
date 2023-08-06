OAUTH_TOKEN_ENDPOINT = 'https://api.robinhood.com/oauth2/token/'


def post_refresh_token(request, client_id, refresh_token, timeout=15):
    res = request.post(
        OAUTH_TOKEN_ENDPOINT,
        json={
            'client_id': client_id,
            'refresh_token': refresh_token,
            "grant_type" : "refresh_token",
            "scope" : "web_limited"
        },
        timeout=timeout
    )
    res.raise_for_status()
    res = res.json()

    return res