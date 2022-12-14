from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import datetime

def hi_command(update: Update, context: CallbackContext):
  log(update, context)
  update.message.reply_text(f'Hi {update.effective_user.first_name}!')
def help_command(update: Update, context: CallbackContext):
  log(update, context)
  update.message.reply_text(f'/hi\n/time\n/help')
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


updater = Updater('5825780566:AAHTJ3Y6L9TmdkJ8RQ9Lhjpq2eOCQXcrCwc')

updater.dispatcher.add_handler(CommandHandler('hi', hi_command))
updater.dispatcher.add_handler(CommandHandler('time', time_command))
updater.dispatcher.add_handler(CommandHandler('help', help_command))
updater.dispatcher.add_handler(CommandHandler('sum', sum_command))
print('server start')
updater.start_polling()
updater.idle()
  