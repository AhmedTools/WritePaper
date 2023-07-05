import os
try:
	import telebot
except:
	os.system('pip install telebot')
	import telebot
try:
	import requests
except:
	os.system('pip install requests')
	import requests
try:
	import time
except:
	os.system('pip install time')
	import time
try:
	import re
except:
	os.system('pip install re')
	import re
if os.name == 'nt':
    clear = 'cls'
    os.system(clear)
else:
    clear = 'clear'
    os.system(clear)
red = '\033[1;31m'
yellow = '\033[1;33m'
green = '\033[2;32m'
restart = '\x1b[0m'
copyright1 = (' '*13+f"{red}'{green}GitHub{red}'{yellow}:{red}'{green}AhmedTools{red}'{yellow},{red}'{green}TeleGram{red}'{yellow}:{red}'{green}U_L_W{red}'\n{restart}")
#codeind
print(copyright1)
bot = telebot.TeleBot((input("- Enter Token : ")))
os.system(clear)
print(copyright1)
last_message = ""
@bot.message_handler(func=lambda message: True)
def working(message):
    global last_message
    symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", "=", "{", "}", "[", "]", "|", "\\", ":", ";", "\"", "'", "<", ">", ",", ".", "?", "/", "~"]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    numbers_arabic = ["٠", "١", "٢", "٣", "٤", "٥", "٦", "٧", "٨", "٩"]
    text = message.text.strip()
    markup = telebot.types.InlineKeyboardMarkup()
    button = telebot.types.InlineKeyboardButton(text='- Dev', url='https://t.me/u_l_w')
    markup.add(button)
    if text == "/start":
        bot.send_message(message.chat.id, "- Send Text To Write In The Paper\n\n- ارسل رسالة لكي يتم كتابتها على الورقة",
                         reply_markup=markup)
    elif any('\u0621' <= c <= '\u064A' for c in text):
        bot.send_message(message.chat.id, "- Sorry This Bot Not Support Arabic Language\n\n- عذراّ هذا البوت لا يدعم اللغة العربية", reply_markup=markup)
    elif any(char in numbers_arabic for char in text):
    	bot.send_message(message.chat.id, "- Sorry This Bot Not Support Arabic Language\n\n- عذراّ هذا البوت لا يدعم اللغة العربية", reply_markup=markup)
    elif text == last_message:
        bot.send_message(message.chat.id, "- Please Send A Different Message To Avoid Duplicate Messages\n\n- يرجى إرسال رسالة مختلفة لتجنب تكرار الرسائل", reply_markup=markup)
    else:
        if any(c.isalnum() and not ('\u0621' <= c <= '\u064A') for c in text):
            bot.send_chat_action(message.chat.id, 'find_location')
            image = requests.get(f"http://apis.xditya.me/write", {'text': text}).content

            time.sleep(0.70)
            bot.send_chat_action(message.chat.id, 'upload_photo')
            markup_text = telebot.types.InlineKeyboardMarkup()
            button_markup = telebot.types.InlineKeyboardButton(text=f'- {text}', callback_data='text')
            markup_text.add(button_markup)
            bot.send_photo(message.chat.id, photo=image, reply_markup=markup_text)
            print(f"{message.chat.id} : {text}")
        elif any(char in symbols or char in numbers for char in text):
            bot.send_chat_action(message.chat.id, 'find_location')
            image = requests.get(f"http://apis.xditya.me/write", {'text': text}).content
            time.sleep(0.40)
            bot.send_chat_action(message.chat.id, 'upload_photo')
            markup_text = telebot.types.InlineKeyboardMarkup()
            button_markup = telebot.types.InlineKeyboardButton(text=f'- {text}', callback_data='text')
            markup_text.add(button_markup)
            bot.send_photo(message.chat.id, photo=image, reply_markup=markup_text)
            print(f"{message.chat.id} : {text}")
        else:
            bot.send_message(message.chat.id, "- Sorry The Bot Not Support This Language\n\n- عذراً هذا البوت لا يدعم هذه اللغة", reply_markup=markup)
    last_message = text

bot.polling()