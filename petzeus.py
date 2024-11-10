import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Command handler
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hello! I am your bot.')

def main() -> None:
    TOKEN = "7869612145:AAFeExC0Gkcr9dqUMK_om0Puy7vm4oIqRLY"  # Replace with your token
    updater = Updater(TOKEN)

    # Register handlers
    updater.dispatcher.add_handler(CommandHandler("start", start))

    # Start the Bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()