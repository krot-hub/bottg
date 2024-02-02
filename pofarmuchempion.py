import telebot  # импорт библиотек
from telebot import types  # для использования кнопок

bot = telebot.TeleBot('6592250235:AAHvpO3dPK12DXVzayFc0KoQmf7DF5LMHfg')  # токен бота в кавычках


@bot.message_handler(commands=['start'])  # начало работы бота
def start(ramzes):  # на выбор пользователю даётся 7 опций
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton("Задания 1-5")
    btn2 = types.KeyboardButton("Задание 8")
    btn3 = types.KeyboardButton("Задания 9, 13")
    btn4 = types.KeyboardButton("Задание 10")
    btn5 = types.KeyboardButton("Задания 11, 22")
    btn6 = types.KeyboardButton("Задание 14")
    btn7 = types.KeyboardButton("Геометрия")
    markup.add(btn1)
    markup.add(btn2)
    markup.row(btn3)
    markup.add(btn4)
    markup.add(btn5)
    markup.row(btn6)
    markup.add(btn7)

    bot.send_message(ramzes.chat.id,
                     f"Здравствуйте, {ramzes.from_user.first_name}! Прошу Вас выбрать один из представленных пунктов.",
                     reply_markup=markup)
    bot.register_next_step_handler(ramzes, step2)


def step2(ramzes):  # следующий шаг, пользователь выбрал задание
    if ramzes.text == "Задания 1-5":  # пользователь выбрал пункт 'Задания 1-5', далее на выбор даётся несколько типов этих заданий
        markup = types.ReplyKeyboardMarkup()
        btn2 = types.KeyboardButton("Шины")
        btn3 = types.KeyboardButton("Мобильный оператор")
        btn4 = types.KeyboardButton("Листы формата А")
        btn5 = types.KeyboardButton("Печи")
        btn1 = types.KeyboardButton("Вернуться назад")

        markup.add(btn2)
        markup.add(btn3)
        markup.add(btn4)
        markup.add(btn5)
        markup.add(btn1)

        bot.send_message(ramzes.chat.id,
                         f"{ramzes.from_user.first_name}, прошу Вас выбрать один из типов заданий.",
                         reply_markup=markup)

        def step3(ramzes):  # следующий шаг, после выбора 'Задания 1-5' пользователь выбрал тип задания, либо захотел вернуться назад

            if ramzes.text == 'Вернуться назад':  # возврат к выбору задания
                markup = types.ReplyKeyboardMarkup()
                btn1 = types.KeyboardButton("Задания 1-5")
                btn2 = types.KeyboardButton("Задание 8")
                btn3 = types.KeyboardButton("Задания 9, 13")
                btn4 = types.KeyboardButton("Задание 10")
                btn5 = types.KeyboardButton("Задания 11, 22")
                btn6 = types.KeyboardButton("Задание 14")
                btn7 = types.KeyboardButton("Геометрия")
                markup.add(btn1)
                markup.add(btn2)
                markup.row(btn3)
                markup.add(btn4)
                markup.add(btn5)
                markup.row(btn6)
                markup.add(btn7)

                bot.send_message(ramzes.chat.id,
                                 f"Здравствуйте, {ramzes.from_user.first_name}! Прошу Вас выбрать один из представленных пунктов.",
                                 reply_markup=markup)
                bot.register_next_step_handler(ramzes, step2)
            elif ramzes.text == 'Шины':  # пользователь выбрал определённый тип задания, ему присылаются файлы с формулами, он может вернуться к выбору задания (start) с помощью нажатия кнопки 'Выбор задания'
                file1 = open('./diametr.png', 'rb')
                file2 = open('./duga.png', 'rb')
                file3 = open('./percents.png', 'rb')
                markup = types.ReplyKeyboardMarkup()
                btn1 = types.KeyboardButton("Вернуться к выбору задания")
                markup.add(btn1)

                bot.send_photo(ramzes.chat.id, file1, reply_markup=markup)
                bot.send_photo(ramzes.chat.id, file2, reply_markup=markup)
                bot.send_photo(ramzes.chat.id, file3, reply_markup=markup)
                bot.register_next_step_handler(ramzes, start)
            elif ramzes.text == 'Мобильный оператор':

                file1 = open('./tarif.png', 'rb')

                markup = types.ReplyKeyboardMarkup()
                btn1 = types.KeyboardButton("Вернуться к выбору задания")
                markup.add(btn1)
                bot.register_next_step_handler(ramzes, start)

                bot.send_photo(ramzes.chat.id, file1, reply_markup=markup)
            elif ramzes.text == 'Листы формата А':

                file1 = open('./formatA.png', 'rb')
                file2 = open('./pifagor.png', 'rb')

                markup = types.ReplyKeyboardMarkup()
                btn1 = types.KeyboardButton("Вернуться к выбору задания")
                markup.add(btn1)
                bot.register_next_step_handler(ramzes, start)

                bot.send_photo(ramzes.chat.id, file1, reply_markup=markup)
                bot.send_photo(ramzes.chat.id, file2, reply_markup=markup)
            elif ramzes.text == 'Печи':

                file1 = open('./parallelepiped.jpg', 'rb')
                file2 = open('./pifagor.png', 'rb')

                markup = types.ReplyKeyboardMarkup()
                btn1 = types.KeyboardButton("Вернуться к выбору задания")
                markup.add(btn1)
                bot.register_next_step_handler(ramzes, start)

                bot.send_photo(ramzes.chat.id, file1, reply_markup=markup)
                bot.send_photo(ramzes.chat.id, file2, reply_markup=markup)

        bot.register_next_step_handler(ramzes, step3)
    elif ramzes.text == 'Задание 8':  # пользователь выбрал задание, ему присылаются файлы с формулами, он может вернуться к выбору задания (start) с помощью нажатия кнопки 'Вернуться назад'
        file1 = open('./stepeni.jpg', 'rb')

        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton("Вернуться назад")
        markup.add(btn1)
        bot.register_next_step_handler(ramzes, start)
        bot.send_photo(ramzes.chat.id, file1, reply_markup=markup)

    elif ramzes.text == 'Задание 10':

        file1 = open('./veroyatnost2.jpg', 'rb')
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton("Вернуться назад")
        markup.add(btn1)
        bot.register_next_step_handler(ramzes, start)
        bot.send_photo(ramzes.chat.id, file1, reply_markup=markup)

    elif ramzes.text == 'Задания 9, 13':
        file1 = open('./discriminant.png', 'rb')
        file2 = open('./viet.jpg', 'rb')
        file3 = open('./fsu.jpg', 'rb')
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton("Вернуться назад")
        markup.add(btn1)
        bot.register_next_step_handler(ramzes, start)
        bot.send_photo(ramzes.chat.id, file1, reply_markup=markup)
        bot.send_photo(ramzes.chat.id, file2, reply_markup=markup)
        bot.send_photo(ramzes.chat.id, file3, reply_markup=markup)
    elif ramzes.text == 'Задания 11, 22':
        file1 = open('./grafiki.jpeg', 'rb')
        file2 = open('./grafikpryam.jpg', 'rb')
        file3 = open('./grafikkvad.png', 'rb')
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton("Вернуться назад")
        markup.add(btn1)
        bot.register_next_step_handler(ramzes, start)
        bot.send_photo(ramzes.chat.id, file1, reply_markup=markup)
        bot.send_photo(ramzes.chat.id, file2, reply_markup=markup)
        bot.send_photo(ramzes.chat.id, file3, reply_markup=markup)
    elif ramzes.text == 'Задание 14':
        file1 = open('./progress2.jpg', 'rb')
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton("Вернуться назад")
        markup.add(btn1)
        bot.register_next_step_handler(ramzes, start)
        bot.send_photo(ramzes.chat.id, file1, reply_markup=markup)
    elif ramzes.text == 'Геометрия':
        file1 = open('./treugs.jpg', 'rb')
        file2 = open('./pifagor.png', 'rb')
        file3 = open('./paral-m.png', 'rb')
        file4 = open('./romb.jpg', 'rb')
        file5 = open('./s_pryam.png', 'rb')
        file6 = open('./krugi.jpeg', 'rb')
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton("Вернуться назад")
        markup.add(btn1)
        bot.register_next_step_handler(ramzes, start)
        bot.send_photo(ramzes.chat.id, file1, reply_markup=markup)
        bot.send_photo(ramzes.chat.id, file2, reply_markup=markup)
        bot.send_photo(ramzes.chat.id, file3, reply_markup=markup)
        bot.send_photo(ramzes.chat.id, file4, reply_markup=markup)
        bot.send_photo(ramzes.chat.id, file5, reply_markup=markup)
        bot.send_photo(ramzes.chat.id, file6, reply_markup=markup)


@bot.message_handler()
def privet(ramzes):  # если пользователь не нажмёт на старт, а решит написать 'привет'
    if ramzes.text.lower() == "привет":
        bot.send_message(ramzes.chat.id,
                         f"Здравствуйте, {ramzes.from_user.first_name}! Чтобы начать использовать функционал бота, введите команду '/start'.")


bot.polling(none_stop=True)  # чтобы программа не завершалась мгновенно
