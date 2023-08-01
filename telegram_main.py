import subprocess
from telegram import Update, Message, Bot
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

bot_token = ""
user_chat_id = ####
bot = Bot(bot_token)

global stdout_output

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"User Chat ID: {update.message.chat.id}")
    message_type: str = update.message.chat.type
    text: str = update.message.text

    if update.message.chat.id == user_chat_id and text != "":
        process = subprocess.Popen(["python", "main.py", text], stdout=subprocess.PIPE)
        result = process.communicate()[0]
        stdout_output = result.decode('utf-8')
        await bot.send_message(chat_id=user_chat_id, text=str(stdout_output))
    else:
        text = ''

if __name__ == "__main__":
    print("Program Starting")
    app = Application.builder().token(bot_token).build()
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    try:
        while True:
            app.run_polling(poll_interval=1)
    except Exception as e:
        print(f"An error occurred: {e}")
