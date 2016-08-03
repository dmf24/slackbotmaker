import time
from slackclient import SlackClient
import logging
import sys

actions=[]

def action(action_function):
    actions.append(action_function)

def onmessageinchannel(action_function):
    def afwrapper(sc, event):
        if event.get('type', None) != 'message':
            return None
        channel=event.get('channel', None)
        if channel is None:
            return None
        action_function(sc, event)
    actions.append(afwrapper)

def rtm_runner(token):
    sc=SlackClient(token)
    if sc.rtm_connect():
        logging.info("Rtm session established")
        while True:
            data=sc.rtm_read()
            for event in data:
                for a in actions:
                    try: 
                        a(sc, event)
                    except KeyboardInterrupt:
                        raise
                    except:
                        logging.error(sys.exc_info())
            time.sleep(1)
    else:
        logging.error("Connection Failed")
