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

# 1: weather_check.py
Download this file.
In the slack app, Create a new incoming Webhook. copy the webhook URL from the slack window & paste it in the script
```
    web_hook_url = <WEBHOOK URL>
```
Save the file & run the script from terminal.
Input any zipcode in USA. This program checks for the word **"Cloud"** in the weather description.
If there is Cloud in the description it will post a message in #general channel about the weather in the city for which you have entered the zipcode.
I have used a open source weather API, that is available online. I am concatinating the zipcode entered by user in the api link & getting the weather of that city. Then parsing the data returned by the api to read the weather & city name.

# 2: draw_slashcommand.py
Download this file & run it. On another terminal window run.
```
    ./ngrok http 5000.
```
There will be a https port address given in the terminal, copy this address & paste it in the slashcommand request url, concatinate it with **"/cards"**. in edit page of slashcommand.
The python file runs until stopped using ctrl+C. 
Now in slack channel use the slash command _/drawcard_ & press enter.
While typing the slashcommand auto complete option is available & there is a hint text shown as tool tip about the slashcommand.In the python file, channel id is read(to post the image in the right channel).
Online playing card API is used to draw a playing card randomly & insert it in the appropriate channel.

# 3: app_reaction.py
Download the files app_reaction.py, bot.py. Then execute:
```
    ./ngrok http 5000
```   
Then open another terminal do the following:
```
    export CLIENT_ID<client ID>
    export CLIENT_SECRET<client secret>
    export VERIFICATION_TOKEN<verification token> 
```
client Id, client secret & verification token is available in the "Events Subscriptions" page of the bot app added in slack workspace.Run  _app_reaction.py_ python script. Now Copy the ngrok url & paste it in the request url section concatinated by /listening. Slask App would send a challenge parameter, as soon as the end point responds with the challenge value, Green **Verified** is added to the request URL, indicating that the url is valid & verified by slack system.
  
