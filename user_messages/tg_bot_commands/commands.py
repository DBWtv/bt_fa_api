from TGBot.main import BOT_TOKEN
import requests

BOT_API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/"


def send_message(message: dict, chat_id: int):
    text = f'{message["first_name"]}, я получил от тебя сообщение:\n{message["message"]}'
    with requests.Session() as client:
        response = client.get(
            f"{BOT_API_URL}sendMessage?chat_id={chat_id}&text={text}"
        )
        return response
