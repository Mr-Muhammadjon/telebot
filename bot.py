# import logging
# import wikipedia
# from aiogram import Bot, Dispatcher, executor, types

# API_TOKEN = '1749049979:AAFue89UuLDpbo3Pp8yeiB1wa8o61R41th4'
# wikipedia.set_lang('uz')

# # Configure logging
# logging.basicConfig(level=logging.INFO)

# # Initialize bot and dispatcher
# bot = Bot(token=API_TOKEN)
# dp = Dispatcher(bot)


# @dp.message_handler(commands=['start', 'help'])
# async def send_welcome(message: types.Message):
#     await message.reply("Assalomu alaykum wikipediya botga xush kelibsiz")



# @dp.message_handler()
# async def sendWiki(message: types.Message):
#     try:
#         respons = wikipedia.summary(message.text)
#         await message.answer(respons)
#     except:

#         await message.answer('bunday nomi topilmadi')

# if __name__ == '__main__':
#     executor.start_polling(dp, skip_updates=True)


import telebot
from telebot import types,util

bot = telebot.TeleBot("2004680877:AAGKKq-cNyUb8OWHBqjb8sp77TO1zWQpPfY")

#chat_member_handler. When status changes, telegram gives update. check status from old_chat_member and new_chat_member.
# @bot.chat_member_handler()
# def chat_m(message: types.ChatMemberUpdated):
#     old = message.old_chat_member
#     new = message.new_chat_member
#     if new.status == "member":
#         bot.send_message(message.chat.id,"Hello {name}!".format(name=new.user.first_name)) # Welcome message

#if bot is added to group, this handler will work
@bot.my_chat_member_handler()
def my_chat_m(message: types.ChatMemberUpdated):
    old = message.old_chat_member
    new = message.new_chat_member
    if new.status == "member":
        bot.send_message(message.chat.id,"Somebody added me to group") # Welcome message, if bot was added to group
        bot.leave_chat(message.chat.id)

#content_Type_service is:
#'new_chat_members', 'left_chat_member', 'new_chat_title', 'new_chat_photo', 'delete_chat_photo', 'group_chat_created',
#'supergroup_chat_created', 'channel_chat_created', 'migrate_to_chat_id', 'migrate_from_chat_id', 'pinned_message',
#'proximity_alert_triggered', 'voice_chat_scheduled', 'voice_chat_started', 'voice_chat_ended', 
#'voice_chat_participants_invited', 'message_auto_delete_timer_changed'
# this handler deletes service messages

@bot.message_handler(content_types=util.content_type_service)
def delall(message: types.Message):
    bot.delete_message(message.chat.id,message.message_id)
bot.polling(allowed_updates=util.update_types)



