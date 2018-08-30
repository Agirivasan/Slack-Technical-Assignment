from slackclient import SlackClient
import requests
import json
import sys

#Function to validate the zip code
def zipcode_validate(zipcode):
    if type(zipcode) != int:
        sys.exit("Invalid Zipcode")
    elif zipcode < 10001 or zipcode >= 99500:
        sys.exit("Invalid Zipcode")
    else:
        valid_zip = str(zipcode)
        return valid_zip


print "Enter any zipCode in USA : "
zipCode = input()

zipCode_str = zipcode_validate(zipCode)

response = requests.get("http://api.openweathermap.org/data/2.5/weather?zip="+zipCode_str+",us&APPID=f0babdd9a3780aed58102caf80819279")
data = response.json()
if json.dumps(data).find("404") > 0:
    sys.exit("invalid Zip code")

##Parcing cityname & weather report & storing in variables

weather = (data["weather"][0]["description"])
cityName = (data["name"])
temp = json.dumps(weather)

if temp.find("cloud") >0:
    slack_msg = {'text': 'It is cloudy in '+cityName+', Rain is expected. Try to stay indoors or Bring an Umbrella.'}
else:
    slack_msg = {'text': 'Weather is fine & Dandy in '+cityName+' have a great day'}

web_hook_url = 'https://hooks.slack.com/services/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'

requests.post(web_hook_url, data=json.dumps(slack_msg))

