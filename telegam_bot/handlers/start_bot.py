from aiogram import Router, F, types
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from telegam_bot.handlers.change_table import TableStep
from telegam_bot.keyboard.start_keyboard import choice_mode

start_router = Router()


@start_router.message(Command('start'))
async def start_command(message: Message) -> None:
    """
    Функция, в которой описывается работа бота при получении команды /start

    :param message: Объект сообщения
    """
    await message.delete()  # Удаляем сообщение /start от пользователя

    name = message.from_user.full_name

    """
    Тут надо дописать подключение к БД
    """

    await message.answer(text=f"Приветствую, {name}\n\n Выберите режим работы"
                              f" с таблицей",
                         reply_markup=choice_mode().as_markup())


@start_router.callback_query(StateFilter(None),
                             F.data.in_(["ok_urfu_mode", "individual_mode"]))
async def choice_mode_callback(callback_query: types.CallbackQuery,
                               state: FSMContext) -> None:
    """
    Выбор режима работы с таблицей.

    Режим для работы в приёмной комиссии
    Режим для собственной настройки работы с таблицей.

    :param callback_query: Объект сообщения (в виде callback_query)
    :param state: Текущее состояние
    """
    match (callback_query.data):
        case "ok_urfu_mode":
            await callback_query.message.edit_text("Введите название файла с расширением")
            await state.set_state(TableStep.enter_table_name)
        case "individual_mode":
            await callback_query.message.edit_text("В разработке ...")
