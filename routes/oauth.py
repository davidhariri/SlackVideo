from flask_restful import Resource, reqparse
from flask import redirect


class OAuthRequests(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument("text", type=str)

        args = parser.parse_args()

        # Check the token from the requester
        if args.get("token", "") != os.environ.get("SLACK_VERIFY_TOKEN"):
            return "Invalid token", 400

        return redirect(
            "https://github.com/davidhariri/SlackVideo/blob/master/SUCCESS.md",
            code=302
        )
