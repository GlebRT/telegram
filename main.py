import telebot
from telebot import types
# Замените 'YOUR_BOT_TOKEN' на токен вашего бота
bot = telebot.TeleBot('6983064353:AAEx7irKW8Cwbw5ji3HeANnElqOvWoS8pBU')
user_product_info= {}
# Словарь для хранения фотографий, отправленных пользователем
user_photos = {}
user_text = {}
i = 1
k = 0
j = 0
media = {}
callback_status = {}
import random

@bot.callback_query_handler(func=lambda call: call.data == 'stop3')
def button2_pressed(callback_query):
    user_id = callback_query.message.chat.id

    # Вызываем функцию stop3
    stop3(callback_query.message)
    # Удаляем обработчик кнопки после выполнения
    bot.edit_message_reply_markup(user_id, callback_query.message.message_id, reply_markup=None)


def stop3(message):
    global valute
    valute = '₽'
    user_id = message.chat.id
    if user_photos != {}:
        c = len(user_photos[user_id])
        if len(user_photos[user_id]) > 10:
            markup2 = types.InlineKeyboardMarkup()
            button4 = types.InlineKeyboardButton("Готово! 📸", callback_data='stop3')
            markup2.add(button4)
            bot.send_message(user_id,f'<b>❌ Ошибка. Вы превысили лимит фотографий.</b>\n\nМаксимально кол-во 10 шт. Загрузите фото заново. Когда закончите <b>нажмите на кнопку "Готово"</b>',parse_mode='HTML',reply_markup= markup2)
            new1(message)
        elif len(user_photos[user_id]) == 0:
            markup2 = types.InlineKeyboardMarkup()
            button4 = types.InlineKeyboardButton("Готово! 📸", callback_data='stop3')
            markup2.add(button4)
            bot.send_message(user_id,'❌ Ошибка. Загрузите хотя бы одну фотографию. Когда закончите нажмите на кнопку "Готово"',parse_mode='HTML', reply_markup=markup2)
            new1(message)
        else:
            stop(message,c)
    else:
        markup2 = types.InlineKeyboardMarkup()
        button4 = types.InlineKeyboardButton("Готово! 📸", callback_data='stop3')
        markup2.add(button4)
        bot.send_message(user_id,'Ошибка. Загрузите хотя бы одну фотографию. Когда закончите нажмите на кнопку "Готово"',parse_mode='HTML',reply_markup=markup2)
        new1(message)
def stop(message,c):
    user_id = message.chat.id
    user_product_info[user_id] = {}  # Создаем пустой словарь для хранения информации о товаре
    if int(c) >= 5:
        so = "✅ Принято "+str(c)+" фотографий."
    elif 4 >= int(c) >= 2:
        so = "✅ Принято "+str(c)+" фотографии."
    elif int(c) == 1:
        so = "✅ Принята  "+str(c)+" фотография."
    bot.send_message(user_id, so,parse_mode='HTML')
    bot.register_next_step_handler(message, get_product_name)
    text4 = f'<b>📝 Введите название товара или его категорию</b>\n\nНапишите как можно точнее название товара, по нему покупатели будут искать ваше объявление среди множества других'
    bot.send_message(user_id,text4, parse_mode='html')


def get_product_name(message):
    user_id = message.from_user.id
    user_product_info[user_id]['name'] = message.text
    text4 = f'<b>💵 Введите цену товара</b>\n\nВводите только число, без наименования валюты.\n\nЕли вы не хотите указывать цену, чтобы договориться о ней с покупателем, введите /next\n\nВалюта по умолчаннию - Российский рубль, чтобы изменить введите /volute'
    bot.send_message(user_id,text4, parse_mode='html')
    bot.register_next_step_handler(message, get_product_price)
def get_product_name2(message):
    user_id = message.from_user.id
    text4 = f'<b>💵 Введите цену товара</b>\n\nВводите только число, без наименования валюты.\n\nЕли вы не хотите указывать цену, чтобы договориться о ней с покупателем, введите /next\n\nВалюта по умолчаннию - Российский рубль, чтобы изменить введите /volute'
    bot.send_message(user_id,text4, parse_mode='html')
    bot.register_next_step_handler(message, get_product_price)


# Функция для получения цены товара
def get_product_price(message):
    user_id = message.from_user.id
    user_product_info[user_id]['price'] = message.text
    if user_product_info[user_id]['price'] == '/volute':
        send_valute_buttons(message)
    elif user_product_info[user_id]['price'] == '/next':
        oshibka(message)
    else:
        try:
            float(message.text)
            text4 = f'📃<b> Введите описание товара.</b>\n\nРаспишите как можно точнее ваш товар. Будьте честны, не скрывайте дефектов и недочетов'
            bot.send_message(user_id,text4, parse_mode='html')
            bot.register_next_step_handler(message, get_product_description)
        except ValueError:
            bot.send_message(user_id, "Ошибка. Некорректная цена. Введите цену заново или пропустите этот шаг командой /next, тогда товар будет без указания цены")
            bot.register_next_step_handler(message, oshibka)
def oshibka(message):
    user_id = message.from_user.id
    k = message.text
    if k == "/next":
        user_product_info[user_id]['price'] = 'Не указана'
        text4 = f'📃 <b>Введите описание товара.</b>\n\nРаспишите как можно точнее ваш товар. Будьте честны, не скрывайте дефектов и недочетов'
        bot.send_message(user_id, text4, parse_mode='html')
        bot.register_next_step_handler(message, get_product_description)
    else:
        get_product_price(message)
# Функция для получения описания товара
def get_product_description(message):
    user_id = message.from_user.id
    user_product_info[user_id]['description'] = message.text
    gorod(message)

def get_product_description3(message):
    user_id = message.from_user.id
    text4 = f'<b>📞 Введите номер вашего телефна в формате 79998887766</b>\n\nВы также можете не указывать номер мобильного телефона, тогда покупатель сможет с вами связаться только в телеграме\n\n/next - пропустить и не указывать номер'
    bot.send_message(user_id, text4, parse_mode='html')
    bot.register_next_step_handler(message, get_product_number)

def gorod(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    buttons = ["Стерлитамак", "Салават", "Ишимбай", "Стерлитамакский р-н", "Ишимбайский р-н","Договорюсь с покупателем"]
    for currency in buttons:
        markup.add(types.KeyboardButton(currency))
    bot.send_message(message.chat.id, f'<b>📍 Выберете город, где сможете продать свой товар.</b>\n\nЕсли сможете доставить товар в другой город или район, выберите пункт "Договорюсь с покупателем"', parse_mode='html', reply_markup=markup)
    bot.register_next_step_handler(message, gorod2)
def gorod2(message):
    global gorodok
    v = message.text
    if v == 'Стерлитамак':
        gorodok ='г.Стерлитамак'
        get_product_description3(message)
    elif v == 'Салават':
        gorodok ='г.Салават'
        get_product_description3(message)
    elif v == 'Ишимбай':
        gorodok ='г.Ишимбай'
        get_product_description3(message)
    elif v == 'Стерлитамакский р-н':
        gorodok ='Стерлитамакский р-н'
        get_product_description3(message)
    elif v == 'Ишимбайский р-н':
        gorodok ='Ишимбайский р-н'
        get_product_description3(message)
    elif v == 'Договорюсь с покупателем':
        gorodok ='Договорюсь с покупателем'
        get_product_description3(message)
    else:
        bot.send_message(message.chat.id, "❌ Город или район не найден, повторите попытку")
        gorod(message)
def send_valute_buttons(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    buttons = ["Российский рубль", "Белорусский рубль", "Китайский Юань", "Азербайджан Манат", "Казахстан тенге", "Доллар", "Евро"]
    for currency in buttons:
        markup.add(types.KeyboardButton(currency))
    bot.send_message(message.chat.id, "Выберите валюту:", reply_markup=markup)
    bot.register_next_step_handler(message, send2)
def send2(message):
    global valute
    v = message.text
    if v == 'Российский рубль':
        valute ='₽'
        bot.send_message(message.chat.id, "✅ Валюта выбрана")
        get_product_name2(message)
    elif v == 'Белорусский рубль':
        valute ='BYN (респ.Белоруссия)'
        bot.send_message(message.chat.id, "✅ Валюта выбрана")
        get_product_name2(message)
    elif v == 'Китайский Юань':
        valute ='¥'
        bot.send_message(message.chat.id, "✅ Валюта выбрана")
        get_product_name2(message)
    elif v == 'Азербайджан Манат':
        valute ='AZN (Азербайджан)'
        bot.send_message(message.chat.id, "✅ Валюта выбрана")
        get_product_name2(message)
    elif v == 'Казахстан тенге':
        valute ='₸'
        bot.send_message(message.chat.id, "✅ Валюта выбрана")
        get_product_name2(message)
    elif v == 'Доллар':
        valute ='$'
        bot.send_message(message.chat.id, "✅ Валюта выбрана")
        get_product_name2(message)
    elif v == 'Евро':
        valute ='€'
        bot.send_message(message.chat.id, "✅ Валюта выбрана")
        get_product_name2(message)
    elif v == '/next':
        oshibka(message)
    else:
        bot.send_message(message.chat.id, "❌ Валюта не найдена, повторите попытку")
        send_valute_buttons(message)
# Функция для получения номера товара и отправки информации в канал
def get_product_number(message):
    global combined_message
    global text_captha
    global k
    global user_link
    global valute
    k = {}
    user_id = message.from_user.id
    user_product_info[user_id]['number'] = message.text
    product_info = user_product_info[user_id]
    phone_number = product_info['number']
    if len(phone_number) == 11 and phone_number[0]=='7' or phone_number=='/next':
        if phone_number == '/next':
            user_product_info[user_id]['number'] = 'Не указан'
        else:
            formatted_number = f"+{phone_number[0]}({phone_number[1:4]}){phone_number[4:7]}-{phone_number[7:9]}-{phone_number[9:]}"
            user_product_info[user_id]['number'] = formatted_number
        user_link = f"@{message.from_user.username}"
        if "Не указана" in user_product_info[user_id]['price']:
            valute = ''
        combined_message = f"{product_info['name']}\n\nЦена: {product_info['price']} {valute}\n\nОписание: {product_info['description']}\n\nНомер: {product_info['number']}\n\nГеолокация: {gorodok}\n\nАвтор: {user_link}"
        bot.send_message(user_id, '✅ Данные успешно собраны. Отгадайте капчу, чтобы подтвердить, что вы не робот:')
        random_num = random.randint(1, 5)
        if random_num == 1:
            captha = open('./1.png', 'rb')
            bot.send_photo(user_id, captha)
            text_captha = 'HY4NM'
            bot.register_next_step_handler(message, public1)
        if random_num == 2:
            captha = open('./2.png', 'rb')
            bot.send_photo(user_id, captha)
            text_captha = 'XRVSH'
            bot.register_next_step_handler(message, public1)
        if random_num == 3:
            captha = open('./3.png', 'rb')
            bot.send_photo(user_id, captha)
            text_captha = 'B4T9S'
            bot.register_next_step_handler(message, public1)
        if random_num == 4:
            captha = open('./4.png', 'rb')
            bot.send_photo(user_id, captha)
            text_captha = 'BR8X6'
            bot.register_next_step_handler(message, public1)
        if random_num == 5:
            captha = open('./5.png', 'rb')
            bot.send_photo(user_id, captha)
            text_captha = 'HAPK3'
            bot.register_next_step_handler(message, public1)
    else:
        bot.send_message(user_id, f"<b>Номер или команда не распознана</b>", parse_mode='HTML')
        get_product_description(message)

def public1(message):
    k = message.text
    user_id = message.from_user.id
    if k == text_captha:
        public(message)
    else:
        bot.send_message(user_id, f"<b>Вы не разгадали капчу. Повторите попытку...</b>", parse_mode='HTML')


def public(message):
    global combined_message
    global media
    global j
    global user_link2
    user_id = message.from_user.id
    if user_id in user_photos:
        try:
            photos = user_photos[user_id]
            media = [telebot.types.InputMediaPhoto(photo) for photo in photos]
            media[0].caption = combined_message
            bot.send_media_group(user_id, media)
            markup = types.InlineKeyboardMarkup()
            button3 = types.InlineKeyboardButton("Опубликовать ✅", callback_data='public')
            user_link2 = "@" + message.from_user.username
            markup.add(button3)
            txt = f'<b>Пожалуйта, проверьте объявление.</b>\n\nЕсли все верно  нажмите на кнопку "Опубликовать", чтобы отправить объявление на проверку.'
            combined_message += f'\n\nПодать объявление: @strdos_bot'
            media[0].caption = combined_message
            sozd = open('./prov.png', 'rb')
            bot.send_photo(user_id, sozd, caption=txt, parse_mode='HTML', reply_markup=markup)
        except telebot.apihelper.ApiException as e:
            txt = f'Ошибка. Время на публикацию истекло либо вы не заполнили важные пункты объявления. Вернитесь и повторите попытку.'
            bot.send_message(user_id, txt, parse_mode='html')

def public2(message):
    global media
    global valute
    global i
    user_id = message.chat.id
    channel_id = "-1002000529708"  # Замените на ваш реальный канал
    if media == {}:
        if user_link != user_link2:
            txt = f'Ошибка. Время на публикацию истекло либо вы не заполнили важные пункты объявления. Вернитесь и повторите попытку.'
            bot.send_message(user_id, txt, parse_mode='html')
    elif (user_link == user_link2) and (media != {}):
        if user_id in user_photos:
            try:
                photos = user_photos[user_id]
                product_info = user_product_info[user_id]
                combined_message = f"ID:{i}\n\n{product_info['name']}\n\nЦена: {product_info['price']} {valute}\n\nОписание: {product_info['description']}\n\nНомер: {product_info['number']}\n\nГеолокация: {gorodok}\n\nАвтор: {user_link}\n\nПодать объявление: @strdos_bot"
                media = [telebot.types.InputMediaPhoto(photo) for photo in photos]
                media[0].caption = combined_message
                bot.send_media_group(channel_id, media)
                bot.send_message(channel_id, f'👀 Проверьте объявление, если все верно перешлите в основной канал, <b>после чего удалите это сообщение</b>', parse_mode='html')
                file2 = open('./public.png', 'rb')
                text4 = f'<b>✅ Отлично! Ваше объявление успешно создано.</b>\n\nМодераторы спешут его проверять. Если все соответствует правилам, то его опубликуют в <a href="https://t.me/str_doska">телеграмм канале</a> в ближайшее время, в противном случае с вами свяжется модератор и уточнит, что стоит изменить.\n\n<b>Когда продадите свой товар, не забудьте убрать объявление с публикации.</b> Сделать это можно спомощью соответствующей кнопки в стартовом сообщении (/start)\n\n@strdos_bot'
                markup = types.InlineKeyboardMarkup()
                button3 = types.InlineKeyboardButton("🔙 вернуться в главное меню", callback_data='back')
                button1 = types.InlineKeyboardButton("Участвовать в опросе 📊",url='https://docs.google.com/forms/d/e/1FAIpQLSeIvBYm_gc33u91eh70TtQf9xX8imFfmu6fkXqD_nRdbEE57Q/viewform?usp=sf_link')
                markup.add(button1)
                markup.add(button3)
                bot.send_photo(user_id, file2, caption=text4, parse_mode='html', reply_markup=markup)
                media = {}
                i+=1
                valute = '₽'
            except telebot.apihelper.ApiException as e:
                txt = f'❌ Ошибка. Время на публикацию истекло либо вы не заполнили важные пункты объявления. Вернитесь и повторите попытку.'
                bot.send_message(user_id, txt, parse_mode='html')
    else:
        txt = f'❌ Ошибка. Время на публикацию истекло либо вы не заполнили важные пункты объявления. Вернитесь и повторите попытку.'
        bot.send_message(user_id, txt, parse_mode='html')
@bot.callback_query_handler(func=lambda call: call.data == 'new')
def new(callback_query):
    user_id = callback_query.message.chat.id
    bot.send_message(user_id, f'<b>Открытие конструктора...</b>', parse_mode='HTML')
    markup = types.InlineKeyboardMarkup()
    button3 = types.InlineKeyboardButton("Правила публикации ✅", url='https://t.me/lavka_str/472')
    markup.add(button3)
    sozd = open('./new.png', 'rb')
    txt = f'<b>Создание нового объявления.</b>\n\nПеред началом рекомендуем ознакомиться с <a href="https://t.me/lavka_str/472">инструкцией и правилами</a>, чтобы исключить неприятные моменты.'
    bot.send_photo(user_id, sozd, caption=txt, parse_mode='HTML', reply_markup=markup)
    bot.edit_message_reply_markup(user_id, callback_query.message.message_id, reply_markup=None)
    new2(callback_query.message)

def new2(message):
    user_id = message.chat.id
    markup2 = types.InlineKeyboardMarkup()
    button4 = types.InlineKeyboardButton("Готово! 📸", callback_data='stop3')
    markup2.add(button4)
    txt2 = f"<b>Отправьте фото вашего товара (до 10 шт.)\n\n</b> Рекомендуем делать фото в хорошем качестве и в овещенном месте, так покупателю будет легче определить визуальное состояние.\n\n<b>Когда загрузите фотографии нажмите на кнопку ниже, чтобы продолжить.</b>"
    bot.send_message(user_id,txt2, parse_mode='HTML',reply_markup=markup2)
    new1(message)


@bot.message_handler(commands=['new'])
def new1(message):
    user_id = message.chat.id
    user_photos[user_id] = []


@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.chat.id
    file = open('./start.png', 'rb')
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton("Создать объявление 📣", callback_data='new')
    button2 = types.InlineKeyboardButton("Снять объявление ❎", callback_data='delete')
    button4 = types.InlineKeyboardButton("Поддержка 🔧", callback_data='podd')
    button5 = types.InlineKeyboardButton("ТG канал 👥", url='https://t.me/lavka_str')
    markup.add(button1)
    markup.add(button2)
    markup.add(button4,button5)
    # Отправляем сообщение с прикрепленной кнопкой
    if message.from_user.first_name == None or message.from_user.last_name == None:
        message.from_user.first_name == ''
        message.from_user.last_name == ''
    text = f'&#128075; <b>Добро пожаловать в бота объявлений, {message.from_user.first_name} {message.from_user.last_name}!</b>\n\n&#128227; <b>Стр</b>Лавка - это проект для размещения ваших объявлений о продаже товаров/услуг для жителей городов: Стерлитамак, Салават, Ишимбай. \n\n&#9989; Чтобы создать объявление нажмите на соответствующую кнопку снизу.\n\n	&#128683; Пожалуйста, помните о том, что объявления должны соответствовать <a href="https://t.me/lavka_str/472">нормам и правилам</a>.\n\n&#128100; Спасибо, что выбрали наш проект для размещения объявлений. Желаем вам удачи и успехов в продажах!\n\n@strdos_bot'
    bot.send_photo(user_id, file, caption = text, parse_mode='html', reply_markup=markup)
# Функция для обработки нажатия на кнопку
def start_delete(message):
    global text_captha
    user_id = message.chat.id
    random_num = random.randint(1, 5)
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton("🔙 вернуться в главное меню", callback_data='back')
    markup.add(button1)
    text6 = f'<b>Пожалуйста, разгадайте капчу.</b>'
    if random_num == 1:
        captha = open('./1.png', 'rb')
        bot.send_photo(user_id, captha, caption=text6, reply_markup=markup, parse_mode='html')
        text_captha = 'HY4NM'
        bot.register_next_step_handler(message, forward_message)
    if random_num == 2:
        captha = open('./2.png', 'rb')
        bot.send_photo(user_id, captha, caption=text6, reply_markup=markup, parse_mode='html')
        text_captha = 'XRVSH'
        bot.register_next_step_handler(message, forward_message)
    if random_num == 3:
        captha = open('./3.png', 'rb')
        bot.send_photo(user_id, captha, caption=text6, reply_markup=markup, parse_mode='html')
        text_captha = 'B4T9S'
        bot.register_next_step_handler(message, forward_message)
    if random_num == 4:
        captha = open('./4.png', 'rb')
        bot.send_photo(user_id, captha, caption=text6, reply_markup=markup, parse_mode='html')
        text_captha = 'BR8X6'
        bot.register_next_step_handler(message, forward_message)
    if random_num == 5:
        captha = open('./5.png', 'rb')
        bot.send_photo(user_id, captha, caption=text6, reply_markup=markup, parse_mode='html')
        text_captha = 'HAPK3'
        bot.register_next_step_handler(message, forward_message)

def forward_message(message):
    captha = message.text
    if captha == text_captha:
        ss = open('./13.png', 'rb')
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("Перейти в телеграм-канал",
                                             url='https://t.me/lavka_str')
        markup.add(button1)
        txt2 = f'<b>Отправьте ссылку на ваше объявление из телеграм-канала.</b>\n\nВ прикрепленном фото выше, показано как это сделать.'
        bot.send_photo(message.chat.id,ss,caption=txt2,parse_mode='html',reply_markup=markup)
        bot.register_next_step_handler(message, forward_message23)
    else:
        start_delete(message)

def forward_message23(message):
    message_id = message.text
    link ='https://t.me/lavka_str/'
    if link in message_id:
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("Участвовать в опросе 📊", url='https://docs.google.com/forms/d/e/1FAIpQLSeIvBYm_gc33u91eh70TtQf9xX8imFfmu6fkXqD_nRdbEE57Q/viewform?usp=sf_link')
        markup.add(button1)
        konec = open('./konec.png','rb')
        button2 = types.InlineKeyboardButton("🔙 вернуться в главное меню", callback_data='back')
        markup.add(button2)
        bot.send_photo(message.chat.id, konec ,caption =f'<b>✅ Заявка на удаление отправлена.</b>\n\nМодераторы проверяют вашу заявку. Если объявление принадлежит вам, его удалят.\n\nСпасибо, что воспользовались нашими услугами.\n\nБудем благодарны если вы <b>примите участие в опросе.</b>',parse_mode='html', reply_markup=markup)
        channel_id = "-1002000529708"
        message_id2 = f'🗑️ Пользователь @{message.from_user.username} просит удалить объявление: {message_id}\n\n<b>Если ник пользователя отличается от ника в объявлении, удалять объявление запрещено.</b>'
        bot.send_message(channel_id, message_id2, parse_mode='html', disable_web_page_preview=True)
    else:
        txt2 = f'<b>❌ Ошибка. Вствленная вами сылка не указывает на объявление телеграм-канала</b>\n\nОтправьте ссылку заново, если не получаетя <b>обратитесь в <a href="https://t.me/modern_str">поддержку</a></b>'
        bot.send_message(message.chat.id, txt2, parse_mode='HTML',disable_web_page_preview=True)
        forward_message(message)


def podd(message):
    global text_captha
    user_id = message.chat.id
    random_num = random.randint(1, 5)
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton("🔙 вернуться", callback_data='back')
    markup.add(button1)
    text6 = f'<b>Пожалуйста, разгадайте капчу.</b>'
    if random_num == 1:
        captha = open('./1.png', 'rb')
        bot.send_photo(user_id, captha, caption=text6, reply_markup=markup,parse_mode='html')
        text_captha = 'HY4NM'
        bot.register_next_step_handler(message, podd2)
    if random_num == 2:
        captha = open('./2.png', 'rb')
        bot.send_photo(user_id, captha, caption=text6, reply_markup=markup,parse_mode='html')
        text_captha = 'XRVSH'
        bot.register_next_step_handler(message, podd2)
    if random_num == 3:
        captha = open('./3.png', 'rb')
        bot.send_photo(user_id, captha, caption=text6, reply_markup=markup,parse_mode='html')
        text_captha = 'B4T9S'
        bot.register_next_step_handler(message, podd2)
    if random_num == 4:
        captha = open('./4.png', 'rb')
        bot.send_photo(user_id, captha, caption=text6, reply_markup=markup,parse_mode='html')
        text_captha = 'BR8X6'
        bot.register_next_step_handler(message, podd2)
    if random_num == 5:
        captha = open('./5.png', 'rb')
        bot.send_photo(user_id, captha, caption=text6, reply_markup=markup,parse_mode='html')
        text_captha = 'HAPK3'
        bot.register_next_step_handler(message, podd2)

def podd2(message):
    captha = message.text
    if captha == text_captha:
        bot.send_message(message.chat.id, f'<b>Опишите свою проблему.</b>\n\nС вами свяжется поддержка и поможет её решить.', parse_mode='html')
        bot.register_next_step_handler(message, forward_message2)
    else:
        start_delete(message)
def podd5(message):
    bot.send_message(message.chat.id, f'❌ Ошибка. Напишите обращение длиной более 10 символов', parse_mode='html')
    bot.register_next_step_handler(message, forward_message2)

def forward_message2(message):
    message_id = message.text
    if message_id != None:
        if len(message_id) >= 10:
            markup = types.InlineKeyboardMarkup()
            button5 = types.InlineKeyboardButton("Написать самостоятельно", url='https://t.me/modern_str')
            markup.add(button5)
            button1 = types.InlineKeyboardButton("🔙 вернуться в главное меню", callback_data='back')
            markup.add(button1)
            ss2 = open('./14.png', 'rb')
            bot.send_photo(message.chat.id,ss2 ,caption=f'<b>✅ Ваше обращение перенапрвлено в поддержку.</b>\n\nС вами свяжутся при первой возможности.',reply_markup=markup, parse_mode='html')
            channel_id = "-1002000529708"
            message_id2 = f'🟠 ' \
                          f'Пользователь @{message.from_user.username} обратился с проблемой: {message_id}\n\n<b>Если проблема решена удалите сообщение</b>'
            bot.send_message(channel_id, message_id2, parse_mode='html', disable_web_page_preview=True)
        else:
            podd5(message)
    else:
        podd5(message)
@bot.callback_query_handler(func=lambda call: call.data == 'public')
def button6_pressed(callback_query):
    user_id = callback_query.message.chat.id
    # Вызываем функцию stop3
    public2(callback_query.message)
    # Удаляем обработчик кнопки после выполнения
    bot.edit_message_reply_markup(user_id, callback_query.message.message_id, reply_markup=None)
@bot.callback_query_handler(func=lambda call: call.data == 'podd')
def button6_pressed3(callback_query):
    user_id = callback_query.message.chat.id
    # Вызываем функцию stop3
    podd(callback_query.message)
    # Удаляем обработчик кнопки после выполнения
    bot.edit_message_reply_markup(user_id, callback_query.message.message_id, reply_markup=None)
@bot.callback_query_handler(func=lambda call: call.data == 'delete')
def button64_pressed3(callback_query):
    user_id = callback_query.message.chat.id
    # Вызываем функцию stop3
    start_delete(callback_query.message)
    # Удаляем обработчик кнопки после выполнения
    bot.edit_message_reply_markup(user_id, callback_query.message.message_id, reply_markup=None)
@bot.callback_query_handler(func=lambda call: call.data == 'back')
def button644_pressed3(callback_query):
    user_id = callback_query.message.chat.id
    # Вызываем функцию stop3
    start(callback_query.message)
    # Удаляем обработчик кнопки после выполнения
    bot.edit_message_reply_markup(user_id, callback_query.message.message_id, reply_markup=None)

@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    user_id = message.chat.id
    if user_id in user_photos:
        user_photos[user_id].append(message.photo[-1].file_id)

@bot.message_handler(func=lambda message: True, content_types=['text'])
def handle_text(message):
    user_id = message.from_user.id
    user_text[user_id] = message.text
# Функция для обработки полученных фотографий

# Запускаем бота
if __name__ == '__main__':
    bot.polling(none_stop=True)
