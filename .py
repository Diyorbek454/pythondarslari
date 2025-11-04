import telebot
from telebot import types
from pymongo import MongoClient

# --- Bot sozlamalari ---
TOKEN = "7753018501:AAHsQuLGYRtHTImVvtVTLRRNwcLTz9MWfgc"
bot = telebot.TeleBot(TOKEN)

# Kanalga obuna bo‘lish shart
CHANNELS = ["@trent_kinola"]

# --- MongoDB ---
MONGO_URL = "mongodb+srv://dkenjayev134_db_user:yD6oFqzfSGxHrTwe@cluster0.va0aifh.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(MONGO_URL)
db = client["kinochi_bot"]
collection = db["videos"]

# --- Foydalanuvchini tekshirish ---
def check_user(user_id):
    for ch in CHANNELS:
        try:
            status = bot.get_chat_member(ch, user_id).status
            if status in ["left", "kicked"]:
                return False
        except Exception as e:
            print(f"Xatolik: {e}")
            return False
    return True

# --- Kanalga post qo‘shilganda saqlash ---
@bot.channel_post_handler(content_types=["video"])
def handle_channel_post(message):
    # ⚠️ Kanal username'ni to‘g‘ri kiriting (without @)
    if message.chat.username == "trent_kinola":
        collection.insert_one({
            "file_id": message.video.file_id,
            "caption": message.caption
        })
        print("✅ Video saqlandi MongoDB'ga!")
    else:
        print("❌ Noto‘g‘ri kanal:", message.chat.username)

# --- Obuna so‘rash ---
def ask_to_subscribe(chat_id):
    markup = types.InlineKeyboardMarkup()
    for ch in CHANNELS:
        markup.add(types.InlineKeyboardButton(text=ch, url=f"https://t.me/{ch[1:]}"))
    markup.add(types.InlineKeyboardButton("✅ Tekshirish", callback_data="check"))
    bot.send_message(chat_id, "Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling 👇", reply_markup=markup)

# --- /start komandasi ---
@bot.message_handler(commands=["start"])
def start(message):
    user_id = message.from_user.id
    if check_user(user_id):
        bot.send_message(message.chat.id, "✅ Botdan foydalanishingiz mumkin! Kodni yuboring (masalan: 1234)")
    else:
        ask_to_subscribe(message.chat.id)

# --- "Tekshirish" tugmasi ---
@bot.callback_query_handler(func=lambda call: call.data == "check")
def check_callback(call):
    user_id = call.from_user.id
    if check_user(user_id):
        bot.send_message(call.message.chat.id, "✅ Obuna tasdiqlandi! Endi kodni yuboring.")
    else:
        bot.send_message(call.message.chat.id, "❌ Hali ham barcha kanallarga obuna bo‘lmagansiz!")

# --- Kod yuborilganda video qidirish ---
@bot.message_handler(func=lambda message: True)
def all_messages(message):
    user_id = message.from_user.id
    if not check_user(user_id):
        ask_to_subscribe(message.chat.id)
        return

    if message.text.isdigit():
        kod = f"Kod: {message.text}"
        video = collection.find_one({"caption": {"$regex": kod}})
        if video:
            bot.send_video(message.chat.id, video["file_id"], caption=video["caption"])
        else:
            bot.send_message(message.chat.id, "❌ Bu kod bo‘yicha video topilmadi.")
    else:
        bot.send_message(message.chat.id, "❗ Kod raqam ko‘rinishida bo‘lishi kerak (masalan: 1234)")

bot.polling(none_stop=True)
