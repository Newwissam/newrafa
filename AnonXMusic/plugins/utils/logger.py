from pyrogram.enums import ParseMode

from AnonXMusic import app
from AnonXMusic.utils.database import is_on_off
from config import LOGGER_ID


async def play_logs(message, streamtype):
    if await is_on_off(2):
        logger_text = f"""
<b>{app.mention} قائمة التشغيل</b>

<b>ايدي المجموعة :</b> <code>{message.chat.id}</code>
<b>اسم المجموعة :</b> {message.chat.title}
<b>يوزر المجموعة :</b> @{message.chat.username}

<b>ايدي الشخص :</b> <code>{message.from_user.id}</code>
<b>اسمه :</b> {message.from_user.mention}
<b>يوزره :</b> @{message.from_user.username}

<b>• :</b> {message.text.split(None, 1)[1]}
<b>• :</b> {streamtype}"""
        if message.chat.id != LOGGER_ID:
            try:
                await app.send_message(
                    chat_id=LOGGER_ID,
                    text=logger_text,
                    parse_mode=ParseMode.HTML,
                    disable_web_page_preview=True,
                )
            except:
                pass
        return
