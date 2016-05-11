from slackbot.bot import Bot
from slackbot.bot import respond_to
from slackbot.bot import listen_to
import re
from TheDonald import maga, random_word
import random
height = 30
@respond_to(".*")
def hi(message):
    global height
    num = random.random()
    if num < .333:
        height +=10
        response = "Well that wall just got 10 feet higher. Current height of the wall is %d feet" % height
        print response
        message.send(response)
    else:
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