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

CHOOSING, TYPING_REPLY, TYPING_CHOICE = range(3)

reply_keyboard = [['Balance', 'Format'],
                  ['BalanceAndFormat', '/start'],
                  ['New Input']]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)

#joiner
def facts_to_str(user_data):
    facts = list()

    for key, value in user_data.items():
        facts.append('{} - {}'.format(key, value))

    return "\n".join(facts).join(['\n', '\n'])


def start(update, context):
    update.message.reply_text(
        "Hi! My name is Doctor Botter. I will hold a more complex conversation with you. "
        "Why don't you tell me something about yourself?",
        reply_markup=markup)

    return CHOOSING


def regular_choice(update, context):
    text = update.message.text
    context.user_data['choice'] = text
    update.message.reply_text(
        'Your {}? Yes, I would love to hear about that!'.format(text.lower()))

    return TYPING_REPLY


def custom_choice(update, context):
    update.message.reply_text('Alright, please send me the category first, '
                              'for example "Most impressive skill"')

    return TYPING_CHOICE




def received_information(update, context):
    user_data = context.user_data
    text = update.message.text
    category = user_data['choice']
    user_data[category] = text
    del user_data['choice']

  #  update.message.reply_text("You entered: {}".format(facts_to_str(user_data)),
   #                           reply_markup=markup)
    reply_markup=markup                          
   # if (.format(facts_to_str(user_data))=='')
    my_string = format(facts_to_str(user_data))
    splitted = my_string.split()
    first = splitted[0]
    second = splitted[1]
    third = splitted[2]



    #Balance
    if (first =='Balance'):
        address_input = third
        i=1
        
        url = ("http://explorer.hacashpool.com/address/"+address_input)
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
    

    #format
    if (first=='Format'):
        hac_input = third
        sen =''.join(i for i in hac_input if i.isdigit())
        minimum = len(sen)
        if (sen!="" and minimum>=4):
            #kolah = float(sen)
            sen1 = int(sen)
            sr1 = sen[:-3]
            sr2 = int(sr1)
            #identifier
            identifier = abs(sen1)%1000
            if (identifier == 230):
                sr230Div = sr2/1000000000000000000
                hac_balance = sr230Div
            if (identifier == 231):
                sr231Div = sr2/100000000000000000
                hac_balance = sr231Div
            if (identifier == 232):
                sr232Div = sr2/10000000000000000
                hac_balance = sr232Div
            if (identifier == 233):
                sr233Div = sr2/1000000000000000
                hac_balance = sr233Div
            if (identifier == 234):
                sr234Div = sr2/100000000000000
                hac_balance = sr234Div
            if (identifier == 235):
                sr235Div = sr2/10000000000000
                hac_balance = sr235Div
            if (identifier == 236):
                sr236Div = sr2/1000000000000
                hac_balance = sr236Div
            if (identifier == 237):
                sr237Div = sr2/100000000000
                hac_balance = sr237Div
            if (identifier == 238):
                sr238Div = sr2/10000000000
                hac_balance = sr238Div
            if (identifier == 239):
                sr239Div = sr2/1000000000
                hac_balance = sr239Div
            if (identifier == 240):
                sr240Div = sr2/100000000
                hac_balance = sr240Div
            if (identifier == 241):
                sr241Div = sr2/10000000
                hac_balance = sr241Div
            if (identifier == 242):
                sr242Div = sr2/1000000
                hac_balance = sr242Div
            if (identifier == 243):
                sr243Div = sr2/100000
                hac_balance = sr243Div
            if (identifier == 244):
                sr244Div = sr2/10000
                hac_balance= sr244Div
            if (identifier == 245):
                sr245Div = sr2/1000
                hac_balance = sr245Div
            if (identifier == 246):
                sr246Div = sr2/100
                hac_balance = sr246Div
            if (identifier == 247):
                sr247Div = sr2/10
                hac_balance = sr247Div
            if (identifier == 248):
                sr248Div = sr2/1
                hac_balance = sr248Div
            if (identifier == 249):
                sr249Div = sr2*.1
                hac_balance = sr249Div
            if (identifier == 250):
                sr250Div = sr2/.01
                hac_balance = sr250Div
            if (identifier == 251):
                sr251Div = sr2/.001
                hac_balance = sr251Div
            if (identifier == 252):
                sr252Div = sr2/.0001
                hac_balance = sr252Div
            if (identifier == 253):
                sr253Div = sr2/.00001
                hac_balance = sr248Div
            if (identifier == 254):
                sr254Div = sr2/.000001
                hac_balance = sr254Div
            if (identifier == 255):
                sr255Div = sr2/.0000001
                hac_balance = sr255Div
            
            if(identifier<=255 and identifier>=230):
                #list   
                sr240Mul = int(hac_balance*100000000)
                sr241Mul = int(hac_balance*10000000)
                sr242Mul = int(hac_balance*1000000)
                sr243Mul = int(hac_balance*100000)
                sr244Mul = int(hac_balance*10000)
                sr245Mul = int(hac_balance*1000)
                sr246Mul = int(hac_balance*100)
                sr247Mul = int(hac_balance*10)
                sr248Mul = int(hac_balance*1)
                
                hb='{:.8f}'.format(hac_balance)
                #update.message.reply_text(print("..."))
                #print(f"Your {hac_input}is equivalent to:")
                update.message.reply_text('...')
                update.message.reply_text(f"""
                    
                Your {hac_input} HAC is equivalent to: 
                =================
                \u311c {hb} HAC
                \u311c {hb}:248
                =================
                \u311c {sr247Mul}:247
                \u311c {sr246Mul}:246
                \u311c {sr245Mul}:245
                \u311c {sr244Mul}:244
                \u311c {sr243Mul}:243
                \u311c {sr242Mul}:242
                \u311c {sr241Mul}:241
                \u311c {sr240Mul}:240

                """)
            else:
                update.message.reply_text("Please ONLY enter HAC format between 230 - 255")
        else:
                update.message.reply_text("Please ONLY enter HAC format between 230 - 255")



    #BalanceAndFormat
    if (first == 'BalanceAndFormat'):
        address_input = third
        i=1
        url = ("http://explorer.hacashpool.com/address/"+address_input)
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
        hac_balance_for_bandf = hac_balance
        


        #formatter
        
        hac_input = hac_balance
        sen =''.join(i for i in hac_input if i.isdigit())
        minimum = len(sen)
        if (sen!="" and minimum>=4):
            #kolah = float(sen)
            sen1 = int(sen)
            sr1 = sen[:-3]
            sr2 = int(sr1)
            #identifier
            identifier = abs(sen1)%1000
            if (identifier == 230):
                sr230Div = sr2/1000000000000000000
                hac_balance = sr230Div
            if (identifier == 231):
                sr231Div = sr2/100000000000000000
                hac_balance = sr231Div
            if (identifier == 232):
                sr232Div = sr2/10000000000000000
                hac_balance = sr232Div
            if (identifier == 233):
                sr233Div = sr2/1000000000000000
                hac_balance = sr233Div
            if (identifier == 234):
                sr234Div = sr2/100000000000000
                hac_balance = sr234Div
            if (identifier == 235):
                sr235Div = sr2/10000000000000
                hac_balance = sr235Div
            if (identifier == 236):
                sr236Div = sr2/1000000000000
                hac_balance = sr236Div
            if (identifier == 237):
                sr237Div = sr2/100000000000
                hac_balance = sr237Div
            if (identifier == 238):
                sr238Div = sr2/10000000000
                hac_balance = sr238Div
            if (identifier == 239):
                sr239Div = sr2/1000000000
                hac_balance = sr239Div
            if (identifier == 240):
                sr240Div = sr2/100000000
                hac_balance = sr240Div
            if (identifier == 241):
                sr241Div = sr2/10000000
                hac_balance = sr241Div
            if (identifier == 242):
                sr242Div = sr2/1000000
                hac_balance = sr242Div
            if (identifier == 243):
                sr243Div = sr2/100000
                hac_balance = sr243Div
            if (identifier == 244):
                sr244Div = sr2/10000
                hac_balance= sr244Div
            if (identifier == 245):
                sr245Div = sr2/1000
                hac_balance = sr245Div
            if (identifier == 246):
                sr246Div = sr2/100
                hac_balance = sr246Div
            if (identifier == 247):
                sr247Div = sr2/10
                hac_balance = sr247Div
            if (identifier == 248):
                sr248Div = sr2/1
                hac_balance = sr248Div
            if (identifier == 249):
                sr249Div = sr2*.1
                hac_balance = sr249Div
            if (identifier == 250):
                sr250Div = sr2/.01
                hac_balance = sr250Div
            if (identifier == 251):
                sr251Div = sr2/.001
                hac_balance = sr251Div
            if (identifier == 252):
                sr252Div = sr2/.0001
                hac_balance = sr252Div
            if (identifier == 253):
                sr253Div = sr2/.00001
                hac_balance = sr248Div
            if (identifier == 254):
                sr254Div = sr2/.000001
                hac_balance = sr254Div
            if (identifier == 255):
                sr255Div = sr2/.0000001
                hac_balance = sr255Div
            
            if(identifier<=255 and identifier>=230):
                #list   
                sr240Mul = int(hac_balance*100000000)
                sr241Mul = int(hac_balance*10000000)
                sr242Mul = int(hac_balance*1000000)
                sr243Mul = int(hac_balance*100000)
                sr244Mul = int(hac_balance*10000)
                sr245Mul = int(hac_balance*1000)
                sr246Mul = int(hac_balance*100)
                sr247Mul = int(hac_balance*10)
                sr248Mul = int(hac_balance*1)
                
                hb='{:.8f}'.format(hac_balance)
                #string/s to be removed
                r_items=["Index/Address"]
                hac_address_real = [x for x in hac_address.split() if x not in r_items]
                hac_address_real1 = ' '.join(hac_address_real)
                hac_address_real2 = 'Address '+hac_address_real1
                update.message.reply_text(f"""  
                {hac_address_real2}

                {hac_balance_for_bandf}
                {hacd_balance}
                =================
                \u311c {hb} HAC
                \u311c {hb}:248
                =================
                \u311c {sr247Mul}:247
                \u311c {sr246Mul}:246
                \u311c {sr245Mul}:245
                \u311c {sr244Mul}:244
                \u311c {sr243Mul}:243
                \u311c {sr242Mul}:242
                \u311c {sr241Mul}:241
                \u311c {sr240Mul}:240
                """)
            else:
                    update.message.reply_text("Address has no balance")
        else:
                update.message.reply_text("Address has no balance")
        
        
        
        
        
        
        
    user_data.clear()
    return CHOOSING










def done(update, context):
    user_data = context.user_data
    if 'choice' in user_data:
        del user_data['choice']

    update.message.reply_text("I learned these facts about you:"
                              "{}"
                              "Until next time!".format(facts_to_str(user_data)))

    user_data.clear()
    return ConversationHandler.END


def main():
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater("YOUR_TOKEN HERE PLEASE PUT YOUR TOKEN HERE FROM BOTFATHER WITH QUOTE , DONT REMOVE QUOTE", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Add conversation handler with the states CHOOSING, TYPING_CHOICE and TYPING_REPLY
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],

        states={#User choose what command and send
            CHOOSING: [MessageHandler(Filters.regex('^(Balance|Format|BalanceAndFormat)$'),
                                      regular_choice),
                       MessageHandler(Filters.regex('^Something else...$'),
                                      custom_choice)
                       ],

            TYPING_CHOICE: [# a prompt to enter the input.
                MessageHandler(Filters.text & ~(Filters.command | Filters.regex('^Done$')),
                               regular_choice)],

            TYPING_REPLY: [
                MessageHandler(Filters.text & ~(Filters.command | Filters.regex('^Done$')),
                               received_information)],
        },

        fallbacks=[MessageHandler(Filters.regex('^Done$'), done)]
    )

    dp.add_handler(conv_handler)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
