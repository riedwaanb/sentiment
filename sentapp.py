from flask import Flask, render_template
from flask import url_for, jsonify, request, abort
import sentiment
import os

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

SUBSCRIPTION_KEY = os.environ.get('SUBSCRIPTION_KEY')
API_URL = os.environ.get('API_URL')

@app.route('/', methods=['POST'])
def sentiment_analysis():
    data = request.get_json()
    if 'language' not in data:
        input_lang = 'en-US'
    else:
        input_lang = data['language']

    if 'text' not in data:
        print("No text provided to sentiment")
        abort(400) 

    input_text = data['text']

    response = sentiment.get_sentiment(input_text, input_lang, SUBSCRIPTION_KEY, API_URL)
    evalnum =  response['documents'][0]['score']

    print(str(evalnum))
    
    if 0.2 >= evalnum >= 0:
        answer = "VERY NEGATIVE"
    elif 0.4 >= evalnum > 0.2:
        answer = "NEGATIVE"
    elif 0.8 > evalnum >= 0.6:
        answer = "POSITIVE"
    elif 1 >= evalnum >= 0.8:
        answer = "VERY POSITIVE"
    else:
        answer = "NEUTRAL"
    return answer


if __name__ == "__main__":
    
    if SUBSCRIPTION_KEY:
        print("Using Subscription Key from Environment Variable: " + SUBSCRIPTION_KEY)
    else: 
        print("No Environment Variable SUBSCRIPTION_KEY set. Exiting")
        exit(1)

    if not API_URL:
       API_URL = "https://southafricanorth.api.cognitive.microsoft.com/text/analytics/v2.1/sentiment"
       print("No Environment Variable set for API_URL, using: " + API_URL)
    else:
       print("Using API URL from Environment Variable: " + API_URL)

    print("Ready to say check sentiment...\n")

    # Run Flask Application
    app.run(host="0.0.0.0", port=8088)
