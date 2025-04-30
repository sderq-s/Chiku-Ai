from pyrogram import Client, filters
from pyrogram.types import Message
import random
import json
import os
import requests

API_ID = 21613960
API_HASH = "7a3c0a16230bb95af0b80403e81d0b7b"
BOT_TOKEN = "7680410833:AAESNMhjnk__RSn1cwZB0Sj-4qMmqFfY3TU"
GEMINI_API_KEY = "AIzaSyCqsASbw2mXQLOmXI3eGGp3jGdF_wiW4W8"
DATA_FILE = "user_data.json"

app = Client("star_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Load or initialize user data
if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "r") as f:
        users = json.load(f)
else:
    users = {}

current_word = None

def save_data():
    with open(DATA_FILE, "w") as f:
        json.dump(users, f)

def get_balance(user_id):
    return users.get(str(user_id), {}).get("stars", 0)

def add_stars(user_id, amount):
    uid = str(user_id)
    if uid not in users:
        users[uid] = {"stars": 0}
    users[uid]["stars"] += amount
    save_data()

def set_transfer_target(chat_id, target_username):
    users[str(chat_id)]["transfer_target"] = target_username
    save_data()

def get_transfer_target(chat_id):
    return users.get(str(chat_id), {}).get("transfer_target")

@app.on_message(filters.text & filters.group)
async def handle_messages(client, message: Message):
    global current_word
    user_id = message.from_user.id
    text = message.text.strip()

    # Word Game Trigger
    if text.lower() == "words":
        current_word = random.choice(["Sky", "Apple", "Dream", "Python", "Book"])
        await message.reply(f"Rewrite a word and win stars: {current_word}")
    
    # Winning the word game
    elif current_word and text == current_word:
        add_stars(user_id, 20)
        await message.reply("Done, you won 20 stars.")
        current_word = None

    # Check balance
    elif "رصيدي" in text or text.lower() == "my balance":
        stars = get_balance(user_id)
        await message.reply(f"Your balance is: {stars} stars")

    # Star transfer start
    elif text.lower() == "transfer":
        if str(message.chat.id) not in users:
            users[str(message.chat.id)] = {}
        set_transfer_target(message.chat.id, None)
        await message.reply("Send a username so I send him stars.")

    # Receive username for transfer
    elif get_transfer_target(message.chat.id) is None and text.startswith("@"):
        recipient = text[1:]
        target_user = None

        for uid, info in users.items():
            if info.get("username", "").lower() == recipient.lower():
                target_user = uid
                break

        if target_user:
            add_stars(target_user, 10)
            await message.reply("Done!")
        else:
            await message.reply("Oops, Invalid username..")
        set_transfer_target(message.chat.id, None)

    # Gemini AI Q&A
    elif text.startswith("Darlene, ") or text.startswith("/ask "):
        query = text.replace("Darlene, ", "").replace("/ask ", "")
        reply = gemini_response(query)
        await message.reply(reply)

    # Store username if available
    if message.from_user.username:
        uid = str(user_id)
        if uid not in users:
            users[uid] = {}
        users[uid]["username"] = message.from_user.username
        save_data()

def gemini_response(prompt):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={GEMINI_API_KEY}"
    headers = {"Content-Type": "application/json"}
    data = {
        "contents": [
            {
                "parts": [{"text": prompt}]
            }
        ]
    }
    try:
        res = requests.post(url, headers=headers, json=data)
        output = res.json()
        return output['candidates'][0]['content']['parts'][0]['text']
    except Exception:
        return "Sorry, I couldn't answer that."

app.run()
