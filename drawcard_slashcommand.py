# This program is to insert an image of random playing card,
# when slash command /draw is used in any channel in slack

import json
from flask import Flask, request, make_response, render_template, jsonify
import requests


app = Flask(__name__)


@app.route("/cards", methods=["GET", "POST"])
def hears():
    """
    This route listens for incoming events from Slack and uses the event
    handler helper function to route events to our Bot.
    """
    response = requests.get("https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1")
    data = response.json()
    
    isSuccess=data["success"]
    temp = json.dumps(isSuccess)

    if temp == "true":
        deckid = data["deck_id"]
    else:
        sys.exit("unable to process the request right now")
       
    response = requests.get("https://deckofcardsapi.com/api/deck/"+deckid+"/draw/?count=1")

    data2 = response.json()
    card_url = (data2["cards"][0]["images"]["png"])

    json.dumps(card_url)
  
    return jsonify(
        response_type='in_channel',
        text=card_url)
                                                             

if __name__ == '__main__':
    app.run(debug=True)
