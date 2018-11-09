# vanity-stargazer

Serverless API endpoint for those who need to power up their GitHub vanity star style.

<img width="430" alt="screen shot 2018-11-08 at 6 02 50 pm" src="https://user-images.githubusercontent.com/538171/48238656-992d4500-e380-11e8-853c-42a1355c10ff.png"> 

GitHub webhook [WatchEvents](https://developer.github.com/v3/activity/events/types/#watchevent) posted nicely to your Slack channel of choice


### Requirements

[NodeJS](https://nodejs.org/en/download/)
[Serverless](https://serverless.com/framework/docs/providers/aws/guide/installation/)
[serverless-python-requirements](https://www.npmjs.com/package/serverless-python-requirements)
[Docker](https://docs.docker.com/install/)

```
#Install serverless-python-requirements
npm install serverless-python-requirements
```

### Deploy stargazer

First go to your Slack account and get the webhook setup for your room you want to publish messages into
This will be a variable input for the serverless deployment

```
sls deploy --slack_webhook_url https://hooks.slack.com/services/T2P8JM69M/B6R0F2KJR/qsuperuniquehookid

Serverless: Generated requirements from /Users/myuser/src/stargazer/requirements.txt in /Users/myuser/src/stargazer/.serverless/requirements.txt...
Serverless: Installing requirements from /Users/myuser/src/stargazer/.serverless/requirements/requirements.txt ...
Serverless: Docker Image: lambci/lambda:build-python3.6
Serverless: Packaging service...
Serverless: Excluding development dependencies...
Serverless: Injecting required Python packages to package...
Serverless: Uploading CloudFormation file to S3...
Serverless: Uploading artifacts...
Serverless: Uploading service .zip file to S3 (2.9 MB)...
Serverless: Validating template...
Serverless: Updating Stack...
Serverless: Checking Stack update progress...
..............
Serverless: Stack update finished...
Service Information
service: stargazer
stage: dev
region: us-west-2
stack: stargazer-dev
api keys:
  None
endpoints:
  POST - https://XXXXXXXX.execute-api.us-west-2.amazonaws.com/dev/stargazer
functions:
  stargazer: stargazer-dev-stargazer
```

Take your new AWS Gateway endpoint output and apply to your Github webhook configuration. This can be done at a Github project or repository level.

<img width="799" alt="screen shot 2018-11-08 at 6 07 29 pm" src="https://user-images.githubusercontent.com/538171/48238872-7a7b7e00-e381-11e8-989a-9d26ae6c6b77.png">

Click the "Let me select individual events" option, then choose the "Watch" event at the bottom of the list.

<img width="745" alt="screen shot 2018-11-08 at 6 07 47 pm" src="https://user-images.githubusercontent.com/538171/48238862-70597f80-e381-11e8-8614-a4e4b083414c.png">
