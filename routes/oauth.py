from flask_restful import Resource
from flask import redirect


class OAuthRequests(Resource):
    def get(self):
        return redirect(
            "https://github.com/davidhariri/SlackVideo/blob/master/README.md",
            code=302
        )
