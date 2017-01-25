from flask_restful import Resource, reqparse
from providers import youtube


class SlackResponse(object):
    def __init__(self, text, video_url=None, video_title=None):
        self.text = text
        self.video_title = video_title
        self.video_url = video_url

    def to_dict(self):
        dict_data = {
            "text": self.text,
            "unfurl_media": True,
            "unfurl_links": True
        }

        if self.video_url is not None:
            dict_data["text"] += " {}".format(self.video_url)
            dict_data["response_type"] = "in_channel"
        else:
            dict_data["response_type"] = "ephemeral"

        return dict_data


class SlackRequests(Resource):
    def get(self):
        return "🏄", 200

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("text", type=str)

        args = parser.parse_args()

        try:
            search = youtube.Search(**args)
            search.execute()
        except Exception:
            resp = SlackResponse(
                "I'm temporarily unavailable. Try me again in a few minutes"
            )

            return resp.to_dict(), 200

        if len(search.results) == 0:
            resp = SlackResponse(
                "I couldn't find anything for '{}'".format(search.text)
            )

            return resp.to_dict(), 200

        resp = SlackResponse(
            "I found this!",
            video_url=search.results[0][1],
            video_title=search.results[0][0]
        )

        return resp.to_dict(), 200
