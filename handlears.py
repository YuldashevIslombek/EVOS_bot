import os

from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, LabeledPrice, FSInputFile
from database import database
from keyboard import select_language, start_buttons, get_regions
from messages import messages, job_info, info_company, hello_message

router = Router()


@router.message(F.text.in_(["🇺🇿/🇷🇺 Til", "🇺🇿/🇷🇺 Язык"]))
async def get_language(message: Message):
    lang = database.get_user_lang(message.from_user.id)
    await message.answer(messages[lang]['select_lang'], reply_markup=select_language())

@router.callback_query(F.data.in_(["uz", "ru"]))
async def set_language(callback_query: CallbackQuery):
    lang = callback_query.data
    database.set_user_lang(telegram_id=callback_query.from_user.id, lang=lang)
    await callback_query.message.answer(text=hello_message[lang], reply_markup=start_buttons(lang))

@router.message(F.text.in_(["Вакансии", "Bo'sh ish o'rinlari"]))
async def get_jobs(message: Message):
    lang = database.get_user_lang(message.from_user.id)
    await message.answer(text=job_info[lang]["job_position"])

@router.message(F.text.in_ (["🏢 О кампании", "🏢 Kampaniya haqida"]))
async def about_company_handler(message: Message):
    img = FSInputFile(os.path.join(os.path.dirname(__file__), "images", "evos.png"))
    lang = database.get_user_lang(message.from_user.id)
    text = info_company[lang]["about_company"]


@router.message(F.text.in_ (["Филиалы", "Filliallari"]))
async def Filliallari(message: Message):
        img = FSInputFile(os.path.join(os.path.dirname(__file__), "images", "img_19.png"))
        text = (
            "EVOS - O'zbekistondagi eng yirik fastfud kompaniyasi. Ayni paytda 49 ta chakana savdo shoxobchasi va zamonaviy"
            "diversifikatsiyalangan ishlab chiqarish ochiq. "
            "Kompaniya xodimlari birgalikda rivojlanib, kundan -kunga o'sib "
            "borayotgan katta oila. EVOS har kuni kengayib bormoqda, bugungi kunda bizda bir yarim mingdan ortiq odam bor. Bizning "
            "jamoamizga a'zo bo'ling, EVOS oilasiga xush kelibsiz!")
        lang = database.get_user_lang(message.from_user.id)
        await message.answer_photo(photo=img, caption=text, reply_markup=get_regions(lang))



@router.message(F.text.in_(["Back🔙", "Назад🔙"]))
async def set_language(message: Message):
    print(message.text)
    lang = database.get_user_lang(message.from_user.id)
    await message.answer(text=hello_message[lang], reply_markup=start_buttons(lang))