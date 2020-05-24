from telethon.sync import TelegramClient, utils

api_id   = '12345678'  #申请请方法参考 https://docs.telethon.dev/en/latest/basic/signing-in.html
api_hash = '123456789abcdefg'
bot      = TelegramClient('your username', api_id, api_hash)  #此处填入你的Telegram名字
channel  = 'https://t.me/qinghua_box' #爬取的频道地址
 
async def main():
    messages = bot.iter_messages(channel, limit=50)
    msges = '';
    async for message in messages:
        msg = str(message.message)
        msge = msg.replace("\r", r"\r").replace('\n', r'\n')
        # print(msge)
        msges = msges + msge + "\n"
    with open('./db.txt', 'a+') as file:
        file.write(msges)

with bot:
    bot.loop.run_until_complete(main())
