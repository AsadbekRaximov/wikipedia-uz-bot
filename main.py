import logging
import wikipedia
from aiogram import Bot, Dispatcher, executor, types

# Bu yerga botFatherdan olingan tokenni qo'ying
API_TOKEN = ''

# O'zbek tilidagi maqolalarni qidirish uchun
wikipedia.set_lang('uz')
# Ruscha maqolalar uchun 'ru'
# Inglizcha maqolalar uchun 'en'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_start(message: types.Message):
    text = """
🇺🇿 Salom, maqola qidirish uchun biror matn yuboring
🇷🇺 Привет, отправьте текст для поиска статей
    """
    await message.answer(text)


@dp.message_handler()
async def sendWiki(message: types.Message):
    try:
        respond = wikipedia.summary(message.text)
        await message.answer(respond)
    except:
        text="""
Maqola topilmadi❌
Статья не найдена❌
        """
        await message.answer(text)


# Agar foydalanuvchi matn emas boshqa kontent yuborsa(gif, video, audio, stiker, ...)
@dp.message_handler(content_types=types.ContentType.ANY)
async def handler(message: types.Message):
    text="""Noto'g'ri kontent yubordingiz!
Maqola qidirish uchun biror matn yuboring
Botni qaytadan ishga tushirish: /start"""
    await message.answer(text)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
