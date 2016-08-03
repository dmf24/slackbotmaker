from slackbotmaker import action
import sys
import logging
import re
from urllib import urlencode

ddg=re.compile(r'ddg: (.*)')

@action
def duckduckgo(sc, event):
    if event.get('type', None) != 'message':
        return None
    matches=re.search(ddg, event.get('text', ''))
    if matches == None:
        return None
    params=urlencode(dict(q=matches.groups()[0],
                          ia='web'))
    msg="https://duckduckgo.com/?%s" % params
    channel=event.get('channel', None)
    if channel is not None:
        logging.info("sending message to channel %s: %s\n" % (channel, msg))
        sc.rtm_send_message(channel, msg)

