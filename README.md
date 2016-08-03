# slackbotmaker
Trivial framework for slackbot rtm client

Initial attempt at a barebones framework for creating an rtm slackbot.

It's one python file, `slackbotmaker.py` the rest are examples.

To use these examples you must have your slack API token.

Then, you can run:

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
