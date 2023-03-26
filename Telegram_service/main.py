from tensor import handel_image
from dotenv import dotenv_values
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
from repository.func import set_user, is_exist_user

"""Settings"""
config = dotenv_values('.env')
TOKEN = config['TOKEN_API']

storage = MemoryStorage()
bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=storage)


class Queue(StatesGroup):
    photo = State()


"""Клавіатури та кнопки"""
start_kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
cancel_kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
cancel_but = types.KeyboardButton('Перервати процес')
kb1 = types.KeyboardButton('Інформація')
kb2 = types.KeyboardButton('Почати роботу')
start_kb.add(kb1).add(kb2)
cancel_kb.add(cancel_but)


@dp.message_handler(Text(equals='Інформація', ignore_case=True))
async def help_message(message: types.Message) -> None:
    await message.reply(text='Я - бот, що спеціалізується на розпізнаванні картинок, для користування натисніть на '
                             'клавіатурі "Почати роботу" та слідуйте подальшим інструкціям')


@dp.message_handler(commands=['start'])
async def start_message(message: types.Message) -> None:
    if not is_exist_user(message.from_user.id):
        set_user(user_id=message.from_user.id, first_name=message.from_user.first_name,
                 last_name=message.from_user.last_name)
    await message.answer(
        text='Вас вітає бот Samantha, для інструкції користування натисніть на клавіатурі "Інформація"',
        reply_markup=start_kb)


@dp.message_handler(Text(equals='Перервати процес', ignore_case=True), state='*')
async def cmd_cancel(message: types.Message, state: FSMContext) -> None:
    current_state = await state.get_state()
    if current_state is None:
        return

    await message.reply('Відмінив', reply_markup=start_kb)
    await state.finish()


@dp.message_handler(Text(equals='Почати роботу', ignore_case=True))
async def start_work(message: types.Message) -> None:
    await Queue.photo.set()
    await message.answer('Спочатку завантажте фотографію', reply_markup=cancel_kb)


@dp.message_handler(lambda message: not message.photo, state=Queue.photo)
async def check_photo(message: types.Message):
    return await message.reply(text='Це не фотографія')


@dp.message_handler(lambda message: message.photo, content_types=['photo'], state=Queue.photo)
async def check_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[-1].file_id
        print(data)
        file_id = data.get('photo')
        print(file_id)
        file = await bot.get_file(file_id)
        file_path = file.file_path
        file_bytes = await bot.download_file(file_path)
        answer = handel_image(file_bytes)

    await message.answer(text=f'Samantha розпізнала це фото як {answer}', reply_markup=start_kb)
    await state.finish()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
