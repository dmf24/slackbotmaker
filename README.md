# slackbotmaker
Trivial, barebones framework for slackbot rtm client. 

It's one python file, `slackbotmaker.py` the rest are examples.

### To use:

1.  install the `slackclient` python package (`pip install slackclient`)
1.  define bot behavior in python scripts (optional, see "Actions files" below).
2.  create your bot with a python script that does the following:
  1.  import `rtm_runner` from `slackbotmaker`
  2.  Define your actions (or import them)
  3.  load your slack token into memory (sample script shows 3 ways to do it.  If you just copy and paste the string into the script, don't tell anyone you did that)
  4.  finish with a call to rtm_runner that passes your token as the sole argument.

### Actions files

To define actions, import the action function from slackbotmaker:

```Python
from slackbotmaker import action
```

Use it as a decorator for the action functions.  Action functions take two arguments, which are passed by rtm_runner.  The first argument is the instance of the slack client.  The second argument is a dictionary containing with the contents of the slack event.

This action will reply to any message with a response chosen randomly from a list

```Python
from slackbotmaker import action

@action
def obnoxious(slack_client, event):
    from random import choice
    if event.get('type', None) != 'message':
        return None
    channel=event.get('channel', None)
    if channel is not None:
        slack_client.rtm_send_message(channel, choice(["Yes!", "hmm", "oic", "mos def", "oh :("]))

```

### Running examples:


```
python samplebot.py <your slack API token>
```

This should enable the follwing interactions with the bot:

![slackbot-2](https://cloud.githubusercontent.com/assets/8546901/17352486/ce38502c-5904-11e6-972b-62d7faef88e9.png)

- Say: `ddg: slack help`
- Bot replies: `https://duckduckgo.com/?ia=web&q=slack+help`
- Say `upcase(this)`
- Reply: `THIS`
- Say `downcase(tHIS)`
- Reply: `this`
