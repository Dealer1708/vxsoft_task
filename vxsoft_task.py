from random import randint
from time import sleep
import telebot
# import http.client, urllib

token = "5995365200:AAGEDoEkjXIpegtauZhiAQO4-P3vIIl-51M"

bot = telebot.TeleBot(token)
status = ["Healthy","Unhealthy"]

# app_token = "aihexhfjr25sjithtnnev7xxf85rn2"
# user_key = "u5zvpgp82yngqhbum53abd49byq1bh"
# conn = http.client.HTTPSConnection("api.pushover.net:443")
@bot.message_handler(commands=["start"])
def start(message):
    while True:
        bot.send_message(message.chat.id, status[randint(0,1)])
        sleep(randint(3,10))

bot.infinity_polling()
#
# for i in range(1,10):
#     conn.request("POST", "/1/messages.json",
#                  urllib.parse.urlencode({
#                      "token": app_token,
#                      "user": user_key,
#                      "message": "hello world",
#                  }), {"Content-type": "application/x-www-form-urlencoded"})
#     conn.getresponse()
#
#     sleep(10)
