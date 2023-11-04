import telebot

# Установите токен вашего бота
TOKEN = '6983064353:AAEx7irKW8Cwbw5ji3HeANnElqOvWoS8pBU'

# Создайте объект бота
bot = telebot.TeleBot(TOKEN)

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def start(message):
    user = message.from_user
    markup = telebot.types.InlineKeyboardMarkup()

    # Создаем три инлайн-кнопки
    button1 = telebot.types.InlineKeyboardButton("Кнопка 1", callback_data='button_1')
    button2 = telebot.types.InlineKeyboardButton("Кнопка 2", callback_data='button_2')
    button3 = telebot.types.InlineKeyboardButton("Кнопка 3", callback_data='button_3')

    # Добавляем кнопки в разметку
    markup.row(button1, button2, button3)

    bot.send_message(message.chat.id, f'Привет, {user.first_name}! Выберите кнопку:', reply_markup=markup)

# Обработчик нажатия на инлайн-кнопку "Кнопка 1"
@bot.callback_query_handler(func=lambda call: call.data == 'button_1')
def button1_pressed(callback_query):
    bot.answer_callback_query(callback_query.id, text="Кнопка 1 нажата!")
    bot.send_message(callback_query.message.chat.id, "Вы нажали Кнопку 1")

# Обработчик нажатия на инлайн-кнопку "Кнопка 2"
@bot.callback_query_handler(func=lambda call: call.data == 'button_2')
def button2_pressed(callback_query):
    bot.answer_callback_query(callback_query.id, text="Кнопка 2 нажата!")
    bot.send_message(callback_query.message.chat.id, "Вы нажали Кнопку 2")

# Обработчик нажатия на инлайн-кнопку "Кнопка 3"
@bot.callback_query_handler(func=lambda call: call.data == 'button_3')
def button3_pressed(callback_query):
    bot.answer_callback_query(callback_query.id, text="Кнопка 3 нажата!")
    bot.send_message(callback_query.message.chat.id, "Вы нажали Кнопку 3")

# Запуск бота
if __name__ == '__main__':
    bot.polling(none_stop=True)
