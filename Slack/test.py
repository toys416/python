import requests
import json

web_hook_url='https://hooks.slack.com/services/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'
slack_msg={'text':'This is a message from python!!!!\n The second line'}
attach={
    "attachments": [
        {
            "fallback": "Required plain-text summary of the attachment.",
            "color": "#36a64f",
            "pretext": "Optional text that appears above the attachment block",
            "author_name": "Wang Jingzhou",
            "title": "Slack API Documentation",
            "title_link": "https://api.slack.com/",
            "text": "Optional text that appears within the attachment",
            "fields": [
                {
                    "title": "Priority",
                    "value": "High"
                },
                {
                    "title": "Componect",
                    "value": "UI"
                }
            ],
            "image_url": "http://my-website.com/path/to/image.jpg",
            "thumb_url": "http://example.com/path/to/thumb.png",
            "footer": "Slack API",
            "footer_icon": "https://platform.slack-edge.com/img/default_application_icon.png",
            "ts": 245456111
        }
    ]
}

requests.post(web_hook_url,data=json.dumps(attach))
