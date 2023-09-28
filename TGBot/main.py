from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from pathlib import Path
import httpx
import os
from dotenv import load_dotenv

load_dotenv()

SETTINGS_FILE = Path(__file__).resolve().parent.parent / "conf" / "settings.py"


with SETTINGS_FILE.open() as settings_file:
    exec(settings_file.read())


BOT_TOKEN = os.getenv('BOT_TOKEN')


async def send_message(message: dict):
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"http://localhost:8000/api/v1/bot/{os.getenv('TG_BOT_API_TOKEN')}",
            json={"message": message}
        )
        return response


bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def start(message: Message):
    await message.answer("Введите токен полученый на сайте")


@dp.message()
async def echo(message: Message):
    message_to_send = {
        'user_id': message.chat.id,
        'username': message.chat.username,
        'first_name': message.chat.first_name,
        'last_name': message.chat.last_name,
        'message': message.text,
    }

    response = await send_message(message_to_send)
    if response.status_code == 200:
        await message.answer("Ваш токен зарегистрирован")
    elif response.status_code == 400:
        if response.json()['info'] == "Token already exists":
            await message.answer("Ваш токен уже зарегистрирован")
        elif response.json()['info'] == "User already exists":
            await message.answer("Вы регистрировали токен от другого пользователя")
        else:
            await message.answer("Возникла ошибка")
    else:
        await message.answer("Ваш токен не зарегистрирован")


if __name__ == '__main__':
    dp.run_polling(bot)
