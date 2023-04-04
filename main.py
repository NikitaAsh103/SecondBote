from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton
import markup as nav
from config import TOKEN
import functions

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
   await bot.send_message(message.from_user.id, "Привет {0.first_name}!\nЯ Бот от Ащика!\n"
                                                "Я создан для отработки решения математики начальных классов."
                                                "\nВыбери арифметическое действие которое ты хочешь отрабоать.".format(message.from_user)
                          , reply_markup=nav.mainMenu)


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("После выбора всех свойств я буду выдавать рандомные примеры, а тебе их нужно будет решать!")


@dp.message_handler()
async def func(message):



    if (message.text == "➕ Cложение"):
        await bot.send_message(message.chat.id, text="Вы выбрали арифметическое действие сложение \nВыберите количество примеров?",
                              reply_markup=nav.quantityQue )
        return

    if (message.text == "➖ Вычитание"):
        await bot.send_message(message.chat.id, text="Вы выбрали арифметическое действие вычитание \nВыберите количество примеров?", reply_markup=nav.btnBack)
        return


    if (message.text == "✖️ Умножение"):
        await bot.send_message(message.chat.id,text="Вы выбрали арифметическое действие умножение \nВыберите количество примеров?", reply_markup=nav.btnBack)
        return

    if (message.text == "➗ Деление"):
        await bot.send_message(message.chat.id,text="Вы выбрали арифметическое действие деление \nВыберите количество примеров?", reply_markup=nav.btnBack)
        return

    if (message.text == "Рандомное арифметическое действие"):
        await bot.send_message(message.chat.id,text="Вы выбрали рандомное арифметическое действие \nВыберите количество примеров?", reply_markup=nav.btnBack)
        return

    if (message.text == "🔙"):
        await bot.send_message(message.chat.id,text="Вы выбрали действие назад",reply_markup=nav.mainMenu)
        return

    else:
        await bot.send_message(message.chat.id, text="На такую комманду я не запрограммирован..")




if __name__ == '__main__':
    executor.start_polling(dp)