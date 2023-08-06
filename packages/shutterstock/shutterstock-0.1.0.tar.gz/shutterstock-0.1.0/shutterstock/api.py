import json
import requests


class ShutterstockAPI:
    def __init__(self, token):
        self.token = token

    def get(self, endpoint, **params):
        headers = {
            'Content-Type': 'application/xml',
            'Authorization': 'Bearer {token}'.format(
                token=self.token
            )
        }

        endpoint = endpoint.format(**params)

        response = requests.get(
            'https://api.shutterstock.com/v2{endpoint}'.format(
                endpoint=endpoint
            ),
            params=params,
            headers=headers
        )

        return json.loads(response.content)
