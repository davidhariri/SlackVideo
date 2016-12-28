from flask_restful import Resource, reqparse

class SlackRequests(Resource):
	def post(self):
		parser = reqparse.RequestParser()

		# parser.add_argument("comment", type=str, help="'comment' should be a string")

		args = parser.parse_args()

		return "Hello World 👋", 200