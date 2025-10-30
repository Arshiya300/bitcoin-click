import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo

TOKEN = "8208656135:AAFYq1bxPNcLsPMmnRM2_OartB_9CLLunqI"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    webapp_btn = KeyboardButton(
        text="ورود به وب‌اپ سایت",
        web_app=WebAppInfo(url="https://coin-rush-e95c8d69.base44.app")
    )
    markup.add(webapp_btn)
    welcome_text = (
        "سلام! به ربات ایدراپ بیت‌کوین خوش آمدید 🌟\n"
        "برای اطلاعات بیشتر و شرکت در ایردراپ از دکمه زیر استفاده کنید.\n"
        "همچنین عضو کانال تلگرام ما شوید:\n"
        "📢 https://t.me/airdropBitcoin10"
    )
    bot.send_message(message.chat.id, welcome_text, reply_markup=markup)

bot.polling()