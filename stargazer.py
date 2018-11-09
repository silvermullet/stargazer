import json
import os
import requests

WEBHOOK_URL = os.environ['WEBHOOK_URL']


def stargazer(event, context):
    """Stargazer event handler, process WatchEvent from Github and post to Slack webhook"""

    message_body = json.loads(event['body'])

    repo = message_body['repository']['name']
    stars = message_body['repository']['stargazers_count']
    username = message_body['sender']['login']
    url = message_body['sender']['html_url']

    slack_post_data = { 'text': f"""
    New Github star for _{repo}_ repo!.,
    The *{repo}* repo now has *{stars}* stars! :tada:.,
    Your new fan is <{url}|{username}>"""
    }

    try:
        r = requests.post(
            WEBHOOK_URL,
            json=slack_post_data,
            headers={'Content-Type': 'application/json'}
        )
        return {
            'request-return-code': r.status_code
        }
    except requests.exceptions.RequestException as err:
        err_message = f'RequestException: {err}'
        return {
            'error': err_message
        }
