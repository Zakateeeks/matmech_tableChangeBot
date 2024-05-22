from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder

def choice_mode() -> InlineKeyboardBuilder:
    """
    Кнопка выбора режима работы с таблицей.
    Привязана к стартовому сообщению.

    - Режим "Приёмка" представляет собой редактирование таблицы
      со стандартной настройкой расположения данных для редактирования.

    - Режим "Свой режим" позволяет пользователю собственноручно настроить что
      и как он хочет изменить.

    :return: inline keyboard
    """

    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="УрФУ",
        callback_data="ok_urfu_mode")
    )
    builder.add(types.InlineKeyboardButton(
        text="Свои настройки",
        callback_data="individual_mode")
    )

    return builder
