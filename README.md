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

Clone this repo.
```
git clone https://github.com/aixdesign/slack-activity.git
```

As environment variable, set `SLACK_TOKEN` to bot user access token. If this token has been shared with you, please keep it safe and do not commit files with this token to repo!

In the code change the `DAYS` variable to desired range for analysis (either 30 or 45).

Run the code and if there are no errors, you should find your file in the `output` directory.