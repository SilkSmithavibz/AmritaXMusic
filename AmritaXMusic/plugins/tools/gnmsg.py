import re
from pyrogram import filters
import random
from AmritaXMusic import app


@app.on_message(filters.command(["gn","n","oodnight","ood Night","ood night"], prefixes=["/","g","G"]))
def goodnight_command_handler(_, message):
    sender = message.from_user.mention
    send_sticker = random.choice([True, False])
    if send_sticker:
        sticker_id = get_random_sticker()
        app.send_sticker(message.chat.id, sticker_id)
        message.reply_text(f"**Goodnight, {sender}! Sleep tight. 🌙**")
    else:
        emoji = get_random_emoji()
        app.send_message(message.chat.id, emoji)
        message.reply_text(f"**Goodnight, {sender}! Sleep tight. {emoji}**")


def get_random_sticker():
    stickers = [
        "CAACAgUAAxkBAAKMxGdMMavNlAlju2_9sM15jrwRY3w6AAIhBgAC2YOAVQHB4kZyPtyrNgQ", # Sticker 1
        "CAACAgUAAxkBAAKMx2dMMclFX1maKN30N0P__QwvH1kCAAJ5BAACtJhBVgAB3wW91RELhzYE", # Sticker 2
        "CAACAgUAAxkBAAKMymdMMebdkofgNNYU7Tzi-X0VKgLnAAI1BgACs2cYVma4ssyKE1ycNgQ", # Sticker 3
        "CAACAgUAAxkBAAKMzWdMMg0xWeDDq3uUdq_fjhTOEarAAAJMDAACRgABIFdPOAqnvz9iMzYE",
        "CAACAgUAAxkBAAKM0GdMMkOGVmIanmjKcGOlOsd_7lXXAAJzCAACFYwYV5ZFOobqxjGMNgQ",
    ]
    return random.choice(stickers)


def get_random_emoji():
    emojis = [
        "😴",
        "😪",
        "💤",
    ]
    return random.choice(emojis)
