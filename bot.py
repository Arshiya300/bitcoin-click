import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
import os

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# 🔑 تنظیمات - توکن و لینک‌ها رو اینجا بذار
TOKEN = "8208656135:AAFYq1bxPNcLsPMmnRM2_OartB_9CLLunqI"
GAME_URL = "https://your-app-url.com"  # ⬅️ لینک بازی
CHANNEL_URL = "https://t.me/airdropBitcoin10"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    user_name = user.first_name
    welcome_message = f"""
🎮 **سلام {user_name} عزیز!**

به **سکه شتاب** خوش اومدی! 🚀

🎁 **هدیه ورود:**
• ۱۰۰۰ سکه رایگان!
• انرژی کامل برای شروع!

💰 **چطور بازی کنم؟**
• روی سکه کلیک کن = امتیاز بگیر
• تسک‌ها رو انجام بده = پاداش بگیر
• دوستات رو دعوت کن = ۵۰۰۰ سکه!

🏆 **ویژگی‌ها:**
✅ سیستم سطح و لیگ
✅ لیدربورد Real-time
✅ پاداش‌های پله‌ای اتوماتیک
✅ فروشگاه و بوستر
✅ جایزه روزانه

📢 **برای آخرین اخبار به کانال ما بپیوندید!**

📱 **آماده‌ای؟ بریم!** 👇
"""
    keyboard = [
        [InlineKeyboardButton("🎮 شروع بازی", url=GAME_URL)],
        [InlineKeyboardButton("📢 عضویت در کانال", url=CHANNEL_URL)],
        [InlineKeyboardButton("👥 دعوت دوستان", callback_data="invite"), InlineKeyboardButton("💰 موجودی", callback_data="balance")],
        [InlineKeyboardButton("🏆 لیدربورد", callback_data="leaderboard"), InlineKeyboardButton("❓ راهنما", callback_data="help")]
    ]
    await update.message.reply_text(welcome_message, parse_mode='Markdown', reply_markup=InlineKeyboardMarkup(keyboard))
    logger.info(f"User {user_name} ({user.id}) started the bot")

async def invite_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    invite_link = f"{GAME_URL}?ref__={user.id}"
    message = f"""
👥 **دعوت از دوستان**

🎁 برای هر دوست:
• **۵۰۰۰ سکه** به شما! (اتوماتیک)
• **۱۰۰۰ سکه** به دوستتون!

🏆 **پاداش‌های پله‌ای (اتوماتیک):**
• ۱ دعوت = ۵,۰۰۰ سکه 🎁
• ۳ دعوت = ۲۰,۰۰۰ سکه 🌟
• ۵ دعوت = ۳۵,۰۰۰ سکه 💎
• ۱۰ دعوت = ۱۰۰,۰۰۰ سکه 🔥
• ۲۵ دعوت = ۳۰۰,۰۰۰ سکه 👑
• ۵۰ دعوت = ۷۵۰,۰۰۰ سکه ⭐
• ۱۰۰ دعوت = ۲,۰۰۰,۰۰۰ سکه 🏆

📊 **پیگیری Real-time:**
پیشرفت دوستات رو زنده ببین!

🔗 **لینک اختصاصی شما:**
`{invite_link}`

💡 لینک رو توی گروه‌ها بذار!
"""
    keyboard = [
        [InlineKeyboardButton("📤 اشتراک‌گذاری", url=f"https://t.me/share/url?url={invite_link}&text=بیا بازی کنیم! 🎮")],
        [InlineKeyboardButton("🎮 بازی کن", url=GAME_URL)],
        [InlineKeyboardButton("📢 کانال ما", url=CHANNEL_URL)]
    ]
    await update.message.reply_text(message, parse_mode='Markdown', reply_markup=InlineKeyboardMarkup(keyboard))

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    help_text = """
📖 **راهنمای بازی سکه شتاب**

🎮 **دستورات:**
/start - منوی اصلی
/invite - دعوت دوستان + پاداش پله‌ای
/balance - موجودی
/help - راهنما

💰 **چطور سکه بگیرم؟**
1️⃣ کلیک روی سکه
2️⃣ تسک‌های روزانه
3️⃣ دعوت دوستان (اتوماتیک!)
4️⃣ جایزه روزانه

🏆 **سیستم سطح:**
• سطح ۱: ۰ امتیاز
• سطح ۵: ۱۰,۰۰۰ امتیاز
• سطح ۱۰: ۱۱۰,۰۰۰ امتیاز
• سطح ۲۰: ۱,۰۰۰,۰۰۰ امتیاز! 🔥

🎖️ **لیگ‌ها:**
🟤 برنزی: ۰+
⚪ نقره‌ای: ۱۰k+
🟡 طلایی: ۵۰k+
🔵 پلاتینیوم: ۱۰۰k+
💎 الماس: ۵۰۰k+

📢 برای اخبار به کانال بپیوندید!
"""
    keyboard = [[InlineKeyboardButton("🎮 بازی کن", url=GAME_URL)], [InlineKeyboardButton("📢 کانال ما", url=CHANNEL_URL)]]
    await update.message.reply_text(help_text, parse_mode='Markdown', reply_markup=InlineKeyboardMarkup(keyboard))

async def balance_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = """
💰 **موجودی شما**

برای مشاهده دقیق، به بازی برید!

📊 در بازی می‌بینید:
• سکه‌ها و امتیاز کل
• سطح و لیگ
• رتبه در لیدربورد
• پیشرفت دوستان Real-time

🎮 بازی کن! 👇
"""
    keyboard = [[InlineKeyboardButton("🎮 مشاهده در بازی", url=GAME_URL)], [InlineKeyboardButton("📢 کانال", url=CHANNEL_URL)]]
    await update.message.reply_text(message, parse_mode='Markdown', reply_markup=InlineKeyboardMarkup(keyboard))

async def leaderboard_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = """
🏆 **لیدربورد جهانی**

💪 رقابت با بهترین‌ها!

📊 ویژگی‌ها:
• ۱۰۰ نفر برتر
• بروزرسانی Real-time
• رتبه شما
• امتیاز و لیگ همه

🎯 بیشتر بازی کن، بالاتر برو!
"""
    keyboard = [[InlineKeyboardButton("🏆 مشاهده لیدربورد", url=f"{GAME_URL}/League")], [InlineKeyboardButton("📢 کانال", url=CHANNEL_URL)]]
    await update.message.reply_text(message, parse_mode='Markdown', reply_markup=InlineKeyboardMarkup(keyboard))

async def channel_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = """
📢 **کانال رسمی سکه شتاب**

🎯 در کانال ما:
✅ آخرین اخبار و اپدیت‌ها
✅ رویداد‌های ویژه
✅ راهنما و آموزش
✅ کدهای تخفیف
✅ برندگان لیدربورد

💎 پیشنهادات ویژه فقط برای اعضا!

👇 همین الان عضو شو!
"""
    keyboard = [[InlineKeyboardButton("📢 عضویت", url=CHANNEL_URL)], [InlineKeyboardButton("🎮 بازی", url=GAME_URL)]]
    await update.message.reply_text(message, parse_mode='Markdown', reply_markup=InlineKeyboardMarkup(keyboard))

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user = query.from_user
    
    if query.data == "invite":
        invite_link = f"{GAME_URL}?ref__={user.id}"
        message = f"""
👥 **دعوت از دوستان**

🔗 **لینک شما:**
`{invite_link}`

🎁 **پاداش‌ها (اتوماتیک):**
• هر دعوت = ۵k سکه
• ۳ دعوت = ۲۰k سکه
• ۵ دعوت = ۳۵k سکه
• ۱۰ دعوت = ۱۰۰k سکه
• ۵۰ دعوت = ۷۵۰k سکه! 🔥

📊 پیشرفت دوستات رو Real-time ببین!
"""
        keyboard = [
            [InlineKeyboardButton("📤 اشتراک‌گذاری", url=f"https://t.me/share/url?url={invite_link}&text=بیا بازی کنیم! 🎮")],
            [InlineKeyboardButton("🎮 بازی", url=GAME_URL)],
            [InlineKeyboardButton("🔙 برگشت", callback_data="back")]
        ]
        await query.edit_message_text(message, parse_mode='Markdown', reply_markup=InlineKeyboardMarkup(keyboard))
    
    elif query.data == "balance":
        message = """
💰 **موجودی شما**

برای مشاهده دقیق، به بازی برید!

📊 در بازی می‌بینید:
• سکه‌ها و امتیاز
• سطح و لیگ
• رتبه در لیدربورد
• پیشرفت دوستان

🎮 بازی کن! 👇
"""
        keyboard = [[InlineKeyboardButton("🎮 مشاهده", url=GAME_URL)], [InlineKeyboardButton("🔙 برگشت", callback_data="back")]]
        await query.edit_message_text(message, parse_mode='Markdown', reply_markup=InlineKeyboardMarkup(keyboard))
    
    elif query.data == "leaderboard":
        message = """
🏆 **لیدربورد جهانی**

💪 رقابت با بهترین‌ها!

📊 ویژگی‌ها:
• ۱۰۰ نفر برتر
• Real-time
• رتبه شما
• امتیاز همه

🎯 بیشتر بازی کن!
"""
        keyboard = [[InlineKeyboardButton("🏆 لیدربورد", url=f"{GAME_URL}/League")], [InlineKeyboardButton("🔙 برگشت", callback_data="back")]]
        await query.edit_message_text(message, parse_mode='Markdown', reply_markup=InlineKeyboardMarkup(keyboard))
    
    elif query.data == "help":
        message = """
📖 **راهنمای سریع**

💰 **چطور سکه بگیرم؟**
• کلیک روی سکه
• انجام تسک‌ها
• دعوت دوستان (اتوماتیک!)
• جایزه روزانه

🏆 **لیگ‌ها:**
🟤 برنزی: ۰+
⚪ نقره‌ای: ۱۰k+
🟡 طلایی: ۵۰k+
🔵 پلاتینیوم: ۱۰۰k+
💎 الماس: ۵۰۰k+

📝 راهنمای کامل: /help
"""
        keyboard = [
            [InlineKeyboardButton("🎮 بازی", url=GAME_URL)],
            [InlineKeyboardButton("📢 کانال", url=CHANNEL_URL)],
            [InlineKeyboardButton("🔙 برگشت", callback_data="back")]
        ]
        await query.edit_message_text(message, parse_mode='Markdown', reply_markup=InlineKeyboardMarkup(keyboard))
    
    elif query.data == "back":
        user_name = user.first_name
        welcome_message = f"""
🎮 **سلام {user_name} عزیز!**

به **سکه شتاب** خوش اومدی! 🚀

🎁 **هدیه ورود:**
• ۱۰۰۰ سکه رایگان!
• انرژی کامل!

💰 **چطور بازی کنم؟**
• کلیک روی سکه = امتیاز
• تسک‌ها رو انجام بده
• دوستات رو دعوت کن = ۵k سکه!

🏆 **ویژگی‌ها:**
✅ سطح و لیگ
✅ لیدربورد Real-time
✅ پاداش اتوماتیک
✅ جایزه روزانه

📢 برای اخبار به کانال بپیوندید!

📱 **آماده‌ای؟ بریم!** 👇
"""
        keyboard = [
            [InlineKeyboardButton("🎮 شروع بازی", url=GAME_URL)],
            [InlineKeyboardButton("📢 عضویت در کانال", url=CHANNEL_URL)],
            [InlineKeyboardButton("👥 دعوت", callback_data="invite"), InlineKeyboardButton("💰 موجودی", callback_data="balance")],
            [InlineKeyboardButton("🏆 لیدربورد", callback_data="leaderboard"), InlineKeyboardButton("❓ راهنما", callback_data="help")]
        ]
        await query.edit_message_text(welcome_message, parse_mode='Markdown', reply_markup=InlineKeyboardMarkup(keyboard))

def main():
    if not TOKEN or TOKEN == "توکن_جدید_ربات_رو_اینجا_بذار":
        print("❌ خطا: توکن تنظیم نشده!")
        print("💡 توکن رو از @BotFather بگیر و توی خط 9 بذار")
        return
    
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("invite", invite_command))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("balance", balance_command))
    app.add_handler(CommandHandler("leaderboard", leaderboard_command))
    app.add_handler(CommandHandler("channel", channel_command))
    app.add_handler(CallbackQueryHandler(button_handler))
    
    print("=" * 50)
    print("🤖 ربات سکه شتاب شروع شد!")
    print("=" * 50)
    print(f"📱 بازی: {GAME_URL}")
    print(f"📢 کانال: {CHANNEL_URL}")
    print("=" * 50)
    print("✅ ربات آماده است...")
    print("💡 توقف: Ctrl+C")
    print("=" * 50)
    
    app.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()
