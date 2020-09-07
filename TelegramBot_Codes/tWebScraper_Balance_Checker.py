#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This program is dedicated to the public domain under the CC0 license.

"""
First, a few callback functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.
Usage:
Example of a bot-user conversation using ConversationHandler.
Send /start to initiate the conversation.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

import logging

from telegram import ReplyKeyboardMarkup
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                          ConversationHandler)

import requests
from bs4 import BeautifulSoup
# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('This bot is in beta. More features will be added soon. This version supports conversion of HAC (avoid using decimals). Please contact @contact if you want to help in developing.')
    update.message.reply_text('Enter your HAC address: ')

def reply(update, context):
	# 1. All websites are basically HTML/CSS and javascript
	# 2. We can use python to find whatever tags we are looking for.
	# 3. For pages that use a lot of javascript, we can  use web drivers instead to make the calls
	#https://towardsdatascience.com/how-to-scrape-any-website-with-python-and-beautiful-soup-bc84e95a3483

	

	address_input = update.message.text

	
	print(address_input)
	i=1
	url = ("http://block.hacash.org/address/"+address_input)
	result = requests.get(url)
	#print(result.content)
	src = result.content
	soup = BeautifulSoup(src, 'lxml')
	soup.find('p')

	contents= soup.findAll('p')
	for x in contents:
		if i == 1:
			hac_address = x.text
		if i == 2:
			hac_balance = x.text
		if i == 3:
			hacd_balance = x.text
		i = i+1
		if i==4:
			break
		
	#string/s to be removed
	r_items=["Index/Address"]
	hac_address_real = [x for x in hac_address.split() if x not in r_items]
	hac_address_real1 = ' '.join(hac_address_real)
	hac_address_real2 = 'Address '+hac_address_real1
	update.message.reply_text(f"""
	{hac_address_real2}
	{hac_balance}
	{hacd_balance}
	""")
	#print(hac_address_real2)
	#print(hac_balance)
	#print(hacd_balance)
    


   

def main():
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater("TOKEN DON'T REMOVE QUOTATION PUT HERE - TOKEN", use_context=True)
    
    # Get the dispatcher to register handlers
    dp = updater.dispatcher
    
    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text, reply))
   
    
    
    
    
    
    
    
    
     # Start the Bot
    updater.start_polling()
    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

if __name__ == '__main__':
    main()
