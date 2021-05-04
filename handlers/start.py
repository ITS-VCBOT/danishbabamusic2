from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_sticker("CAACAgEAAxkBAAEJhqRghWPsjqUKSS8_6VmdS7qpU3_lTQAC1wEAAhj9KUQdpq7AObW5uh8E")
    await message.reply_text(
        f"""<b>Hey {format(
        message.from_user.mention)}! Hii
I am powerful VC music Bot..🔥
I can play songs in your group's VC 
To listen songs also add @danishbabamusic to your group..
And don't forgot to promote me with all rights..😉
Otherwise I can't play songs..🙄
Use the buttons below to know more about me..🔥
 </b>""",
      
       
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⚪ Support Group ⚪", url="https://t.me/CoffinXsupport",
                    )
                ],
                [
                    InlineKeyboardButton(
                        "⚪ Channel ⚪", url="https://t.me/CoffinX_updates"
                    ),
                    InlineKeyboardButton(
                        "⚪ Help ⚪", callback_data="help_back"
                    ),
                    InlineKeyboardButton(
                        "⚪ Assistant ⚪", url="https://t.me/CoffinXAssistant?startgroup=true"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "➕ Add To Your Group ➕", url="https://t.me/CoffinXmusic_BoT?startgroup=true"
                    ) 
                ]
            ]
        )
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**𝘏𝘦𝘺 𝘐'𝘮 𝘈𝘭𝘪𝘷𝘦..👻 𝘈𝘯𝘥 𝘙𝘦𝘢𝘥𝘺 𝘛𝘰 𝘗𝘭𝘢𝘺 𝘔𝘶𝘴𝘪𝘤 𝘍𝘰𝘳 𝘠𝘰𝘶 🎛️**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔊 Channel", url="https://t.me/CoffinX_updates"
                    )
                ],[
                    InlineKeyboardButton(
                        "✅ Yes", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "No ❌", callback_data="close"
                    )
                ]
            ]
        )
    )


@Client.on_message(
    filters.command("help")
    & filters.private
    & ~ filters.edited
)
async def help(client: Client, message: Message):
    await message.reply_text(
        f"""<b>Here Is Cmd Of CoffinXmusic !
╔━━━━━━━━⊰✦⊱━━━━━━━━╗
\n/play <song name> - play song you requested
/dplay <song name> - play song you requested via deezer
/splay <song name> - play song you requested via jio saavn
/playlist - Show now playing list
/current - Show now playing
/song <song name> - download songs you want quickly
/search <query> - search videos on youtube with details
/deezer <song name> - download songs you want quickly via deezer
/saavn <song name> - download songs you want quickly via saavn
/video <song name> - download videos you want quickly
\n*Admins only*
/player - open music player settings panel
/pause - pause song play
/resume - resume song play
/skip - play next song
/end - stop music play
/userbotjoin - invite assistant to your chat
/admincache - Refresh admin list
╚━━━━━━━━⊰✦⊱━━━━━━━━╝
 </b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔊 Channel", url="https://t.me/CoffinX_updates"
                    )
                ],[
                    InlineKeyboardButton(
                        "🚑 Support Group", url="https://t.me/CoffinXsupport"
                    ),
                    InlineKeyboardButton(
                        "➕Add CoffinX in your group➕", url="https://t.me/CoffinXmusic_BoT?startgroup=true"
                    )
                ]
            ]
        )
    )
