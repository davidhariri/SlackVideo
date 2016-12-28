from flask_restful import Resource, reqparse

class SlackResponse(object):
	def __init__(self, video_url):
		self.video_url = video_url

	def to_dict(self):
		return dict(
			text=self.video_url
		)

class SlackRequests(Resource):
	def post(self):
		parser = reqparse.RequestParser()

		# parser.add_argument("comment", type=str, help="'comment' should be a string")

		args = parser.parse_args()

		resp = SlackResponse("Hello World")

		return resp.to_dict(), 200