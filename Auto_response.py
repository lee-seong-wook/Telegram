#동일하게 logging부분은 필요없으면 빼셔도 무관합니다.
#'테스트'라는 단어가 들어간 문장이라면 '테스트 성공입니다.'라고 답변이 돌아올것입니다.

import logging
from telegram import Update
from telegram.ext import Application, ContextTypes, MessageHandler, filters

token = '텔레그램 토큰값'

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logging.getLogger("httpx").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text
    if "테스트" in msg:
        replay = "테스트 성공입니다."
    else:
        replay = "잘 이해하지 못했습니다. 다시한번 적어주세요."
    await update.message.reply_text(replay)

def main():
    application = Application.builder().token(token).build()
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
