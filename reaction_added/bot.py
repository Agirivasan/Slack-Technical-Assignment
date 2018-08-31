"""
Python Slack Bot class for use with the pythOnBoarding app
"""
import os
import message

from slackclient import SlackClient
import json


class Bot(object):
    """ Instanciates a Bot object to handle Slack onboarding interactions."""
    def __init__(self):
        super(Bot, self).__init__()
        self.name = "pythonboardingbot"
        self.emoji = ":robot_face:"
        # When we instantiate a new bot object, we can access the app
        # credentials we set earlier in our local development environment.
        self.oauth = {"client_id": os.environ.get("CLIENT_ID"),
                      "client_secret": os.environ.get("CLIENT_SECRET"),
                      # Scopes provide and limit permissions to what our app
                      # can access. It's important to use the most restricted
                      # scope that your app will need.
                      "scope": "bot"}
        self.verification = os.environ.get("VERIFICATION_TOKEN")

        # NOTE: Python-slack requires a client connection to generate
        # an oauth token. We can connect to the client without authenticating
        # by passing an empty string as a token and then reinstantiating the
        # client with a valid OAuth token once we have one.
        self.client = SlackClient("")
        # We'll use this dictionary to store the state of each message object.
        # In a production envrionment you'll likely want to store this more
        # persistantly in  a database.
        self.messages = {}

    def reaction_msg(self, channel_id,slack_reaction,user_id):
        # this function send the message to channel about the reaction added by user.
        slack_token = "xoxb-421491431014-423230183907-b7IXUHGk1oQnCXGTlYbJjoTQ"
        sc = SlackClient(slack_token)

        userobj = sc.api_call("users.info", token=slack_token, user=user_id)
        unames = userobj['user']['profile']['real_name']

        post_message = sc.api_call("chat.postMessage",
                                                channel=channel_id,
                                                username=self.name,
                                                icon_emoji=self.emoji,
                                                text=unames + " has reacted to a message with " + slack_reaction
                                                )
