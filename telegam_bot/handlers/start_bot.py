from aiogram import types, Dispatcher

from telegam_bot.keyboard import start_keyboard


async def welcome_message(msg: types.Message) -> None:
    """
    Функция, в которой описывается работа бота при получении команды /start

    :param msg: Объект сообщения
    """
    await msg.delete()  # Удаляем сообщение /start от пользователя

    chat_id = msg.chat.id
    name = msg.from_user.first_name

    """
    Тут надо дописать подключение к БД
    """

    await msg.answer(text=f"Приветствую, {name}\n\n Выберите режим работы"
                          f" с таблицей", reply_markup=start_keyboard.choice_mode())


def start_handler(dp: Dispatcher) -> None:
    """
    В этой функции мы описываем то, как будут вызываться функции
    для взаимодействия бота с пользователем
    """
    dp.register_message_handler(welcome_message, commands=["start"])
