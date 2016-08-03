import time
from slackclient import SlackClient
import logging

actions=[]

def action(action_function):
    actions.append(action_function)

def rtm_runner(token):
    sc=SlackClient(token)
    if sc.rtm_connect():
        while True:
            data=sc.rtm_read()
            for event in data:
                for a in actions:
                    a(sc, event)
            time.sleep(1)
    else:
        logging.error("Connection Failed")
