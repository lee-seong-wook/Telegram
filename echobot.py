#텔레그램에서 적은 문장을 다시 돌려보내는 에코봇입니다.
#logging의 경우 터미널창에서 텔레그램이 실행되고 있는 것을 보여주는 코드이기에 빼셔도 무관합니다.

import logging
from telegram import Update
from telegram.ext import Application, ContextTypes, MessageHandler, filters

token = '본인의 Token값을 넣으시면 됩니다.'

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logging.getLogger("httpx").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(update.message.text)

def main():
    application = Application.builder().token(token).build()
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
