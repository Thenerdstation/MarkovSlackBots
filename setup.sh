#!/bin/sh
pip install slackbot
touch Donald/slackbot_settings.py
echo "API_TOKEN = ### ADD YOUR TOKEN HERE ###" > Donald/slackbot_settings.py
touch Rick/slackbot_settings.py
echo "API_TOKEN = ### ADD YOUR TOKEN HERE ###" > Rick/slackbot_settings.py