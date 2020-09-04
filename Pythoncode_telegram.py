import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)







def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('This bot is in beta. More features will be added soon. This version supports conversion of HAC (avoid using decimals). Please contact @WARRENBUFFER if you want to help in developing.')
    update.message.reply_text('Enter your HAC balance: ')



def do_something(user_input):
    answer = user_input
    return answer
    
    

def reply(update, context):
    hac_input = update.message.text
    sen =''.join(i for i in hac_input if i.isdigit())
    sen1 = int(sen)
    sr1 = sen[:-3]
    sr2 = int(sr1)
	#identifier
    identifier = abs(sen1)%1000
    
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
 

   

def main():
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater("token", use_context=True)
    
    # Get the dispatcher to register handlers
    dp = updater.dispatcher
    
    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
   # dp.add_handler(CommandHandler("help", help))
   # dp.add_handler(CommandHandler("convert", convert))
    
    dp.add_handler(MessageHandler(Filters.text, reply))
    
    
    
    
    
    
    
    
     # Start the Bot
    updater.start_polling()
    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

if __name__ == '__main__':
    main()
