from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, CallbackQueryHandler
import datetime
from fractions import Fraction
from math import *  
import telegram 

def hi_command(update: Update, context: CallbackContext):
  log(update, context)
  update.message.reply_text(f'Hi {update.effective_user.first_name}!')
def help_command(update: Update, context: CallbackContext):
  log(update, context)
  update.message.reply_text(f'/hi\n/time\n/help\n/calc\n')
def time_command(update: Update, context: CallbackContext):
  log(update, context)
  update.message.reply_text(f'{datetime.datetime.now().time()}')
def sum_command(update: Update, context: CallbackContext):
  log(update, context)
  msg = update.message.text
  print(msg)
  items = msg.split() # /sum 123 534543
  x = int(items[1])
  y = int(items[2])
  update.message.reply_text(f'{x} + {y} = {x+y}')

def log(update: Update, context: CallbackContext):
  file = open('db.csv', 'a')
  file.write(f'{update.effective_user.first_name},{update.effective_user.id}, {update.message.text}\n')
  file.close() 


def help_calc_value(update: Update, context: CallbackContext):
  log(update, context)
  update.message.reply_text(f'Хотите выполнить действие сложения введите команду в формате /sumv <первое число> <второе число> Пример:/sumv 10 2\n\
    \n Хотите выполнить действие вычитания введите команду в формате /minv <первое число> <второе число> Пример:/minv 10 2\n\
    \n Хотите выполнить действие умножения введите команду в формате /multv <первое число> <второе число> Пример:/multv 10 2\n\
    \n Хотите выполнить действие деления введите команду в формате /divv <первое число> <второе число> Пример:/divv 10 2\n')   

def help_calc_complex(update: Update, context: CallbackContext):
  log(update, context)
  update.message.reply_text(f'Хотите выполнить действие сложения введите команду в формате /sumc <вещественная часть первого числа> <мнимая часть первого числа> <вещественная часть второго числа> <мнимая часть второго числа> Пример:/sumc 2 5 6 8\n\
    \n Хотите выполнить действие вычитания введите команду в формате /minc <вещественная часть первого числа> <мнимая часть первого числa> <вещественная часть второго числа> <мнимая часть второго числa> Пример:/minc 2 5 6 8\n\
    \n Хотите выполнить действие умножения введите команду в формате /multc <вещественная часть первого числа> <мнимая часть первого числa> <вещественная часть второго числа> <мнимая часть второго числa> Пример:/multc 2 5 6 8\n\
    \n Хотите выполнить действие деления введите команду в формате /divc <вещественная часть первого числа> <мнимая часть первого числa> <вещественная часть второго числа> <мнимая часть второго числa> Пример:/divc 2 5 6 8\n')  

def help_calc_rational(update: Update, context: CallbackContext):
  log(update, context)
  update.message.reply_text(f'Хотите выполнить действие сложения введите команду в формате /sumr <первое число в формате дроби> <второе число в формате дроби> Пример:/sumr 10.5 4.2\n\
    \n Хотите выполнить действие вычитания введите команду в формате /minr <первое число в формате дроби> <второе число в формате дроби> Пример:/minr 10.5 4.2\n\
    \n Хотите выполнить действие умножения введите команду в формате /multr <первое число в формате дроби> <второе число в формате дроби> Пример:/multr 10.5 4.2\n\
    \n Хотите выполнить действие деления введите команду в формате /divr <первое число в формате дроби> <второе число в формате дроби> Пример:/divr 10.5 4.2\n')    

def min_command(update: Update, context: CallbackContext):
  log(update, context)
  msg = update.message.text
  print(msg)
  items = msg.split() 
  x = int(items[1])
  y = int(items[2])
  update.message.reply_text(f'{x} - {y} = {x-y}')    

def mult_command(update: Update, context: CallbackContext):
  log(update, context)
  msg = update.message.text
  print(msg)
  items = msg.split() 
  x = int(items[1])
  y = int(items[2])
  update.message.reply_text(f'{x} * {y} = {x*y}')   

def div_command(update: Update, context: CallbackContext):
  log(update, context)
  msg = update.message.text
  print(msg)
  items = msg.split() 
  x = int(items[1])
  y = int(items[2])
  update.message.reply_text(f'{x} / {y} = {x/y}')     

def help_value(update: Update, context: CallbackContext):
  log(update, context)
  update.message.reply_text(f'Хотите воспользоваться калькулятором простых чисел введите /val\n\
   \n Хотите воспользоваться калькулятором комплексных чисел введите /compl\n \
   \n Хотите воспользоваться калькулятором рациональных чисел введите /ration\n ') 

def sumc_command(update: Update, context: CallbackContext):
  log(update, context)
  msg = update.message.text
  print(msg)
  items = msg.split() 
  x = complex(int(items[1]), int(items[2]))
  y = complex(int(items[3]), int(items[4]))
  update.message.reply_text(f'{x} + {y} = {x+y}')   

def minc_command(update: Update, context: CallbackContext):
  log(update, context)
  msg = update.message.text
  print(msg)
  items = msg.split() 
  x = complex(int(items[1]), int(items[2]))
  y = complex(int(items[3]), int(items[4]))
  update.message.reply_text(f'{x} - {y} = {x-y}')    

def multc_command(update: Update, context: CallbackContext):
  log(update, context)
  msg = update.message.text
  print(msg)
  items = msg.split() 
  x = complex(int(items[1]), int(items[2]))
  y = complex(int(items[3]), int(items[4]))
  update.message.reply_text(f'{x} * {y} = {x*y}')   

def divc_command(update: Update, context: CallbackContext):
  log(update, context)
  msg = update.message.text
  print(msg)
  items = msg.split() 
  x = complex(int(items[1]), int(items[2]))
  y = complex(int(items[3]), int(items[4]))
  update.message.reply_text(f'{x} / {y} = {x/y}')   


def sumr_command(update: Update, context: CallbackContext):
  log(update, context)
  msg = update.message.text
  print(msg)
  items = msg.split() 
  x = Fraction(float(items[1]))
  y = Fraction(float(items[2]))
  update.message.reply_text(f'{x} + {y} = {x+y}')   

def minr_command(update: Update, context: CallbackContext):
  log(update, context)
  msg = update.message.text
  print(msg)
  items = msg.split() 
  x = Fraction(float(items[1]))
  y = Fraction(float(items[2]))
  update.message.reply_text(f'{x} - {y} = {x-y}')    

def multr_command(update: Update, context: CallbackContext):
  log(update, context)
  msg = update.message.text
  print(msg)
  items = msg.split() 
  x = Fraction(float(items[1]))
  y = Fraction(float(items[2]))
  update.message.reply_text(f'{x} * {y} = {x*y}')   

def divr_command(update: Update, context: CallbackContext):
  log(update, context)
  msg = update.message.text
  print(msg)
  items = msg.split() 
  x = Fraction(float(items[1]))
  y = Fraction(float(items[2]))
  update.message.reply_text(f'{x} / {y} = {x/y}')        



updater = Updater('5825780566:AAHTJ3Y6L9TmdkJ8RQ9Lhjpq2eOCQXcrCwc')

def startCommand(update: Update, context: CallbackContext):
    buttonA = telegram.InlineKeyboardButton('Поздороваться', callback_data='buttonA')
    buttonB = telegram.InlineKeyboardButton('Помощь', callback_data='buttonB')
    buttonC = telegram.InlineKeyboardButton('Время', callback_data='buttonC')
    buttonD = telegram.InlineKeyboardButton('Калькулятор', callback_data='buttonD')

    markup = telegram.InlineKeyboardMarkup(inline_keyboard=[[buttonA], [buttonB], [buttonC], [buttonD]])

    update.message.reply_text('Добрый день! Чтобы начать работу, выберите одно из возможных действий',
                              reply_markup=markup)
    return callback

def callback(update: Update, context: CallbackContext):
    query = update.callback_query
    variant = query.data
    if variant == 'buttonA':
        query.answer()
        query.edit_message_text(text='Хотите поздороваться? Введите /hi')

    if variant == 'buttonB':
        query.answer()
        query.edit_message_text(text='Хотите узнать, что я умею? Нажмите /help"')

    if variant == 'buttonC':
        query.answer()
        query.edit_message_text(text='Хотите узнать время. Введите /time"')

    if variant == 'buttonD':
        query.answer()
        query.edit_message_text(text='Хотите воспользоваться калькулятором. Введите /calc"')


updater.dispatcher.add_handler(CommandHandler('start', startCommand))
updater.dispatcher.add_handler(CallbackQueryHandler(callback=callback, pattern=None, run_async=False))
updater.dispatcher.add_handler(CommandHandler('hi', hi_command))
updater.dispatcher.add_handler(CommandHandler('time', time_command))
updater.dispatcher.add_handler(CommandHandler('help', help_command))
updater.dispatcher.add_handler(CommandHandler('calc', help_value))
updater.dispatcher.add_handler(CommandHandler('val', help_calc_value))
updater.dispatcher.add_handler(CommandHandler('sumv', sum_command))
updater.dispatcher.add_handler(CommandHandler('minv', min_command))
updater.dispatcher.add_handler(CommandHandler('multv', mult_command))
updater.dispatcher.add_handler(CommandHandler('divv', div_command))
updater.dispatcher.add_handler(CommandHandler('compl', help_calc_complex))
updater.dispatcher.add_handler(CommandHandler('sumc', sumc_command))
updater.dispatcher.add_handler(CommandHandler('minc', minc_command))
updater.dispatcher.add_handler(CommandHandler('multc', multc_command))
updater.dispatcher.add_handler(CommandHandler('divc', divc_command))
updater.dispatcher.add_handler(CommandHandler('ration', help_calc_rational))
updater.dispatcher.add_handler(CommandHandler('sumr', sumr_command))
updater.dispatcher.add_handler(CommandHandler('minr', minr_command))
updater.dispatcher.add_handler(CommandHandler('multr', multr_command))
updater.dispatcher.add_handler(CommandHandler('divr', divr_command))

print('server start')
updater.start_polling()
updater.idle()