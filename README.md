# Videos in Slack!
This is a simple API which you can spin up to support a slash-command bot on Slack for searching YouTube videos. You have two options:

## 1. Install directly to Slack
I deployed this to the Slack store so you can just install it to your team and use my own API. Hopefully YouTube doesn't rate limit us all!

<a href="https://slack.com/oauth/authorize?scope=incoming-webhook&client_id=97744058151.100606474326"><img alt="Add to Slack" height="40" width="139" src="https://platform.slack-edge.com/img/add_to_slack.png" srcset="https://platform.slack-edge.com/img/add_to_slack.png 1x, https://platform.slack-edge.com/img/add_to_slack@2x.png 2x"/></a>

## 2. DIY
The API is deployed using Heroku. All you have to do is make a *.env* file in the base of this project with contents like this:

```py
FLASK_DEBUG=True
YOUTUBE_API_KEY="your-google-youtube-api-key-here"
SLACK_VERIFY_TOKEN="your-slack-verify-token-here"
```

Once your server is up, you can use it by pointing a new Slack slash-command to `https://yourhost.com/`.

Don't forget to make an environment with virtualenv and install all requirements in requirements.txt. This app was built using Python 3.5.

Enjoy!