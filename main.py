import os
from flask import Flask
from flask_restful import Api

app = Flask(__name__)
api = Api(app)

if __name__ == "__main__":
    app.run(debug=os.environ.get("FLASK_DEBUG", False))
