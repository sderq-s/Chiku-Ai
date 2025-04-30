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

# === البيانات ===
balances = {}
challenges = {}
addresses = {}
sending_state = {}

WORDS_LIST = [
    "شجاع", "مبدع", "سريع", "صادق", "متميز",
    "متعاون", "مرن", "مبتكر", "حكيم", "مرح"
]

# === إنشاء عنوان ثابت ===
def get_user_address(user_id):
    if user_id not in addresses:
        addresses[user_id] = ''.join(random.choices('0123456789', k=10))
    return addresses[user_id]

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

# === التحقق من التحدي ===
async def check_answer(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    msg = update.message
    user_id = msg.from_user.id
    text = msg.text.strip()
    if user_id in challenges and text == challenges[user_id]:
        balances[user_id] = balances.get(user_id, 0) + 20
        await msg.reply_text("تهانينا، لقد فزت بـ20 نجوم.")
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

# === أمر العنوان ===
async def handle_address(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.message.text == "عنواني":
        addr = get_user_address(update.message.from_user.id)
        await update.message.reply_text(f"عنوانك الحالي: {addr}")

# === أمر إرسال النجوم ===
async def handle_send(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.message.from_user.id
    text = update.message.text.strip()
    
    if text == "إرسال":
        sending_state[user_id] = {"step": "awaiting_address"}
        await update.message.reply_text("حسنا، للقيام بذلك؛ أرسلي عنوان رفيقك")
    elif user_id in sending_state:
        state = sending_state[user_id]
        
        if state["step"] == "awaiting_address":
            state["address"] = text
            state["step"] = "awaiting_amount"
            await update.message.reply_text("الٱن، ماهي كمية النجوم المراد إرسالها؟")
        elif state["step"] == "awaiting_amount":
            try:
                amount = int(text)
                if amount <= 0:
                    raise ValueError()
            except ValueError:
                await update.message.reply_text("الرجاء إدخال رقم صحيح.")
                return

            sender_balance = balances.get(user_id, 0)
            if sender_balance == 0:
                await update.message.reply_text("مهلا، ليس لديك رصيد للقيام بذلك..")
            elif sender_balance < amount:
                await update.message.reply_text("رصيدك غير كافئ للقيام بهذه العملية..")
            else:
                # البحث عن المستخدم الذي يملك هذا العنوان
                recipient_id = None
                for uid, addr in addresses.items():
                    if addr == state["address"]:
                        recipient_id = uid
                        break
                if recipient_id:
                    balances[user_id] -= amount
                    balances[recipient_id] = balances.get(recipient_id, 0) + amount
                    await update.message.reply_text("تم إرسال النجوم بنجاح!")
                else:
                    await update.message.reply_text("هذا العنوان غير موجود.")
            del sending_state[user_id]

# === main ===
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
