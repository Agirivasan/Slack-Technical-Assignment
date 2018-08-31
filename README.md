# Slack-Technical-Assignment
## Manual Qa-Technical Assignment
This project has 3 parts in it: 
1. Enter a zipcode in USA, to get the weather if it is going to rain or not. 
2. Use the slash-command /drawcard to draw a random playing card & post that in the slack channel. 
3. If someone reacts to a message in 1 channel there is a message posted on another stating that someone has reacted with <something> to the message in another channel.
  
# Pre-quisites:
install pip, slackclient, ngrok, flask, & python. Using following steps:

```
    pip install slackclient
    pip install ngrok
    pip install flask

```

Create slack app, events-api, incoming webhook, in slack web app.

# 1: weather_check.py
Download this file & run it.
Input any zipcode in USA. This program checks for the word "Cloud" in the weather description.
If there is Cloud in the description it will post a message in #general channel about the weather in the city for which you have entered the zipcode.
For this program I have used the API-Token of the channel using incoming web-hook from slack. 
I have used a open source weather API, that is available online. I am concatinating the zipcode entered by user in the api link & getting the weather of that city. Then parsing the data returned by the api to read the weather & city name.

# 2: draw_slashcommand.py
Download this file & run it. on another terminal window run the ./ngrok http 5000.
There will be a https port address given in the terminal, copy this address & paste this in the slashcommand request url concatinate it with "/cards". (slack basic info page)
The python file runs until stopped using ctrl+C. 
Now in slack channel use the slash command /drawcard & press enter.
In the python file, channel id is read.
Online playing card API is used to draw a playing card randomly & insert it in the channel where the slash command is used.

# 3: app_reaction.py
First execute ./ngrok http 5000, Then open another terminal do the following:
export CLIENT_ID<client ID>, export CLIENT_SECRET<client secret> & export VERIFICATION_TOKEN<verification token> from the basic info page in the bot settings.
  Now copy the ngrok url & paste it in the request url section concatinated by /listening
  
