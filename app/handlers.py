import app.keybords as kb
import random

from aiogram.types import InlineKeyboardMarkup
from app.funcshion import  prockrutka , ruletka_numbers , result_of_ruletka
from aiogram import F, Router
from aiogram.types import Message ,CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram.fsm.state import State ,StatesGroup
from aiogram.fsm.context import FSMContext

router = Router()

class stvk(StatesGroup):
    stavka = State()

bd = 'nth'

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("выберите игру:", reply_markup=kb.start_game)

@router.callback_query(F.data == 'start')
async def game1(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer("выберите игру:", reply_markup=kb.start_game)

@router.callback_query(F.data == 'game1')
async def game1(callback: CallbackQuery):
    await callback.answer('вы выбрали игру номер 1')
    await callback.message.answer("game process...", reply_markup=kb.first_phase)


@router.callback_query(F.data == 'game2')
async def stavka(callback: CallbackQuery, state:FSMContext):
    await callback.answer('время ставки')
    await state.set_state(stvk.stavka)
    await callback.message.answer("введите число от 0 до 36:")

@router.message(stvk.stavka)
async def stavka_catching(message:Message, state:FSMContext):
    await state.update_data(stavka = message.text)
    data = await state.get_data()
    global bd
    bd = data['stavka']
    await state.clear()
    try:
        if int(bd) in range(0,37):
            await message.answer(f" вы выбрали номер: {data['stavka']}",reply_markup=kb.krutka1)
        else:
            await message.answer(f'такой ставки не существует, попробуйте еще.', reply_markup=kb.stavka)
    except ValueError:
        await message.answer(f'такой ставки не существует, попробуйте еще.', reply_markup=kb.stavka)

@router.callback_query(F.data == "krutka")
async def krutka(callback: CallbackQuery):
    await callback.answer('game process...',)
    a = random.randint(1,37)
    el=0
    while el < 17:
        el+=1
        await callback.message.edit_text("game process...", reply_markup= InlineKeyboardMarkup(inline_keyboard=[prockrutka(a,el)]))
    await callback.message.answer(f'выпал номер {ruletka_numbers[a+17]}')      
    await callback.message.answer(result_of_ruletka(bd,ruletka_numbers[a+17]), reply_markup=kb.yes_or_no)