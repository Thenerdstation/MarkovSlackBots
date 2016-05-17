import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__)))
from slackbot.bot import Bot
from slackbot.bot import respond_to
from slackbot.bot import listen_to
import re
from Donald.TheDonald import maga
import random

@listen_to(".*help.*")
def hi2(message):
    message.send(maga())

@respond_to(".*")
def hi(message):
    message.send(maga())

@respond_to(".*fuck.*")
def fuckyou(message):
    message.send("Hey @dan_walker, go fuck yourself.")

@respond_to(".*aidan.*")
def loverolls(message):
    message.send("http://i.imgur.com/dNVvntX.gif?noredirect")

@respond_to(".*maga.*")
def loverolls(message):
    message.send("/giphy " + random_word())

def main():
    bot = Bot()
    bot.run()

if __name__ == "__main__":
    main()
