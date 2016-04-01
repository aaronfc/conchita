from twx.botapi import TelegramBot, ReplyKeyboardMarkup
from config import API_TOKEN
from tinydb import TinyDB, Query
from time import time, sleep

updates_db = TinyDB('json/updates_log.json')
users_db = TinyDB('json/users.json')

"""
Setup the bot
"""

bot = TelegramBot(API_TOKEN)
bot.update_bot_info().wait()
print "Bot {} loaded.".format(bot.username)


"""
Send a message to a user
"""
#user_id = int(<someuserid>)

#result = bot.send_message(user_id, 'test message body').wait()
#print(result)


def process(update):
    update_id = update.update_id
    Update = Query()
    result = updates_db.search(Update.id == update_id)
    text = update.message.text
    sender = update.message.sender
    if len(result) == 0:
        print "Processing update with ID {}".format(update_id)
        updates_db.insert({'id': update_id, 'user_id': sender.id, 'text': text})
        if text == "/start":
            User = Query()
            result = users_db.search(User.id == sender.id)
            if len(result) == 0:
                users_db.insert({'id': sender.id, 'name': sender.first_name, 'username': sender.username, 'creation_time': int(time())})
                bot.send_message(sender.id, "You are now my sir.").wait()
            else:
                user_info = result[0]
                bot.send_message(sender.id, "You are already my sir since {} seconds ago.".format(int(time()-user_info['creation_time'])))
    else:
        print "Ignored update with ID {}".format(update_id)


"""
Get updates sent to the bot
"""
while True:
    updates = bot.get_updates().wait()
    for update in updates:
        process(update)
    sleep(5)

"""
Use a custom keyboard
"""
#keyboard = [
#    ['7', '8', '9'],
#    ['4', '5', '6'],
#    ['1', '2', '3'],
#         ['0']
#]
#reply_markup = ReplyKeyboardMarkup.create(keyboard)

#bot.send_message(user_id, 'please enter a number', reply_markup=reply_markup).wait()