#!/usr/bin/env python
from slackbotmaker import rtm_runner
import sample_actions
import duckduckgo_actions
import os
import sys

if len(sys.argv) > 1:
    token=sys.argv[1]
else:
    token=os.getenv('SLACKBOT_TOKEN')
    if token is None:
        tokenfile=os.path.join(os.getenv('HOME'), '.slackbot-token')
        if os.path.isfile(tokenfile):
            lines=[x.strip() for x in file(tokenfile).readlines() if x.strip() != '']
            if lines > 0:
                token=lines[0]

if __name__ == "__main__":
    rtm_runner(token)
