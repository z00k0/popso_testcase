from dotenv import load_dotenv
import os
import json
from telethon import TelegramClient

load_dotenv()
API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")

client = TelegramClient("test", API_ID, API_HASH)

channels = ["ozonmarketplace", "market_marketplace"]
channels_dict = {"ozonmarketplace": "OZON", "market_marketplace": "Яндекс.Маркет"}


async def parse(channel, news_count):
    counter = 0
    result = []
    async for message in client.iter_messages(channel):
        # Параметр limit нормально не работает. Попадаются пустые посты. Возможно удаленные или скрытые.
        # Пришлось добавить счетчик "непустых" постов, чтоб  спарсить точно 10 штук
        if len(message.text) > 0:
            counter += 1
            path = None
            if message.photo:
                path = await client.download_media(
                    message.photo, f"{channels_dict[channel]}-{message.id}.jpg"
                )

            result.append(
                {
                    "channel": channels_dict[channel],
                    "message_id": message.id,
                    "date": message.date.strftime("%d-%m-%Y, %H:%M:%S"),
                    "text": message.text,
                    "photo": path,
                }
            )
        if counter >= news_count:
            break
    return result


async def main():
    news = []
    for channel in channels_dict.keys():
        res = await parse(channel, 10)
        news.extend(res)
    with open("news.json", "w", encoding="utf8") as file:
        json.dump(news, file, ensure_ascii=False, indent=4)


with client:
    client.loop.run_until_complete(main())
