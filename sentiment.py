import os, uuid, json
import requests        # needs sudo pip install requests

def get_sentiment(input_text, input_language, subscription_key, api_url):

    headers = {
        'Ocp-Apim-Subscription-Key': subscription_key,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }

    # You can pass more than one object in body.
    body = {
        'documents': [
            {
                'language': input_language,
                'id': '1',
                'text': input_text
            }
        ]
    }
    response = requests.post(api_url, headers=headers, json=body)
    return response.json()

