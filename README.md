# Slackbotmaker
Trivial, barebones framework for slackbot rtm client in python.  WIP use at your own risk.  Uses `slackclient` library.  Define actions using decorators, which registers them for a runner that runs the rtm bot.

### To use:

1.  Obtain a slack API token.  [This Tuturial is Helpful](https://www.fullstackpython.com/blog/build-first-slack-bot-python.html).  There's also the [slack docs on web authentication](https://api.slack.com/web#authentication)
1.  install the `slackbotmaker` python package (`pip install https://rc.hms.harvard.edu/dmf24/slackbotmaker-0.0.3.tar.gz`)
2.  create your bot with a python script that does the following:
  1.  import `rtm_runner` from `slackbotmaker`
  2.  Define your actions or import them.  [See below.](https://github.com/dmf24/slackbotmaker/blob/master/README.md#actions-files)
  3.  load your slack token into memory (sample script shows 3 ways to do it.  If you just copy and paste the string into the script, don't tell anyone you did that)
  4.  finish with a call to rtm_runner that passes your token as the sole argument.

### Actions

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

### Full Example

```Python
from slackbotmaker import action, rtm_runner
import sys

@action
def obnoxious(slack_client, event):
    from random import choice
    if event.get('type', None) != 'message':
        return None
    channel=event.get('channel', None)
    if channel is not None:
        slack_client.rtm_send_message(channel, choice(["Yes!", "hmm", "oic", "mos def", "oh :("]))

if __name__ == '__main__:
    if len(sys.argv) < 2:
        sys.stderr.write("Please specify a slack API bot token\n")
    else:
        rtm_runner(sys.argv[1])
```

### Running examples:

Clone the repository:

```
git clone https://github.com/dmf24/slackbotmaker.git
cd slackbotmaker
```

If you have already installed slackbotmaker, skip this step
```
python setup.py install
```
Change to the examples directory.
```
cd examples
```

Now you have 3 options, depending on how you store your slack API token.  Either an environment variable, a text file, or passed at the command line.
```
export SLACKBOT_TOKEN="your_slack_API_token"
python samplebot.py
```

```
echo "your_slack_API_token" > $HOME/.slackbot-token
python samplebot.py
```

```
python samplebot.py "your_slack_API_token"
```

This should enable the follwing interactions with the bot:

![slackbot-2](https://cloud.githubusercontent.com/assets/8546901/17352486/ce38502c-5904-11e6-972b-62d7faef88e9.png)

- Say: `ddg: slack help`
- Bot replies: `https://duckduckgo.com/?ia=web&q=slack+help`
- Say `upcase(this)`
- Reply: `THIS`
- Say `downcase(tHIS)`
- Reply: `this`
