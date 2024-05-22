from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder


def mode_table_edit() -> InlineKeyboardBuilder:
    """
    Кнопки выборки абитуриентов по параметрам

    :return: inline keyboard
    """

    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="По баллам (убывание)",
        callback_data="point_low_mode")
    )
    builder.add(types.InlineKeyboardButton(
        text="По приоритетам",
        callback_data="priority_mode")
    )
    builder.add(types.InlineKeyboardButton(
        text="По баллам (с 210) возрастание",
        callback_data="point_up_mode")
    )
    builder.add(types.InlineKeyboardButton(
        text="По зелёным",
        callback_data="green_mode")
    )
    builder.add(types.InlineKeyboardButton(
        text="По неопределившимся",
        callback_data="yellow_mode")
    )

    builder.adjust(2)

    return builder
