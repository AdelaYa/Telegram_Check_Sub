
from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN, CHANNEL_ID


NOTSUB_MESSAGE = "Для дальнейшей работы бота , подпишитесь на канал @rericomtest"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


def check_sub_channel(chat_member):
    if chat_member['status'] != 'left':
        return True
    else:
        return False


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    if check_sub_channel(await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)):
        await bot.send_message(message.from_user.id, "Привет. Спасибо за подписку на канал!")
    else:
        await bot.send_message(message.from_user.id, NOTSUB_MESSAGE)

if __name__ == '__main__':
    executor.start_polling(dp)

