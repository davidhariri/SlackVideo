from flask_restful import Resource, reqparse


class OAuthChallengeRequests(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("challenge", type=str)

        args = parser.parse_args()

        return args["challenge"], 200
