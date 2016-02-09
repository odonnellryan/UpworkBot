from flask import Flask
from flask.ext.admin import Admin
import requests
import oauth2
from urllib import parse
from config import key, secret, endpoint

app = Flask(__name__)
app.debug = True
admin = Admin(app)

def get_token():
    oauth_token = oauth2.Token(key, secret)
    response = requests.post(parse.urljoin(endpoint, '/api/auth/v1/oauth/token/request'))
    return response

@app.route('/')
def gather_data():
    print(get_token().content)
    return 'stuff'

if __name__ == '__main__':
    app.run()