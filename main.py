import os
from flask import Flask
from flask_restful import Api

app = Flask(__name__)
api = Api(app)

from routes.slack import SlackRequests

api.add_resource(SlackRequests, "/slack/")

if __name__ == "__main__":
    app.run(debug=os.environ.get("FLASK_DEBUG", False))
