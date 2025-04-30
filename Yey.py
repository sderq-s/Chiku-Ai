import random
from pyrogram import Client, filters
import google.generativeai as genai

API_ID = 123456  # Replace with your API ID
API_HASH = "your_api_hash"  # Replace with your API HASH
BOT_TOKEN = "your_bot_token"

# Gemini setup
GEMINI_API_KEY = "AIzaSyCqsASbw2mXQLOmXI3eGGp3jGdF_wiW4W8"
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-pro")

app = Client("group_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# User data
user_balances = {}
word_game_active = False
current_word = ""

# Random word generator
def get_random_word():
    words = ["Tree", "River", "Lion", "Music", "Ocean", "Space", "Stone"]
    return random.choice(words)

# Handlers
@app.on_message(filters.command("start") & filters.private)
def start(_, msg):
    msg.reply("Bot is active in your group!")

@app.on_message(filters.text & filters.group)
def handle_message(_, msg):
    global word_game_active, current_word

    text = msg.text.lower()
    user_id = msg.from_user.id
    username = msg.from_user.username or f"user_{user_id}"

    # Initialize balance
    if username not in user_balances:
        user_balances[username] = 0

    # Word game trigger
    if "words" in text:
        current_word = get_random_word()
        word_game_active = True
        msg.reply(f"Rewrite a word and win stars: {current_word}")

    # Word win logic
    elif word_game_active and current_word.lower() in text:
        user_balances[username] += 20
        word_game_active = False
        msg.reply("Done, you won 20 stars.")

    # Balance check
    elif "my balance" in text:
        stars = user_balances.get(username, 0)
        msg.reply(f"Your balance is: {stars} stars")

    # Transfer
    elif "transfer" in text:
        msg.reply("Send a username so I send him stars.")
        app.set_parse_mode(None)
        app.set_state(chat_id=msg.chat.id, user_id=user_id, state="awaiting_username")

    elif app.get_state(chat_id=msg.chat.id, user_id=user_id) == "awaiting_username":
        target = text.replace("@", "").strip()
        if target in user_balances:
            user_balances[target] += 10
            msg.reply("Done!")
        else:
            msg.reply("Oops, Invalid username..")
        app.set_state(chat_id=msg.chat.id, user_id=user_id, state=None)

    # Gemini AI query
    elif text.startswith("darlene,") or text.startswith("/ask"):
        question = msg.text.replace("darlene,", "").replace("/ask", "").strip()
        if not question:
            msg.reply("Please ask something.")
            return
        try:
            reply = model.generate_content(question).text
            msg.reply(reply)
        except Exception as e:
            msg.reply("Error using AI.")

app.run()
