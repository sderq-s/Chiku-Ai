import logging
import random
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes,
)

# === إعداد السجلات ===
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

# === توكن البوت ===
BOT_TOKEN = "7680410833:AAESNMhjnk__RSn1cwZB0Sj-4qMmqFfY3TU"

# === بيانات البوت (في الذاكرة) ===
balances = {}  # رصيد المستخدمين: { user_id: balance_int }
challenges = {}  # تحديات الكلمات الحالية: { user_id: current_word }
user_addresses = {}  # العناوين العشوائية للمستخدمين: { user_id: address }

# قائمة الكلمات العشوائية لأمر "كلمات"
WORDS_LIST = ["شجاع", "مبدع", "سريع", "صادق", "متميز", "متعاون", "مرن", "مبتكر", "حكيم", "مرح"]

# === /start ===
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "مرحباً! ⭐️\n"
        "أضفني كمشرف في مجموعتك ثم أرسل:\n"
        "- رصيدي\n"
        "- رصيده (رداً على رسالة أحد)\n"
        "- كلمات\n"
        "- عنواني\n"
        "- إرسال\n\n"
        "كل كلمة تعيد إرسالها تكسبك 20 نجمة!"
    )

# === أمر "كلمات" ===
async def send_challenge(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    msg = update.message
    if msg.text == "كلمات":
        word = random.choice(WORDS_LIST)
        challenges[msg.from_user.id] = word
        await msg.reply_text(f"أعد إرسال الكلمة التالية للحصول على المزيد من النجوم: {word}")

# === التحقق من إعادة إرسال الكلمة ===
async def check_answer(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    msg = update.message
    user_id = msg.from_user.id
    text = msg.text.strip()
    
    if user_id in challenges and text == challenges[user_id]:
        balances[user_id] = balances.get(user_id, 0) + 20
        await msg.reply_text("تهانينا، لقد فزت بـ20 نجوم!")
        del challenges[user_id]

# === أوامر الرصيد ===
async def handle_balance(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    msg = update.message
    text = msg.text.strip()
    
    if text == "رصيدي":
        bal = balances.get(msg.from_user.id, 0)
        await msg.reply_text(f"رصيدك: {bal} نجوم")
    
    elif text == "رصيده" and msg.reply_to_message:
        target = msg.reply_to_message.from_user
        bal = balances.get(target.id, 0)
        await msg.reply_text(f"رصيده: {bal} نجوم")

# === أمر "عنواني" ===
async def handle_address(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.message.from_user.id
    if user_id not in user_addresses:
        user_addresses[user_id] = str(random.randint(1000000000, 9999999999))
    await update.message.reply_text(f"عنوانك الحالي: {user_addresses[user_id]}")

# === أمر "إرسال" ===
async def handle_send(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.message.from_user.id
    text = update.message.text.strip()
    
    if text == "إرسال":
        await update.message.reply_text("حسناً، للقيام بذلك؛ أرسلي عنوان رفيقك")
        return
    
    if user_id in user_addresses:
        if text.isdigit():
            amount = int(text)
            if balances.get(user_id, 0) >= amount:
                balances[user_id] -= amount
                await update.message.reply_text("تم إرسال النجوم بنجاح!")
            else:
                await update.message.reply_text("رصيدك غير كافئ للقيام بهذه العملية..")
        else:
            await update.message.reply_text("الآن، ما هي كمية النجوم المراد إرسالها؟")
    else:
        await update.message.reply_text("مهلا، ليس لديك رصيد للقيام بذلك..")

def main() -> None:
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & filters.ChatType.SUPERGROUP, send_challenge))
    app.add_handler(MessageHandler(filters.TEXT & filters.ChatType.SUPERGROUP, check_answer))
    app.add_handler(MessageHandler(filters.TEXT & filters.ChatType.SUPERGROUP, handle_balance))
    app.add_handler(MessageHandler(filters.TEXT & filters.ChatType.SUPERGROUP, handle_address))
    app.add_handler(MessageHandler(filters.TEXT & filters.ChatType.SUPERGROUP, handle_send))

    logger.info("البوت يعمل الآن...")
    app.run_polling()

if __name__ == "__main__":
    main()
