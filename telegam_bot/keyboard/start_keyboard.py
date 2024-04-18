from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def choice_mode() -> InlineKeyboardMarkup:
    """
    Кнопка выбора режима работы с таблицей.
    Привязана к стартовому сообщению.

    - Режим "Приёмка" представляет собой редактирование таблицы
      со стандартной настройкой расположения данных для редактирования.

    - Режим "Свой режим" позволяет пользователю собственноручно настроить что
      и как он хочет изменить.

    :return: inline keyboard
    """

    keyboard = InlineKeyboardMarkup(row_width=2)

    keyboard.add(
        InlineKeyboardButton(text="Приёмка", callback_data="ok_urfu"),
        InlineKeyboardButton(text="Свой режим", callback_data="individual_mode")
    )

    return keyboard
