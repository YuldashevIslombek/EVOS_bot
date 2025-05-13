import os

from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery, FSInputFile
from database import database
from keyboard import select_language, start_buttons
from messages import messages

router = Router()

@router.message(F.text.in_(["🇺🇿/🇷🇺 Til", "🇺🇿/🇷🇺 Язык"]))
async def get_language(message: Message):
    lang = database.get_user_lang(message.from_user.id)
    await message.answer(messages[lang]['select_lang'], reply_markup=select_language())

@router.callback_query(F.data.in_(["uz", "ru"]))
async def set_language(callback_query: CallbackQuery):
    lang = callback_query.data
    database.set_user_lang(telegram_id=callback_query.from_user.id, lang=lang)
    await callback_query.message.answer(text='Assalomu alekum', reply_markup=start_buttons(lang))


@router.message(F.text == "🏢 Kampaniya haqida")
async def about_company_handler(message: Message):
    img = FSInputFile(os.path.join(os.path.dirname(__file__), "images", "img.png"))
    text = ("BIZ HAQIMIZDA!\n"
            "Kompaniyamizning birinchi filiali 2006 yilda ochilgan bo’lib, shu kungacha muvaffaqiyatli faoliyat yuritib "
            "kelmoqdaligini bilarmidingiz? 15 yil davomida kompaniya avtobus bekatidagi kichik ovqatlanish joyidan "
            "zamonaviy, kengaytirilgan tarmoqqa aylandi, u bugungi kunda O‘zbekiston bo‘ylab 65 dan ortiq restoranlarni,"
            "o‘zining eng tezkor yetkazib berish xizmatini, zamonaviy IT-infratuzilmasini va 2000 dan ortiq xodimlarni "
            "o‘z ichiga oladi.")
    await message.answer(photo=img, text=text)



# @router.message(Command("about_company"))
# async def about_company_handler()
