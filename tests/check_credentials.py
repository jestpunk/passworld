import asyncio
import telegram
import sys

async def main():
    bot = telegram.Bot(sys.argv[1])
    async with bot:
        updates = (await bot.get_updates())
        chat_id = updates[0].message.from_user.id

        await bot.send_message(text=f"Hi {updates[0].message.from_user.first_name}!", 
                               chat_id=chat_id)
        
        #print(updates)

if __name__ == '__main__':
    asyncio.run(main())
