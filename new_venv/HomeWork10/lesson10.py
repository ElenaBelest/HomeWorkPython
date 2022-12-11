def hello_command(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(f"Hi {update.effective_user.first_name}! I'm a prisoner of this bot."\
    "\n Hope you will help me to find freedom.")

def help_command(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(f"Hi {update.effective_user.first_name}!"\
    "\n I can tell you about myself."\
    "\nJust type /hello to know me better. \n"\
    "\n As well you can use following comands:"\
    "\n  /c <3 digit value code> to see currency of value e.g. USD or EUR>"
    "\n /w <city> Hope to see weather forecast for entered city")

def weather_command(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split() # /sum 123 534543
    city = items[1]
    update.message.reply_text(f'{Get_weather(city, Get_my_Weather_taken())}')

def currency_command(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text
    print(msg)
    currencyCode = context.args[0].upper()
    #msg.upper().split() # /sum 123 534543
    update.message.reply_text(f'{Get_currency(currencyCode)}')

def Calculator(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text
    print(msg)

    x = int(context.args[0])
    action = context.args[1]
    y = int(context.args[2])

    if action == "+":
        update.message.reply_text(f'{x} {action} {y} = {x + y}')
    elif action == "-":
        update.message.reply_text(f'{x} {action} {y} = {x - y}')
    elif action == "*":
        update.message.reply_text(f'{x} {action} {y} = {x * y}')
    elif action == "/":
        update.message.reply_text(f'{x} {action} {y} = {x / y}')

    #msg.upper().split() # /sum 123 534543

updater = Updater(Get_my_Tg_taken())

# обработка команды старт (создаем Inline клавиатуру)
def startCommand(update: Update, context: CallbackContext):
    buttonA = telegram.InlineKeyboardButton('Поздороваться', callback_data='buttonA')
    buttonB = telegram.InlineKeyboardButton('Help', callback_data='buttonB')
    buttonC = telegram.InlineKeyboardButton('weather', callback_data='buttonC')
    buttonD = telegram.InlineKeyboardButton('currency', callback_data='buttonD')
    buttonE = telegram.InlineKeyboardButton('calculator', callback_data='buttonE')

    markup = telegram.InlineKeyboardMarkup(inline_keyboard=[[buttonA], [buttonB], [buttonC], [buttonD], [buttonE]])

    update.message.reply_text('Добрый день! Чтобы начать работу, выберите одно из возможных действий',
                              reply_markup=markup)
    return callback

# обработка нажатия клавиш клавиатуры
def callback(update: Update, context: CallbackContext):
    query = update.callback_query
    variant = query.data
    if variant == 'buttonA':
        query.answer()
        query.edit_message_text(text='Хотите поздороваться? Введите /hello')

    if variant == 'buttonB':
        query.answer()
        query.edit_message_text(text='Хотите узнать, что я умею? Нажмите /help"')

    if variant == 'buttonC':
        query.answer()
        query.edit_message_text(text='Хотите узнать погоду в задданом городе. Введите /w <город>"')

    if variant == 'buttonD':
        query.answer()
        query.edit_message_tex