import asyncio
import logging

from aiogram import Bot, Dispatcher

from config import API_TOKEN
from handlers.change_table import table_router
from handlers.start_bot import start_router


async def main() -> None:
    """
    Старт бота, подключение файлов бота.
    """
    bot = Bot(token=API_TOKEN)
    dp = Dispatcher()
    dp.include_routers(start_router,
                       table_router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
