from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from tg_bot.config import BOT_TOKEN
from tg_bot.handlers.other import register_other
from tg_bot.handlers.user import register_user
from tg_bot.config import POSTGRES_URL
from tg_bot.database.models import db


def register_all_middlewares(dp):
    pass


def register_all_filters(dp):
    pass


def register_all_handlers(dp):
    register_user(dp)

    register_other(dp)


async def on_startup(dp):
    await db.set_bind(POSTGRES_URL)
    await db.gino.create_all()
    print('Bot started!')


def main():
    storage = MemoryStorage()
    bot = Bot(token=BOT_TOKEN, parse_mode='HTML')
    dp = Dispatcher(bot, storage=storage)

    register_all_middlewares(dp)
    register_all_filters(dp)
    register_all_handlers(dp)

    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)


if __name__ == '__main__':
    main()


