from aiogram import Bot, Dispatcher, executor, types

bot = Bot('7026071943:AAEYmXludjxwnIXD24gUa8oX1xeGhno6up0')
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
	markup = types.ReplyKeyboardMarkup()
	markup.add(types.ReplyKeyboardMarkup('Web App', web_app=WebAppInfo(url='https://www.google.com')))
	await message.answer('Привет, мой друг!', reply_markup=markup)
 
executor.start_polling(dp)