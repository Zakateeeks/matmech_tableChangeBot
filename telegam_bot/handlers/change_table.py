import os

from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message

from telegam_bot.config import bot
from telegam_bot.keyboard.start_keyboard import *
from telegam_bot.keyboard.table_keyboard import *

table_router = Router()


class TableStep(StatesGroup):
    enter_table_name = State()


def table_name_check(name: str) -> bool:
    """
    Проверка директории на существование указанного файла.

    :param name: имя файла с расширением
    :return: True - если файл существует, False - в ином случае
    """
    return os.path.isfile(os.path.join(name))


@table_router.message(TableStep.enter_table_name)
async def table_name_chosed(message: Message, state: FSMContext) -> None:
    """
    Проверка указанного файла на существование.

    Обновляем состояние, для ожидания получения сообщения
    от пользователя.

    :param message: Объект сообщения
    :param state: Текущее состояние
    """
    await state.update_data(input_name=message)
    is_file = table_name_check(message.text)
    await message.delete()
    await state.clear()

    mess_id = message.chat.id
    if is_file:
        await bot.send_message(mess_id, text="Файл найден!\nПерейдём к выбору"
                                             " режима обработки",
                               reply_markup=mode_table_edit().as_markup())
    else:
        await bot.send_message(mess_id, text="Файл не найден, попробуйте"
                                             " заново",
                               reply_markup=choice_mode().as_markup())
