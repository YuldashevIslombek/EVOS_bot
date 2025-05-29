from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    WebAppInfo
)
from messages import messages


def start_buttons(lang):
    buttons = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text=f"{messages[lang]['about_company']}"),
         KeyboardButton(text=f"{messages[lang]['branches']}")],
        [KeyboardButton(text=f"{messages[lang]['job_positions']}")],
        [KeyboardButton(text=f"{messages[lang]['menu']}",
                        web_app=WebAppInfo(url="https://yuldashevislombek.github.io/EVOS_bot/")),
         KeyboardButton(text=f"{messages[lang]['news']}")],
        [
            KeyboardButton(text=f"{messages[lang]['contacts']}"),
            KeyboardButton(text=f"{messages[lang]['language']}")
        ],
        [KeyboardButton(text=f"{messages[lang]['send_location']}", request_location=True), ]

    ],

        resize_keyboard=True)

    return buttons


def select_language():
    buttons = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🇺🇿", callback_data="uz"),
         InlineKeyboardButton(text="🇷🇺", callback_data="ru"),
         ]

    ], resize_keyboard=True)
    return buttons



def get_regions(lang):
    buttons = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text=f"{messages[lang]['Tashkent']}"), KeyboardButton(text=f"{messages[lang]['Andijan']}")],
        [KeyboardButton(text=f"{messages[lang]['Qarshi']}"), KeyboardButton(text=f"{messages[lang]['Qoqon']}")],
        [KeyboardButton(text=f"{messages[lang]['Namangan']}"), KeyboardButton(text=f"{messages[lang]['Samarqand']}")],
        [KeyboardButton(text=f"{messages[lang]['Fargona']}"), KeyboardButton(text=f"{messages[lang]['Shaxrisabz']}")],
        [KeyboardButton(text=f"{messages[lang]['Xorazim']}"), KeyboardButton(text=f"{messages[lang]['Navoiy']}")],
        [KeyboardButton(text=f"{messages[lang]['Back🔙']}")]

    ], resize_keyboard=True)
    return buttons