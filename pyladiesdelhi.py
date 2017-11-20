from telegram.ext import Updater,CommandHandler
from telegram import ChatAction
from datetime import datetime, timedelta
from pytz import timezone
from time import sleep
import logging,requests,pytz,re,ast

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)

updater=Updater(token='<Bot-Token>')
dispatcher=updater.dispatcher

print("I'm On..!!")

def start(bot, update, args):
        bot.sendChatAction(chat_id=update.message.chat_id, action=ChatAction.TYPING)
        sleep(0.2)
        bot.sendMessage(chat_id=update.message.chat_id,text='''
Hi! My powers are solely for the service of PyLadies Delhi Community
Use /help to get /help''')

def invitelink(bot,update):
        bot.sendChatAction(chat_id=update.message.chat_id, action=ChatAction.TYPING)
        sleep(0.2)
        bot.sendMessage(chat_id=update.message.chat_id, text='https://t.me/joinchat/C_ZAjhGaj0SshHl6woLvuA')

def twitter(bot,update):
        bot.sendChatAction(chat_id=update.message.chat_id, action=ChatAction.TYPING)
        sleep(0.2)
        bot.sendMessage(chat_id=update.message.chat_id, text='https://twitter.com/pyladiesDL')

def github(bot,update):
        bot.sendChatAction(chat_id=update.message.chat_id, action=ChatAction.TYPING)
        sleep(0.2)
        bot.sendMessage(chat_id=update.message.chat_id, text='https://github.com/PyLadiesDelhi')

def email(bot,update):
        bot.sendChatAction(chat_id=update.message.chat_id, action=ChatAction.TYPING)
        sleep(0.2)
        bot.sendMessage(chat_id=update.message.chat_id, text='delhi@pyladies.com')

def help(bot, update):
        bot.sendChatAction(chat_id=update.message.chat_id, action=ChatAction.TYPING)
        sleep(0.2)
        bot.sendMessage(chat_id=update.message.chat_id, text='''
Use one of the following commands
/invitelink - to get an invite link for PyLadies Delhi Telegram Group of Volunteers
/twitter - to get the twitter profile link of PyLadies Delhi
/github - to get github profile link of PyLadies Delhi
/email - to get email address in order to contact PyLadies Delhi
/help - to see recursion in action ;)

To contribute to|modify this bot : https://github.com/realslimshanky/PyLadiesDelhiBot
''')

dispatcher.add_handler(CommandHandler('start', start, pass_args=True))
dispatcher.add_handler(CommandHandler('invitelink', invitelink))
dispatcher.add_handler(CommandHandler('twitter', twitter))
dispatcher.add_handler(CommandHandler('github', github))
dispatcher.add_handler(CommandHandler('email', email))
dispatcher.add_handler(CommandHandler('help', help))
