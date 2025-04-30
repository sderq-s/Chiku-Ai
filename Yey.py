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

# === بيانات البوت في الذاكرة ===
balances = {}            # user_id: balance
challenges = {}          # user_id: current_word
addresses = {}           # user_id: static address
address_to_user = {}     # address: user_id
pending_transfer = {}    # user_id: {"step": 1, "target": None}

WORDS_LIST = [
    "شجاع", "مبدع", "سريع", "صادق", "متميز",
    "متعاون", "مرن", "مبتكر", "حكيم", "مرح"
]

# === توليد عنوان ثابت للمستخدم ===
def generate_address(user_id: int) -> str:
    if user_id not in addresses:
        address = str(random.randint(1000000000, 9999999999))
        addresses[user_id] = address
        address_to_user[address] = user_id
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

# === "كلمات" ===
async def send_challenge(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    msg = update.message
    if msg.text == "كلمات":
        word = random.choice(WORDS_LIST)
        challenges[msg.from_user.id] = word
        await msg.reply_text(f"أعد إرسال الكلمة التالية للحصول على المزيد من النجوم: {word}")

# === التحقق من الكلمة ===
async def check_answer(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    msg = update.message
    user_id = msg.from_user.id
    text = msg.text.strip()

    if user_id in challenges and text == challenges[user_id]:
        balances[user_id] = balances.get(user_id, 0) + 20
        await msg.reply_text("تهانينا، لقد فزت بـ20 نجوم.")
        del challenges[user_id]

# === الرصيد ===
async def handle_balance(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    msg = update.message
    text = msg.text.strip()
    user_id = msg.from_user.id

    if text == "رصيدي":
        bal = balances.get(user_id, 0)
        await msg.reply_text(f"رصيدك: {bal} نجوم")

    elif text == "رصيده" and msg.reply_to_message:
        target = msg.reply_to_message.from_user
        bal = balances.get(target.id, 0)
        await msg.reply_text(f"رصيده: {bal} نجوم")

# === العنوان ===
async def handle_address(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.message.from_user.id
    address = generate_address(user_id)
    await update.message.reply_text(f"عنوانك الحالي: {address}")

# === إرسال النجوم ===
async def handle_transfer(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.message.from_user.id
    text = update.message.text.strip()

    if text == "إرسال":
        pending_transfer[user_id] = {"step": 1, "target": None}
        await update.message.reply_text("حسنا، للقيام بذلك؛ أرسلي عنوان رفيقك")
    elif user_id in pending_transfer:
        step = pending_transfer[user_id]["step"]

        # الخطوة 1: التحقق من العنوان
        if step == 1:
            if text in address_to_user:
                target_id = address_to_user[text]
                if target_id == user_id:
                    await update.message.reply_text("لا يمكنك إرسال النجوم لنفسك.")
                    del pending_transfer[user_id]
                    return
                pending_transfer[user_id]["target"] = target_id
                pending_transfer[user_id]["step"] = 2
                await update.message.reply_text("الٱن، ماهي كمية النجوم المراد إرسالها؟")
            else:
                await update.message.reply_text("مهلا، العنوان الذي أرسلته غير موجود.")
                del pending_transfer[user_id]

        # الخطوة 2: التحقق من الرصيد
        elif step == 2:
            try:
                amount = int(text)
                sender_balance = balances.get(user_id, 0)
                if amount <= 0:
                    raise ValueError

                if sender_balance == 0:
                    await update.message.reply_text("مهلا، ليس لديك رصيد للقيام بذلك..")
                elif sender_balance < amount:
                    await update.message.reply_text("رصيدك غير كافئ للقيام بهذه العملية..")
                else:
                    balances[user_id] = sender_balance - amount
                    receiver = pending_transfer[user_id]["target"]
                    balances[receiver] = balances.get(receiver, 0) + amount
                    await update.message.reply_text("تم إرسال النجوم بنجاح.")
            except ValueError:
                await update.message.reply_text("يرجى كتابة عدد صحيح للنجوم.")
            del pending_transfer[user_id]

def main() -> None:
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    # الأوامر بالنصوص داخل المجموعات فقط
    app.add_handler(MessageHandler(filters.TEXT & filters.ChatType.SUPERGROUP, send_challenge))
    app.add_handler(MessageHandler(filters.TEXT & filters.ChatType.SUPERGROUP, check_answer))
    app.add_handler(MessageHandler(filters.TEXT & filters.ChatType.SUPERGROUP, handle_balance))
    app.add_handler(MessageHandler(filters.TEXT & filters.ChatType.SUPERGROUP, handle_address))
    app.add_handler(MessageHandler(filters.TEXT & filters.ChatType.SUPERGROUP, handle_transfer))

    logger.info("البوت يعمل الآن...")
    app.run_polling()

if __name__ == "__main__":
    main()
