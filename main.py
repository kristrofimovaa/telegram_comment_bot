
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

TOKEN = '7610862682:AAEbvP8aUHRTbdI29MgkX8de1pXaKJUcFMw'
CHANNEL_ID = '@krisitrofimova'
COMMENT_TEXT = """
приветик, родня! 👋

во-первых, хочу напомнить, что ты — супер 💖
и прислать мои остальные соц сети:

📸 Instagram: https://www.instagram.com/67.llllll?igsh=c3B4ZWRqaDJ5cmQy
🎵 TikTok: https://www.tiktok.com/@kristrofimovaaaa?_t=ZN-8w8H0aaCqQQ&_r=1

📝 Написав комментарий вы автоматически соглашаетесь с правилами чата
"""

async def new_post_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_chat.type == 'channel':
        keyboard = [
            [
                InlineKeyboardButton("правила", url="https://telegra.ph/Pravila-chatika-Kristyushki-Trofimovoj-05-06"),
                InlineKeyboardButton("войти в чат", url="https://t.me/+t-wNv5ojDLU3Yzdi")
            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await context.bot.send_message(
            chat_id=CHANNEL_ID,
            text=COMMENT_TEXT,
            reply_to_message_id=update.message.message_id,
            reply_markup=reply_markup
        )

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.ChatType.CHANNEL, new_post_handler))

app.run_polling()
