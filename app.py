import flask
from flask import request
from authy.api import AuthyApiClient

app = flask.Flask(__name__)
token = 'SFGtP2w2kuBf494bSbmUaRCYeAdEcLHi'
authy_api = AuthyApiClient(token)

@app.route('/', methods = ['GET'])
def home():
    authy_id = str(request.args['authyid'])
    otp = str(request.args['otp'])
    try: 
        verification = authy_api.tokens.verify(authy_id, token=otp)
        return str(verification.ok())
    except:
        return  "Hello World"