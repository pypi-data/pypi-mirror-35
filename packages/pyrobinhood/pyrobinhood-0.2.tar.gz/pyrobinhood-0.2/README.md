# pyrobinhood
A robinhood client for python

# Test
- Login to robinhood in your browser and grab your bearer token from any request.
- `> pip install -r requirements.txt`
- `> export RB_USERNAME={your_username}`
- `> export RB_PASSWORD={your_password}`
- `> export RB_CLIENT_ID={your_client_id}`
    - You can find the `client_id` from a login request in your browser
- `> make test`
