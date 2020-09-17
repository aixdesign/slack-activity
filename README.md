# slack-activity

This script is written for AIxDesign for administrative insights.
The purpose of this script is to analyze the Slack workspace and output a csv file with information on inactive members, based on a given time range. 

## Requirements
- Bot User OAuth Access Token (from ADA - internally developed app for workspace)

## How to use script

Install required packages into your working environment.
```
pip install requirements.txt
```

As environment variable, set `SLACK_TOKEN` to bot user access token. If this token has been shared with you, please keep it safe and do not commit files with this token to repo!

