import os
from apiclient.discovery import build


class Search(object):
    def __init__(self, text):
        self.text = text
        self.results = []

    def execute(self):
        youtube = build(
            "youtube",
            "v3",
            developerKey=os.environ.get("YOUTUBE_API_KEY")
        )

        api_response = youtube.search().list(
            q=self.text,
            type="video",
            part="id,snippet",
            maxResults=1,
            videoEmbeddable="true"
        ).execute()

        # Merge video ids
        for r in api_response.get("items", []):
            self.results.append((
                r["snippet"]["title"],
                "https://www.youtube.com/watch?v={}".format(r["id"]["videoId"])
            ))
