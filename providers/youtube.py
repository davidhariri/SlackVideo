import os
from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser

class Search(object):
	def __init__(self, text):
		self.text = text
		self.results = []

	def execute(self):
		youtube = build("youtube", "v3", developerKey=os.environ.get("YOUTUBE_API_KEY"))

		api_response = youtube.search().list(
			q=self.text,
			type="video",
			part="id",
			maxResults=1
		).execute()

		# Merge video ids
		for r in api_response.get("items", []):
			self.results.append("https://www.youtube.com/watch?v={}".format(r["id"]["videoId"]))