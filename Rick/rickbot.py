from slackbot.bot import Bot
from slackbot.bot import respond_to
from slackbot.bot import listen_to
import re
from Rick.rick import morty
import random

@respond_to(".*")
def hi(message):
    message.send(morty)

def main():
    bot = Bot()
    bot.run()

if __name__ == "__main__":
    main()