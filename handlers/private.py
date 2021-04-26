from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgQAAx0CTv65QgABBfJlYF6VCrGMm6OJ23AxHmD6qUSWESsAAhoQAAKm8XEeD5nrjz5IJFYeBA")
    await message.reply_text(
        f"""**Hɘƴ, I'ɱ {bn} 🎵

I cʌŋ pɭʌƴ ɱʋsɩc ɩŋ ƴoʋʀ ʛʀoʋp's voɩcɘ cʌɭɭ. Dɘvɘɭopɘɗ ɓƴ [Hexor(https://t.me/Its_Hexor).

Aɗɗ ɱɘ to ƴoʋʀ ʛʀoʋp ʌŋɗ pɭʌƴ ɱʋsɩc ʆʀɘɘɭƴ !**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🛠 Soʋʀcɘ Coɗɘ 🛠", url="https://t.me/SankiiPublic")
                  ],[
                    InlineKeyboardButton(
                        "💬 Gʀoʋp", url="https://t.me/SankiiPublic"
                    ),
                    InlineKeyboardButton(
                        "🔊 Bot Owŋɘʀ", url="https://t.me/Its_Hexor"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "➕ Aɗɗ Mɘ To Yoʋʀ Gʀoʋp ➕", url="https://t.me/sankiipublicbot?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**Gʀoʋp Mʋsɩc Pɭʌƴɘʀ Oŋɭɩŋɘ ✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔊 Bot Owŋɘʀ", url="https://t.me/its_Hexor")
                ]
            ]
        )
   )


