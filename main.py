import os
from flask import Flask
from flask_restful import Api
from routes.slack import SlackRequests
from routes.oauth import OAuthRequests

app = Flask(__name__)
api = Api(app)

api.add_resource(SlackRequests, "/")
api.add_resource(OAuthRequests, "/oauth/")

if __name__ == "__main__":
    app.run(debug=os.environ.get("FLASK_DEBUG", False))
