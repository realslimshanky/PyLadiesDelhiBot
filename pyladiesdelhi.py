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

def help(bot, update):
	bot.sendChatAction(chat_id=update.message.chat_id, action=ChatAction.TYPING)
	sleep(0.2)
	bot.sendMessage(chat_id=update.message.chat_id, text='''
Use one of the following commands
/invitelink - to get an invite link for PyLadies Delhi Telegram Group of Volunteers
/help - to see recursion in action ;)

To contribute to|modify this bot : https://github.com/realslimshanky/PyLadiesDelhiBot
''')

dispatcher.add_handler(CommandHandler('start', start, pass_args=True))
dispatcher.add_handler(CommandHandler('invitelink', invitelink))
dispatcher.add_handler(CommandHandler('help', help))

updater.start_polling()
