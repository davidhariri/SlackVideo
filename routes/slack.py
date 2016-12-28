from flask_restful import Resource, reqparse
from providers import youtube

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
		parser.add_argument("text", type=str)
		
		args = parser.parse_args()

		search = youtube.Search(**args)
		search.execute()

		resp = SlackResponse(video_url=search.results[0])

		return resp.to_dict(), 200