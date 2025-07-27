from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

TOKEN = "8042595654:AAEOXMx6ogjktBRzunES4nXdX10eRteAbKc"
OWNER_CHAT_ID = "123456789"  # Replace with your own Telegram ID

async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.channel_post and update.channel_post.photo:
        file_id = update.channel_post.photo[-1].file_id
        new_file = await context.bot.get_file(file_id)
        link = f"https://api.telegram.org/file/bot{TOKEN}/{new_file.file_path}"
        await context.bot.send_message(chat_id=OWNER_CHAT_ID, text=f"Image Link: {link}")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.PHOTO & filters.UpdateType.CHANNEL_POST, handle_photo))
app.run_polling()



async def get_id(update, context):
    await update.message.reply_text(f"Your ID: {update.message.chat_id}")

app.add_handler(MessageHandler(filters.TEXT, get_id))