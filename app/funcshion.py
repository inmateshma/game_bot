import random
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

ruletka_numbers = [ 26, 0, 32, 15, 19, 4, 21, 2, 25, 17, 34, 6, 27, 13, 36, 11, 30, 8, 23, 10, 5, 24, 16, 33, 1, 20, 14, 31, 9, 22,18, 29, 7, 28, 12, 35, 3, 26, 0, 32, 15, 19, 4, 21, 2, 25, 17, 34, 6, 27, 13, 36, 11, 30, 8, 23, 10, 5, 24, 16, 33, 1, 20, 14, 31, 9, 22,18, 29, 7, 28, 12, 35, 3, 26 ]



def prockrutka(a,el):
    button1 = InlineKeyboardButton(text=str(ruletka_numbers[(a-1)+el]), callback_data='aa')
    button2 = InlineKeyboardButton(text=str(ruletka_numbers[a+el]), callback_data='aa')
    button3 = InlineKeyboardButton(text=str(ruletka_numbers[(a+1)+el]), callback_data='aa')
    list_buttons = [button1, button2, button3]
    return list_buttons


def result_of_ruletka(a,b):
    if a == str(b):
        c = f"ваша ставка сыграла, поздравляю, хотите сыграть еще раз?"
    else:
        c = f"ваша ставка не сыграла, хотитет сыграть еще раз?"
    return c