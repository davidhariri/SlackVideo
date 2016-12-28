from flask_restful import Resource, reqparse
from providers import youtube

class SlackResponse(object):
	def __init__(self, text, video_url=None, video_title=None):
		self.text = text
		self.video_title = video_title
		self.video_url = video_url

	def to_dict(self):
		data = {
			"text" : self.text,
			"response_type" : "in_channel",
			"unfurl_media" : True,
			"unfurl_links" : True
		}

		if self.video_url:
			data["attachments"] = [
		        {
					"title" : self.video_title,
					"fallback": self.video_title,
					"color": "#e62116",
		            "title_link": self.video_url,
					"footer": "From YouTube"
				}
		    ]

		return data

class SlackRequests(Resource):
	def post(self):
		parser = reqparse.RequestParser()
		parser.add_argument("text", type=str)

		args = parser.parse_args()

		try:
			search = youtube.Search(**args)
			search.execute()
		except Exception as e:
			resp = SlackResponse("Sorry, I'm temporarily unavailable. Try me again in a few minutes")
			return resp.to_dict(), 200

		if len(search.results) == 0:
			resp = SlackResponse("Sorry, I couldn't find anything for '{}'".format(search.text))
			return resp.to_dict(), 200

		resp = SlackResponse("I found this!", video_url=search.results[0][0], video_title=search.results[0][1])
		return resp.to_dict(), 200