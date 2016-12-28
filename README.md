# YouTube 👉 Slack Bot
This is a simple API which you can spin up to support a slash-command bot on Slack for searching YouTube videos. You'll just need to provide an environment variable called `YOUTUBE_API_KEY` which should correspond to a YouTube Data API (v3) server-side access key. You can get this in your Google Developer Console.

Once your server is up, you can use it by pointing a new Slack slash-command to `https://yourhost.com/slack/`.

Don't forget to make an environment with virtualenv and install all requirements in requirements.txt. This app was built using Python 3.5, but I'm 99% sure it will work in Python 2.7.

Enjoy!