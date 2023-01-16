import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CallbackQueryHandler, CommandHandler, MessageHandler, Filters
#import os
#PORT = int(os.environ.get('PORT', '5000'))

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)
TOKEN = '5939028652:AAE9hFyIrdx0gQPoMTnasEzfNGKc0P2ZVfc'

# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi! Hit "/" for available commands!')

def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')
     
def echo(update, context):
    """Echo the user message."""
    update.message.reply_text(update.message.text)

async def report(update, context):
    """Echo the user message."""
    keyboard = [
        [
            InlineKeyboardButton("Option 1", callback_data="1"),
            InlineKeyboardButton("Option 2", callback_data="2"),
        ],
        [InlineKeyboardButton("Option 3", callback_data="3")],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Please choose:", reply_markup=reply_markup)

async def button(update, context) -> None:
    """Parses the CallbackQuery and updates the message text."""
    query = update.callback_query

    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    await query.answer()

    await query.edit_message_text(text=f"Selected option: {query.data}")

def error(update, context):
    """Log Errors caused by Updates."""
    update.message.reply_text(update.message.text)

def fault(update, context):
    update.message.reply_text("Please state your name: ")
    userName = update.message.text
    if userName != "END":
        fault2
    
    # userName = update.message.text

    # update.message.reply_text("Please state your mobile number: ")
    # userNo = update.message.text
    # if userNo == "END":
    #     if endFault:
    #         return
    # update.message.reply_text("Please select type of fault: ")
    # userType = update.message.text
    # update.message.reply_text("Please give a brief description of the fault: ")
    # userDesc = update.message.text
    # update.message.reply_text("(Optional) Please upload a photo of the fault: ")
    # userPhoto = update.message.text
    # fullInfo = userName + userNo + userType + userDesc + userNo
    # update.message.reply_text(fullInfo)

def fault2(update, context):
    update.message.reply_text("Please state your mobile number: ")

def filterYES(self,message):
    return message.text == "YES" 
    

def endFault(update, context):
    update.message.reply_text("Discard fault report?")
    filterYES

def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CallbackQueryHandler(button))
    dp.add_handler(CommandHandler("report", report))

    dp.add_handler(CommandHandler("fault", fault))
    # on noncommand i.e message - echo the message on Telegram
    # dp.add_handler(MessageHandler(filterEND, endFault))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()
    #updater.start_webhook(
    #    listen="0.0.0.0",
    #    port=int(PORT),
    #    url_path=TOKEN,
    #    webhook_url='https://carparkcheckersg.herokuapp.com/' + TOKEN
    #)

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

if __name__ == '__main__':
    main()