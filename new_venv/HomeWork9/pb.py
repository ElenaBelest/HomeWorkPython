from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import datetime
import requests
from pprint import pprint

def hi_command(update: Update, context: CallbackContext):
  log(update, context)
  update.message.reply_text(f'Hi {update.effective_user.first_name}!')

def help_command(update: Update, context: CallbackContext):
  log(update, context)
  update.message.reply_text(f'/hi\n/time\n/help\n/exch')

def time_command(update: Update, context: CallbackContext):
  log(update, context)
  update.message.reply_text(f'{datetime.datetime.now().time()}')

def exchange_command(update: Update, context: CallbackContext):
  log(update, context)
  msg = update.message.text
  print(msg)
  data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
  pprint(data)
  items = msg.split()
  print(items)
  cur = items[1]
  print(data['Valute'][cur]['Name'], data['Valute'][cur]['Value'], data['Date'])
  cur1 = data['Valute'][cur]['Name']
  cur2 = data['Valute'][cur]['Value']
  dt = data['Date']
  update.message.reply_text(f'{cur1} \n {cur2} \n {dt} ')

def log(update: Update, context: CallbackContext):
  file = open('db.csv', 'a')
  file.write(f'{update.effective_user.first_name},{update.effective_user.id}, {update.message.text}\n')
  file.close() 


updater = Updater('5825780566:AAHTJ3Y6L9TmdkJ8RQ9Lhjpq2eOCQXcrCwc')

updater.dispatcher.add_handler(CommandHandler('hi', hi_command))
updater.dispatcher.add_handler(CommandHandler('time', time_command))
updater.dispatcher.add_handler(CommandHandler('help', help_command))
updater.dispatcher.add_handler(CommandHandler('exch', exchange_command))
print('server start')
updater.start_polling()
updater.idle()