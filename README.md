# edie-slack
Meet Edie, Eliza's younger, hipper, psychobabble-friendly successor. She makes a great Slackbot.

## Background
Edie's is Slack's Python-based [real-time messaging bot](https://github.com/slackhq/python-rtmbot) wrapped around  Daniel Connelly's [Python implementation of Peter Norvig's *Paradigms of AI Programming* Eliza](https://github.com/dhconnelly/paip-python). 

... with updated diction. Loads has changed since 1991, and she seemed a little standoff-ish – which also led to her new, hip name.

The langauge updates rendered her internals less elegant, but I think – hope – they make Edie more fun than Eliza ever would've been.

## Running Edie
Edie should be run, for the most part, as Slack [instructs](http://github.com/slackhq/python-rtmbot):

### Dependencies
* [websocket-client](https://pypi.python.org/pypi/websocket-client/)
* [python-slackclient](https://github.com/slackhq/python-slackclient)

### Installation
1. Download Edie

  ````
  git clone git@github.com:christinac/edie-slack.git
  cd edie-slack
  ````

2. Install dependencies (With virtualenv if you're doing things correctly.)

  ````
  pip install -r requirements.txt
  ````

3. Configure rtmbot (Slack instructions [here](https://api.slack.com/bot-users))

  ````
  cp example-config/rtmbot.conf .
  vi rtmbot.conf
  SLACK_TOKEN: "xoxb-11111111111-222222222222222"
  ````

4. Run her!

````
  python rtmbot.py
````

## Edie in action
![Edie in action](http://i.imgur.com/DImoAqa.png)
