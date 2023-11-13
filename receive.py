#코드를 실행하면 "테스트 진행중 이라는 메시지를 받습니다."
import asyncio
import telegram

token = "본인의 텔레그램 token값을 넣으면 됩니다."
id="텔레그램 봇의 아이디를 넣으면 됩니다."

async def main():
    bot = telegram.Bot(token)
    await bot.send_message(chat_id=id, text="테스트 진행중")

asyncio.run(main())
