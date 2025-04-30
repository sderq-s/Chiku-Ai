from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import logging
import random

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# User data storage
user_data = {}
# List of correct words for the game
words_list = ["Boys", "Girls", "Cats", "Dogs", "Stars", "Games"]

# Start command handler
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Welcome! Type "My balance" to check your stars or any word to play.')

# Balance command handler
def balance(update: Update, context: CallbackContext) -> None:
    user_id = update.message.from_user.id
    balance = user_data.get(user_id, 0)
    update.message.reply_text(f'Your balance is: {balance} stars')

# Message handler for words
def handle_message(update: Update, context: CallbackContext) -> None:
    user_id = update.message.from_user.id
    word = update.message.text.strip()

    if word.lower() == "my balance":
        balance(update, context)
    else:
        # Check if the provided word is in the list of correct words
        if word in words_list:
            user_data[user_id] = user_data.get(user_id, 0) + 20
            update.message.reply_text("Nice, you win 20 stars.")
        else:
            correct_word = random.choice(words_list)  # Randomly suggest a correct word
            update.message.reply_text(f'Rewrite word and win stars: {correct_word}')

def main() -> None:
    # Create the Updater and pass it your bot's token.
    updater = Updater("7680410833:AAESNMhjnk__RSn1cwZB0Sj-4qMmqFfY3TU")

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Register command handlers
    dispatcher.add_handler(CommandHandler("start", start))

    # Register message handler for all text messages in groups
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you send a signal to stop (Ctrl+C)
    updater.idle()

if __name__ == '__main__':
    main()
