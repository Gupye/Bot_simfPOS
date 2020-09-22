import configparser
import requests
from PIL import Image, ImageDraw, ImageFont


def send_new_alarm(message, send_filename, bot, lock):
    with lock:
        file = open(send_filename, 'r', encoding='UTF-8')
        mans = file.readlines()
        file.close()
    for man in mans:
        manw = str(man).strip()
        if check_connection():
            with lock:

                file = open('text.txt', 'w', encoding='UTF-8')
                file.write(message)
                file.close()
            image_send(bot, manw)
        else:
            with lock:
                file = open('temp_reports/buffer.txt', 'a', encoding='UTF-8')
                file.write(message + 'ienevade_point' + str(mans) + '\n')
                break


def check_connection():
    try:
        req = requests.get("http://www.google.com")
        return True
    except:
        return False


def image_send(bot, chat, filed='text.txt'):
    config = configparser.ConfigParser()  # создаём объекта парсера
    config.read("settings.ini")
    split_lines = int(config['image']['split_lines'])
    file = open(filed, 'r', encoding='UTF-8')
    message = file.readlines()
    file.seek(0)
    count = 0

    mes = str()
    if len(message) >= split_lines:
        message.append(' ')
        for i in range(0, len(message)):
            mes += message[i]
            count += 1
            if count >= split_lines:
                count = 0
                bot.send_message(chat, f'<pre>{mes}</pre>', parse_mode='HTML')
                mes = ''
        if mes != '':
            bot.send_message(chat, f'<pre>{mes}</pre>', parse_mode='HTML')
    else:

        message.append(' ')
        for i in range(0, len(message)):
            mes += message[i]
        bot.send_message(chat, f'<pre>{mes}</pre>', parse_mode='HTML')
    file.close()


def send_picture(bot, chat):
    file = open(f'{chat}.txt', 'r', encoding='UTF-8')
    stret = file.readlines()
    file.seek(0)
    tempo = str()
    count = len(stret) // 30
    rest = len(stret) % 30
    font = ImageFont.truetype("InputMono/InputMonoCompressed-Thin.ttf", 15, encoding='UTF-8')
    for i in range(0, count):
        for z in range(i * 30, (i + 1) * 30):
            tempo += stret[z]
        message_clast = file.read(len(tempo))
        sizes = (30 * 22) + 15
        img = Image.new('RGB', (350, sizes), (230, 230, 230))
        draw = ImageDraw.Draw(img)
        draw.text((10, 10), message_clast, fill='rgb(0, 0, 0)', font=font)
        img.save(f"{chat}.jpg")
        bot.send_photo(chat, open(f'{chat}.jpg', 'rb'))
        tempo = str()
    if count != 0:
        for z in range(1, rest):
            tempo += stret[-z]
        message_clast = file.read(len(tempo))
    else:
        message_clast = file.read()

    print(tempo, len(tempo))
    print(message_clast)
    sizes = (30 * 22) + 30
    img = Image.new('RGB', (350, sizes), (230, 230, 230))
    draw = ImageDraw.Draw(img)
    draw.text((10, 10), message_clast, fill='rgb(0, 0, 0)', font=font)
    img.save(f'{chat}.jpg')
    bot.send_photo(chat, open(f'{chat}.jpg', 'rb'))
    file.close()
