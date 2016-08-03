from slackbotmaker import action, onmessageinchannel
import sys
import logging
import re

upcaserx=re.compile(r'upcase\((.*)\)')
downcaserx=re.compile(r'downcase\((.*)\)')

#Basic action
@action
def uppercase(sc, event):
    if event.get('type', None) != 'message':
        return None
    matches=re.search(upcaserx, event.get('text', ''))
    if matches == None:
        return None
    msg=' '.join([x.upper() for x in matches.groups()])
    channel=event.get('channel', None)
    if channel is not None:
        logging.info("sending message to channel %s: %s\n" % (channel, msg))
        sc.rtm_send_message(channel, msg)

# Only runs when event type is 'message' and 'channel' is defined.
@onmessageinchannel
def downcase(sc, event):
    matches=re.search(downcaserx, event.get('text', ''))
    if matches == None:
        return None
    msg=' '.join([x.lower() for x in matches.groups()])
    logging.info("sending message to channel %s: %s\n" % (event['channel'], msg))
    sc.rtm_send_message(event['channel'], msg)    
