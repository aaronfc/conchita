from twx.botapi import TelegramBot, ReplyKeyboardMarkup
from config import API_TOKEN

"""
Setup the bot
"""

bot = TelegramBot(API_TOKEN)
bot.update_bot_info().wait()
print(bot.username)


"""
Send a message to a user
"""
#user_id = int(<someuserid>)

#result = bot.send_message(user_id, 'test message body').wait()
#print(result)

"""
Get updates sent to the bot
"""
updates = bot.get_updates().wait()
for update in updates:
    print(update)

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