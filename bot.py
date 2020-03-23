import telebot
import config
import random
import re

TOKEN = '1117651347:AAEc5If0N-lTFU46mR038ZJnjWiwPIR_hSk'
bot = telebot.TeleBot(TOKEN)
token = 0


def analize_message(text):
    global token
    answer = ''
    find = re.search(r'^(привет|здравствуйте)', text)
    if find:
        answer = random.choice(
            ["Здравствуйте! Могу ли я чем-нибудь помочь?", 'Здравствуйте', 'Привет', 'Привет, как настроение?'])
    find = re.search(r'(да|давай|ок)', text)
    if find:
        answer = random.choice(["Как прошел ваш день?", "Как настроение?", "Где были?", "ЧТо нового?", "Что обсудим?"])
    find = re.search(r"(не\sхорошо|плохо|грустно|одиноко|депрессивно|паршиво)", text)
    if find:
        answer = random.choice(["А что так? Что случилось?", "Что стряслось?", "Давайте вы расскажите мне об этом.",
                                "Выкладывайте, что у вас там?"])
        token = 1
    if token == 1:
        answer = random.choice(['Главное-не унывать!', "Держитесь! Я в вас верю", "Вы все преодолеете!",
                                "В жизни нет ни черной, ни белой полосы, а есть только серая, поэтому не зацикливайтесь на проблемах. Все хорошее впереди!!!"])
        token = 2
    find = re.search(r'(хорошо|отлично|прекрасно|круто)', text)
    if find:
        answer = random.choice(['Так держать', 'Отлично'])
    if token == 2:
        token = 0
    return answer


@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id,
                     "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот. Готов выслушать ваши проблемы.".format(
                         message.from_user, bot.get_me()),
                     parse_mode='html')


@bot.message_handler(content_types=['text'])
def dialog(message):
    answer = analize_message(message.text.lower())
    bot.send_message(message.chat.id, answer)


bot.polling(none_stop=True)
