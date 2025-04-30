import telebot

token = "7299957663:AAEehpvWYSSsXwUd_GAhk6qpzSiIgfaIhDI"
bot = telebot.TeleBot(token)

@bot.message_handler(func=lambda m: True)
def rm(m):
    if m.text == "أهلا":
        bot.reply_to(m, "وسهلا، كيف حالك يا رفيقي؟")

@bot.message_handler(commands=['ban'])
def ban_user(message):
    if message.reply_to_message:
        try:
            bot.ban_chat_member(message.chat.id, message.reply_to_message.from_user.id)
            bot.send_message(message.chat.id, f"تم حظر {message.reply_to_message.from_user.first_name}")
        except Exception as e:
            bot.send_message(message.chat.id, f"حدث خطأ: {str(e)}")
    else:
        bot.send_message(message.chat.id, "يرجى الرد على رسالة المستخدم الذي تريد حظره.")

bot.infinity_polling()
