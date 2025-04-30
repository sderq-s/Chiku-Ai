import random
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Bot Token
TOKEN = "7680410833:AAESNMhjnk__RSn1cwZB0Sj-4qMmqFfY3TU"

# Initialize the bot
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

# User balance
user_balance = {}

# List of random words
random_words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew"]

# Command to check balance
def balance(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    balance = user_balance.get(user_id, 0)
    update.message.reply_text(f"Your balance is: {balance} stars")

# Command to rewrite a word
def rewrite_word(update: Update, context: CallbackContext):
    word = random.choice(random_words)
    update.message.reply_text(f"Rewrite a word and win stars: {word}")

# Command to handle winning
def win(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    user_balance[user_id] = user_balance.get(user_id, 0) + 20
    update.message.reply_text("Done, you won 20 stars.")

# Command to transfer stars
def transfer(update: Update, context: CallbackContext):
    update.message.reply_text("Send a username so I send him stars.")

# Command to handle username for transfer
def handle_username(update: Update, context: CallbackContext):
    username = context.args[0] if context.args else None
    if username and username.isalnum():  # Simple validation for username
        update.message.reply_text("Done!")
    else:
        update.message.reply_text("Oops, Invalid username..")

# Command to handle specific questions
def handle_darlene(update: Update, context: CallbackContext):
    if context.args:
        question = " ".join(context.args)
        update.message.reply_text(f"Darlene, you asked: {question}")
    else:
        update.message.reply_text("Please provide a question after 'Darlene,'.")

# Command to handle /ask
def ask(update: Update, context: CallbackContext):
    if context.args:
        question = " ".join(context.args)
        update.message.reply_text(f"You asked: {question}")
    else:
        update.message.reply_text("Please provide a question after '/ask'.")

# Handlers
dispatcher.add_handler(CommandHandler("balance", balance))
dispatcher.add_handler(CommandHandler("rewrite", rewrite_word))
dispatcher.add_handler(CommandHandler("win", win))
dispatcher.add_handler(CommandHandler("transfer", transfer))
dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_username))
dispatcher.add_handler(MessageHandler(Filters.regex(r'^Darlene,'), handle_darlene))
dispatcher.add_handler(CommandHandler("ask", ask))

# Start the bot
updater.start_polling()
updater.idle()
