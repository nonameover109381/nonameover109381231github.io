import telebot
import config
bot = telebot.TeleBot(config.token)
t = telebot.types
@bot.message_handler(commands = ['start'])
def welcome(message):
    texts = f"Hi {message.from_user.first_name} please choose lng"
    keyboard = t.InlineKeyboardMarkup(row_width=1)
    key1 = t.InlineKeyboardButton("UKR", callback_data='UKRA')
    keyboard.add(key1)
    bot.send_message(message.chat.id, texts, reply_markup=keyboard)
@bot.message_handler(content_types=['text'])
def firstweek (message):
    if message.text == "Розклад дзвінків":
        bot.send_message(message.chat.id, "1 пара    {8:00-9:20}\n"
                                          "2 пара   {9:40-11:00}\n"
                                          "3 пара  {11:20-12:40}\n"
                                          "4 пара  {13:00-14:20}\n"
                                          "5 пара  {14:40-16:00}\n"
                                          "6 пара  {16:20-17:40}\n"
                                          "7 пара  {18:00-19:20}\n"
                                          "8 пара  {19:40-21:00}\n")

    if message.text == "1 Тиждень":
        reply = t.InlineKeyboardMarkup(row_width=1)
        qwe1 = t.InlineKeyboardButton("понеділок", callback_data='monday')
        qwe2 = t.InlineKeyboardButton("вівторок", callback_data='tuesday')
        qwe3 = t.InlineKeyboardButton("середа", callback_data='wednesday')
        qwe4 = t.InlineKeyboardButton("четвер", callback_data='thursday')
        qwe5 = t.InlineKeyboardButton("п’ятниця", callback_data='friday')
        reply.add(qwe1, qwe2, qwe3, qwe4, qwe5)
        bot.send_message(message.chat.id, "Оберіть день, який вам потрібен",reply_markup=reply)
    if message.text == "2 Тиждень":
        repl = t.InlineKeyboardMarkup(row_width=1)
        qwe1 = t.InlineKeyboardButton("понеділок", callback_data='mnday')
        qwe2 = t.InlineKeyboardButton("вівторок", callback_data='tesday')
        qwe3 = t.InlineKeyboardButton("середа", callback_data='wdnesday')
        qwe4 = t.InlineKeyboardButton("четвер", callback_data='tursday')
        qwe5 = t.InlineKeyboardButton("п’ятниця", callback_data='fiday')
        repl.add(qwe1, qwe2, qwe3, qwe4, qwe5)
        bot.send_message(message.chat.id, "Оберіть день, який вам потрібен",reply_markup=repl)
    if message.text == 'Коди ClassRoom':
        bot.send_message(message.chat.id, "\nКоди Історія imczlti\n\n"
                                          "Історія практика ad2mpjr\n\n"
                                          "Вища математика 6a3cd7l \n\n"
                                          "Вища математика(практика) nuxymtk\n\n"
                                          "Код групи copgv3u  \n\n"
                                          "Інформаційні технології 3e7p5kv\n\n"
                                          "ІТ (практика, лаби, ІД) gkadefv\n\n"
                                          "ІТ   gkadefv\n\n"
                                          "1 курс лекціїї    БІ_ІТ    lvskwba\n\n"
                                          "Фізика jafgqin\n\n"
                                          "Фізика (1 група) brpo4j4\n\n"
                                          "Основи кібербезпеки 5daxmim\n\n"
                                          "Основи кібербезпеки практика h76sguk\n\n"
                                          "Основи автоматизованої обробки інформації 5cbxt7t\n\n"
                                          "Англійська для 1 підгрупи 3s3suje\n\n"
                                          "Англійська для 2 підгрупи 5kcfzrm\n\n"
                                          "СУМ лекції plfzrjt")
    if message.text == 'Посилання на Google Meet':
        bot.send_message(message.chat.id, "Вища математика лекції\n"
                                          "https://meet.google.com/lookup/eqq6l4krib?authuser=1&hs=179\n"
                                          "Вища математика практика\n"
                                          "https://meet.google.com/lookup/ae4zv5hsgx?authuser=1&hs=179\n"
                                          "Фізика лекції\n"
                                          "https://meet.google.com/lookup/hvug6sxjey?authuser=1&hs=179\n"
                                          "Фізика лаби 1 підгрупа\n"
                                          "https://meet.google.com/lookup/g3hxx5j3dn?authuser=1&hs=179\n"
                                          "Історія лекції\n"
                                          "https://meet.google.com/lookup/cxet7rz3fe?authuser=1&hs=179\n"
                                          "Історія практика\n"
                                          "https://meet.google.com/lookup/bbot7xtrzw?authuser=1&hs=179\n"
                                          "ОАОІ лекції\n"
                                          "https://meet.google.com/lookup/agiureeap4?authuser=1&hs=179\n"
                                          "ОАОІ лаби\n"
                                          "https://meet.google.com/lookup/em4rtbjtzq?authuser=1&hs=179\n"
                                          "ІТ лекції\n"
                                          "https://meet.google.com/lookup/a3k5jrp3fr?authuser=1&hs=179\n"
                                          "ІТ лаби та практики\n"
                                          "https://meet.google.com/lookup/dvywebor62?authuser=1&hs=179\n"
                                          "СУМ лекції\n"
                                          "https://meet.google.com/lookup/cqsxoo46zv?authuser=1&hs=179\n"
                                          "СУМ практика\n"
                                          "https://meet.google.com/lookup/fpijp2lofu?authuser=1&hs=179\n"
                                          "Англійська 1 підгрупа\n"
                                          "https://meet.google.com/lookup/ajlj362fft?authuser=1&hs=179\n"
                                          "Англійська 2 підгрупа\n"
                                          "https://meet.google.com/gtt-msxg-nxj?pli=1&authuser=1\n"
                                          "ОК практика\n"
                                          "https://meet.google.com/lookup/eircn6u4iq?authuser=1&hs=179\n")

@bot.callback_query_handler(func = lambda call: True)
def calllback(call):
    if call.data=='UKRA':
        key = t.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False, row_width=2)
        key1 = t.KeyboardButton("1 Тиждень")
        key2 = t.KeyboardButton("2 Тиждень")
        key3 = t.KeyboardButton("Посилання на Google Meet")
        key4 = t.KeyboardButton("Коди ClassRoom")
        key5 = t.KeyboardButton("Розклад дзвінків")
        key.add(key1, key2, key3, key4, key5)
        msg = bot.send_message(call.message.chat.id,'Оберіть потрібний тиждень', reply_markup=key)
        bot.register_next_step_handler(msg, firstweek)
    if call.data=='monday':
        bot.send_message(call.message.chat.id, '1)Основи кібербезпеки(практичне)(Яковенко.О.П)\n\n'
                                               '2)Основи кібербезпеки(практичне)(Яковенко.О.П)\n\n'
                                               '3)Фіичне виховання')
    if call.data=='tuesday':
        bot.send_message(call.message.chat.id, '1) (1группа) Інформаційні технології(лабараторна)(Дубчак.О.В)\n\n' 
                                               '     (2группа) Іноземна мова(практичне)(Шоріна.Т.Г)\n\n'
                         '2) Виша математика(практичне)(Варивода.В.О)\n\n'
                         '3) Виша математика(практичне)(Варивода.В.О)\n\n'
                         '4) Фізика(практичне)(Рудницька.Ж.О)'
        )
    if call.data=='wednesday':
        bot.send_message(call.message.chat.id, '1)--------------------------------------------\n\n'
                                               '2) Виша математика(лекція)(Денисюк.В.П)\n\n'
                                               '3) Іст України(лекція)(Кошетар.У.П)')
    if call.data=='thursday':
        bot.send_message(call.message.chat.id, '1) Фізика(лекція)(Рудницька.Ж.О)\n\n'
                                               '2) Виша математика(лекція)(Денисюк.В.П)\n\n'
                                               '3) (2группа)Фізика(лабараторна)(Рудницька.Ж.О)\n\n'
                                               '4) (2группа)Фізика(лабараторна)(Рудницька.Ж.О)'
                                               )
    if call.data=='friday':
        bot.send_message(call.message.chat.id, '1) Основи кібербезпеки(лекція)(Яковенко.О.П)\n\n'
                                               '2) Сучасна укр мова(лекція)(Дячук.Т.М)\n\n'
                                               '3) Сучасна укр мова(практичне)(Дячук.Т.М)\n\n'
                                               '4) (1группа)Іноземна мова(практичне)(Согратова.К.В)')
        #second week
    if call.data=='mnday':
        bot.send_message(call.message.chat.id, '1) Основи автоматизованої обробки інф(лекція)(Бурбела.О.О)\n\n'
                                               '2) Інформаційні технології(лекція)(Дубчак.О.В)\n\n'
                                               '3) Фізика(лабараторна)(Бордюг.Г.Б)\n\n'
                                               '4) Фізика(лабараторна)(Бордюг.Г.Б)\n\n'
                                               )
    if call.data=='tesday':
        bot.send_message(call.message.chat.id, '1) (1группа)Основи автоматизованої обробки інф(лабароторна)(Вишневська.Н.В)\n\n'
                                               '2) (1группа)Основи автоматизованої обробки інф(лабароторна)(Вишневська.Н.В)\n\n'
                                               '3) (1группа)Іноземна мова(практичне)(Согратова.К.В)\n'
                                               '   (2группа)Основи автоматизованої обробки інф(лабароторна)(Вишневська.Н.В)\n\n'
                                               '4) (2группа)Основи автоматизованої обробки інф(лабароторна)(Вишневська.Н.В)\n\n'
                                               '5) (2группа)Інформаційні технології(лабараторна)(Дубчак.О.В)')
    if call.data=='wdnesday':
        bot.send_message(call.message.chat.id, '1) --------------------------------------------\n\n'
                                               '2) (2группа) Іноземна мова(практичне)(Шоріна.Т.Г)\n\n'
                                               '3) Іст України(практичне)(Кошетар.У.П)\n\n'
                                               '4) Виша математика(практичне)(Варивода.В.О)\n\n'
                                               '5) Інформаційні технології(практичне)(Дубчак.О.В)\n\n'
                                               )
    if call.data=='tursday':
        bot.send_message(call.message.chat.id, '1) Фізика(лекція)(Рудницька.Ж.О)\n\n'
                                               '2) Виша математика(лекція)(Денисюк.В.П)\n\n'
                                               )
    if call.data=='fiday':
        bot.send_message(call.message.chat.id, '1)Основи кібербезпеки(лекція)(Яковенко.О.П)\n\n'
                                               '2)Основи кібербезпеки(лекція)(Яковенко.О.П)\n\n'
                                               )




bot.polling(none_stop   = True, interval = 0)