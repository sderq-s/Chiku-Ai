import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# إعداد تسجيل الأخطاء
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# تخزين رصيد المستخدمين
user_balances = {}

# قائمة الكلمات
words = ["Boys", "Girls", "Cats", "Dogs", "Horses"]

# دالة لعرض الرصيد
def balance(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id
    balance = user_balances.get(user_id, 0)
    update.message.reply_text(f'Your balance is: {balance} stars')

# دالة لإعادة كتابة كلمة
def word_game(update: Update, context: CallbackContext):
    word_to_rewrite = words[0]  # يمكنك تغيير هذه الكلمة أو اختيارها عشوائيًا
    update.message.reply_text(f'Rewrite word and win stars: {word_to_rewrite}')

# دالة للتحقق من الكلمة المدخلة
def check_word(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id
    user_input = update.message.text
    
    if user_input in words:
        user_balances[user_id] = user_balances.get(user_id, 0) + 20
        update.message.reply_text('Nice, you win 20 stars.')
    else:
        update.message.reply_text('Try again!')

def main():
    # إدخال رمز التوكن الخاص بك هنا
    token = '7680410833:AAESNMhjnk__RSn1cwZB0Sj-4qMmqFfY3TU'
    
    updater = Updater(token)

    # إضافة المعالجات
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("balance", balance))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, check_word))
    dp.add_handler(CommandHandler("start", word_game))

    # بدء البوت
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
