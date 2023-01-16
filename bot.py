import logging
from getInfo import getData

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)
TOKEN = '5939028652:AAE9hFyIrdx0gQPoMTnasEzfNGKc0P2ZVfc'
data = [2]
# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!')

def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')
     
def echo(update, context):
    """Echo the user message."""
    update.message.reply_text(update.message.text)

def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def testinput(update, context):
    global data
    text = update.message.text
    if(text == "Arun" or text == "Wei yuan"):
        data[0] =text
        update.message.reply_text("Enter the fault description")
        return
    if(text == "Faulty pipe"):
        update.message.reply_text("Your name: " + data[0] + "/nFault reported: " + text)
        update.message.reply_text("Fault reported!\n We will contact you with updates")
        return
    print(text)
    answer = getData(text)
    print(answer)
    update.message.reply_text(answer)
        

def checklots(update, context):
    """Send a message when the command /checklots is issued."""
    update.message.reply_text("Input carpark id number: ")


def fault(update, context):
    update.message.reply_text("Fault Reporting\n Enter your name")

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
    dp.add_handler(CommandHandler("fault", fault))
    dp.add_handler(CommandHandler("checklots", checklots))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, testinput))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

if __name__ == '__main__':
    main()