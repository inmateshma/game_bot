from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
import random


start_game = InlineKeyboardMarkup(inline_keyboard=[
    #[InlineKeyboardButton(text="📦/💥", callback_data='game1')],
    [InlineKeyboardButton(text="🎰", callback_data='game2')]
])


first_phase = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="игра в разработке...", callback_data='...')]
])   

krutka1 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='крутить рулетку', callback_data='krutka')]
])

yes_or_no = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="да", callback_data='game2')],
    [InlineKeyboardButton(text="нет", callback_data='start')]
])

stavka = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="попробовать еще раз.", callback_data='game2')],
    [InlineKeyboardButton(text="выбрать другую игру", callback_data='start')]
])