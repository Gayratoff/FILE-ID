from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
import logging
from aiogram import types
from aiogram.types import CallbackQuery

from utils.db_api.sqlite import *
from loader import dp, db, bot
logging.basicConfig(level=logging.INFO)

bot_user = "https://t.me/FileDown_Robot?start="

@dp.callback_query_handler(text="start")
async def bot_echo(message: CallbackQuery):
    user_id = message.from_user.id
    await bot.send_message(chat_id=user_id,text="<b>– Yaxshi Qo'shimcha Ma'lumotlar Uchun:\n\nSizga Kerakli Bo'lgan Ma'lumot Kodini Kiriting yoki Bu Botga O'tgan Tugmangizni Qaytadan Bosing.</b>")

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    if 2 == len(message.text.split(' ')) > 0:
        return await idsave(message, message.text.split(' ')[1])
    user_id = message.from_user.first_name
    await message.reply(f"<b>👋🏻 Salom {user_id}\n\n– Qo'shimcha Ma'lumotlar Uchun:\nSizga Kerakli Bo'lgan Ma'lumot Kodini Kiriting yoki Bu Botga O'tgan Tugmangizni Qaytadan Bosing.</b>")

@dp.message_handler(content_types=['document'])
async def echo(message: types.Message):
    try:
        file_id = message.document.file_id
        caption = message.caption
        if caption == None: caption = ''
        user_id = message.from_user.id
        db.add_files(type="document", file_id=file_id, caption=caption, user_id=user_id)
        id_send = db.select_files(user_id=user_id)
        for idsend in id_send:
            sql_id = idsend[0]
        await message.answer(f"✅ Document id silakasi {bot_user}{sql_id}")
    except:
        await message.answer("Xatolik yuzaga keldi, qayta urinb ko'ring 😔")

@dp.message_handler(content_types=['video'])
async def echo(message: types.Message):
    try:
        file_id = message.video.file_id
        caption = message.caption
        if caption == None: caption = ''
        user_id = message.from_user.id
        db.add_files(type="video", file_id=file_id, caption=caption, user_id=user_id)
        id_send = db.select_files(user_id=user_id)
        for idsend in id_send:
            sql_id = idsend[0]
        await message.answer(f"✅ Video id silakasi {bot_user}{sql_id}")
    except:
        await message.answer("Xatolik yuzaga keldi, qayta urinb ko'ring 😔")

@dp.message_handler(content_types=['photo'])
async def echo(message: types.Message):
    try:
        file_id = message.photo[0].file_id
        caption = message.caption
        if caption == None: caption = ''
        user_id = message.from_user.id
        db.add_files(type="photo", file_id=file_id, caption=caption, user_id=user_id)
        id_send = db.select_files(user_id=user_id)
        for idsend in id_send:
            sql_id = idsend[0]
        await message.answer(f"✅ Photo id silakasi {bot_user}{sql_id}")
    except:
        await message.answer("Xatolik yuzaga keldi, qayta urinb ko'ring 😔")

@dp.message_handler(content_types=['audio'])
async def echo(message: types.Message):
    try:
        file_id = message.audio.file_id
        caption = message.caption
        if caption == None: caption = ''
        user_id = message.from_user.id
        db.add_files(type="audio", file_id=file_id, caption=caption, user_id=user_id)
        id_send = db.select_files(user_id=user_id)
        for idsend in id_send:
            sql_id = idsend[0]
        await message.answer(f"✅ Audio id silakasi {bot_user}{sql_id}")
    except:
        await message.answer("Xatolik yuzaga keldi, qayta urinb ko'ring 😔")

@dp.message_handler(content_types=['voice'])
async def echo(message: types.Message):
    try:
        file_id = message.voice.file_id
        caption = message.caption
        if caption == None: caption = ''
        user_id = message.from_user.id
        db.add_files(type="voice", file_id=file_id, caption=caption, user_id=user_id)
        id_send = db.select_files(user_id=user_id)
        for idsend in id_send:
            sql_id = idsend[0]
        await message.answer(f"✅ Voice id silakasi {bot_user}{sql_id}")
    except:
        await message.answer("Xatolik yuzaga keldi, qayta urinb ko'ring 😔")


@dp.message_handler()
async def idsave(message: types.Message, text=None):
    try:
        if text == None: text = message.text
        if text.isdigit():
            IDTXT1 = db.select_files(id=text)
            if len(IDTXT1) > 0:
                IDTXT = IDTXT1[0]
                if IDTXT[1] == 'document':
                    await message.answer_document(IDTXT[2], caption=IDTXT[3])
                elif IDTXT[1] == 'video':
                    await message.answer_video(IDTXT[2], caption=IDTXT[3])
                elif IDTXT[1] == 'photo':
                    await message.answer_photo(IDTXT[2], caption=IDTXT[3])
                elif IDTXT[1] == 'audio':
                    await message.answer_audio(IDTXT[2], caption=IDTXT[3])
                elif IDTXT[1] == 'voice':
                    await message.answer_voice(IDTXT[2], caption=IDTXT[3])
            else:
                await message.answer("Hech narsa topilmadi 😔")
    except:
        await message.answer("Xatolik yuzaga keldi, qayta urinb ko'ring 😔")