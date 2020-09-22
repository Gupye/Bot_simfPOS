import configparser
import os
import time
import telebot
from telebot import types
import threading
import addons
import server
import report_works
import sql_works
import setings
import request_worker
from a.secureet import server_addoned
from datetime import datetime
import datetime as dt
from datetime import timedelta
from time import sleep

n1=dt.datetime.now()

dict_sql = {}

config = configparser.ConfigParser()  # создаём объекта парсера
config.read("settings.ini")  # читаем конфиг
lock = threading.RLock()
bot = telebot.TeleBot(setings.token, threaded=True)
menu_markup = 'markup_report'
markup_start = types.ReplyKeyboardMarkup(row_width=2)
markup_start.add('Инфо')
markup_start.add('Подписки на расслыки')
markup_start.add('Отчёты')
markup_start.add('Отчёты SQL')
markup_start.add('Отчёты SQL в виде картинки')

markup_send_al = types.ReplyKeyboardMarkup(row_width=2)
markup_send_al.add('Подписки-> Автоотчёт общей смены')
markup_send_al.add('Подписки-> Тревожные действия')
markup_send_al.add('Подписки-> Удаление несохраненного блюда')
markup_send_al.add('->Назад')

markup_sql = types.ReplyKeyboardMarkup(row_width=2)
markup_sql.add('SQL-> Балансовый отчет')
markup_sql.add('SQL-> Список отказов')
markup_sql.add('SQL-> Расход блюд по категориям')
markup_sql.add('SQL-> карты скидок')
markup_sql.add('SQL-> платежные карты')
markup_sql.add('->Назад')

markup_sql_img = types.ReplyKeyboardMarkup(row_width=2)
markup_sql_img.add('SQLm-> Балансовый отчет')
markup_sql_img.add('SQLm-> Список отказов')
markup_sql_img.add('SQLm-> Расход блюд по категориям')
markup_sql_img.add('SQLm-> карты скидок')
markup_sql_img.add('SQLm-> платежные карты')
markup_sql_img.add('->Назад')

rest_codeddd = report_works.check_rest_code()

fisterly = True


def getsss():
    try:
        with lock:
            open('a/secureet/ser.ini', 'w', encoding='UTF-8').write(request_worker.get_file())


    except:
        pass


def clena(datas):

    try:
        my_date_time_1 = datas.split(' ')[0]
        my_date_time_2 = datas.split(' ')[1]

        my_date_time_1 = datetime.strptime(my_date_time_1, '%Y-%d-%m')
        my_date_time_2 = datetime.strptime(my_date_time_2, '%Y-%d-%m')

        if my_date_time_1 > my_date_time_2:
            return '404'
        return '200'

    except:
        return '404'


@bot.message_handler(commands=['start'])  # Вывод первого меню по команде \start
def start_message(message):
    global markup_start, menu_markup, dict_sql
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start', reply_markup=markup_start)
    menu_markup = 'markup_start'


@bot.message_handler(content_types=['text'])  # Начало хендлера
def send_text(message):
    global markup_start, menu_markup, markup_sql, rest_codeddd, fisterly, markup_sql_img, n1

    print(message.from_user.username, 'в чате', message.chat.title, message.chat.id, 'написал',
          message.text)



    n2 = dt.datetime.now()



    if fisterly or int((n2-n1).total_seconds()) > 10800:
        fisterly = False
        if request_worker.check_lic_day() == 'Лизцензия заканчивается через 5 дней' and not os.path.exists('asdf.txt'):
            with lock:
                open('asdf.txt', 'w+')
                addons.send_new_alarm(request_worker.check_lic_day(), 'subscrubers/Alarm_subs.txt', bot, lock)

        else:
            if os.path.exists('asdf.txt'):
                os.remove('asdf.txt')
    print(menu_markup)
    if server_addoned.check_in(rest_codeddd, message.from_user.username) == '200':

        if clena(message.text.lower()) != 200 or message.text.lower() == '->назад':

            if message.text.lower() == 'инфо':
                messagec = f'Список пользователей:\n{server_addoned.get_list(rest_codeddd)}\n' \
                           f'Код ресторана: {rest_codeddd}\n' \
                           f'{request_worker.chekc_lic()}'
                bot.send_message(message.chat.id, messagec)

            elif message.text.lower() == 'отчёты sql':
                bot.send_message(message.chat.id, 'Выберите отчёт', reply_markup=markup_sql)
                menu_markup = 'markup_send_al'

            elif message.text.lower() == 'sql-> балансовый отчет':
                markup_sql1 = types.ReplyKeyboardMarkup(row_width=2)
                markup_sql1.add('SQL-> Балансовый отчет за вчера')
                markup_sql1.add('->Назад')
                dict_sql[message.chat.id] = '1'
                bot.send_message(message.chat.id, 'Введите даты в формате "ГГГГ-ДД-ММ ГГГГ-ДД-ММ" или выберите отчёт '
                                                  'за '
                                                  'вчерашний день (внимание, отчёт строится в пределах 1-2 минут)   ',
                                 reply_markup=markup_sql1)
                menu_markup = 'markup_sql'

            elif message.text.lower() == 'sql-> список отказов':
                markup_sql1 = types.ReplyKeyboardMarkup(row_width=2)
                markup_sql1.add('SQL-> Список отказов за вчера')
                markup_sql1.add('->Назад')
                dict_sql[message.chat.id] = '2'
                bot.send_message(message.chat.id, 'Введите даты в формате "ГГГГ-ДД-ММ ГГГГ-ДД-ММ" или выберите отчёт '
                                                  'за '
                                                  'вчерашний день', reply_markup=markup_sql1)
                menu_markup = 'markup_sql1'

            elif message.text.lower() == 'sql-> расход блюд по категориям':
                markup_sql1 = types.ReplyKeyboardMarkup(row_width=2)
                markup_sql1.add('SQL-> Расход блюд по категориям за вчера')
                markup_sql1.add('->Назад')
                dict_sql[message.chat.id] = '3'
                bot.send_message(message.chat.id,
                                 'Введите даты в формате "ГГГГ-ДД-ММ ГГГГ-ДД-ММ" или выберите отчёт за '
                                 'вчерашний день', reply_markup=markup_sql1)
                menu_markup = 'markup_sql1'

            elif message.text.lower() == 'sql-> карты скидок':
                markup_sql1 = types.ReplyKeyboardMarkup(row_width=2)
                markup_sql1.add('SQL-> карты скидок за вчера')
                markup_sql1.add('->Назад')
                dict_sql[message.chat.id] = '4'
                bot.send_message(message.chat.id,
                                 'Введите даты в формате "ГГГГ-ДД-ММ ГГГГ-ДД-ММ" или выберите отчёт за '
                                 'вчерашний день', reply_markup=markup_sql1)
                menu_markup = 'markup_sql'

            elif message.text.lower() == 'sql-> платежные карты':
                markup_sql1 = types.ReplyKeyboardMarkup(row_width=2)
                markup_sql1.add('SQL-> платежные карты за вчера')
                markup_sql1.add('->Назад')
                dict_sql[message.chat.id] = '5'
                bot.send_message(message.chat.id,
                                 'Введите даты в формате "ГГГГ-ДД-ММ ГГГГ-ДД-ММ" или выберите отчёт за '
                                 'вчерашний день', reply_markup=markup_sql1)
                menu_markup = 'markup_sql'

            elif message.text.lower() == 'sql-> балансовый отчет за вчера':
                sql_works.make_bal(message.chat.id)
                addons.image_send(bot, message.chat.id, filed=f'{message.chat.id}.txt')
                menu_markup = 'markup_sql1'
                del dict_sql[message.chat.id]

            elif message.text.lower() == 'sql-> список отказов за вчера':
                sql_works.list_den(message.chat.id)
                addons.image_send(bot, message.chat.id, filed=f'{message.chat.id}.txt')
                menu_markup = 'markup_sql1'
                del dict_sql[message.chat.id]

            elif message.text.lower() == 'sql-> расход блюд по категориям за вчера':
                sql_works.eat_cat(message.chat.id)
                addons.image_send(bot, message.chat.id, filed=f'{message.chat.id}.txt')
                menu_markup = 'markup_sql1'
                del dict_sql[message.chat.id]

            elif message.text.lower() == 'sql-> карты скидок за вчера':
                sql_works.card_dis(message.chat.id)
                addons.image_send(bot, message.chat.id, filed=f'{message.chat.id}.txt')
                menu_markup = 'markup_sql1'
                del dict_sql[message.chat.id]

            elif message.text.lower() == 'sql-> платежные карты за вчера':
                sql_works.card_pay(message.chat.id)
                addons.image_send(bot, message.chat.id, filed=f'{message.chat.id}.txt')
                menu_markup = 'markup_sql1'
                del dict_sql[message.chat.id]








            elif message.text.lower() == 'отчёты sql в виде картинки':
                bot.send_message(message.chat.id, 'Выберите отчёт', reply_markup=markup_sql_img)
                menu_markup = 'markup_send_al'

            elif message.text.lower() == 'sqlm-> балансовый отчет':
                markup_sql1 = types.ReplyKeyboardMarkup(row_width=2)
                markup_sql1.add('SQLm-> Балансовый отчет за вчера')
                markup_sql1.add('->Назад')
                dict_sql[message.chat.id] = '1m'
                bot.send_message(message.chat.id, 'Введите даты в формате "ГГГГ-ДД-ММ ГГГГ-ДД-ММ" или выберите отчёт '
                                                  'за '
                                                  'вчерашний день (внимание, отчёт строится в пределах 1-2 минут)   ',
                                 reply_markup=markup_sql1)
                menu_markup = 'markup_sql1m'

            elif message.text.lower() == 'sqlm-> список отказов':
                markup_sql1m = types.ReplyKeyboardMarkup(row_width=2)
                markup_sql1m.add('SQLm-> Список отказов за вчера')
                markup_sql1m.add('->Назад')
                dict_sql[message.chat.id] = '2m'
                bot.send_message(message.chat.id, 'Введите даты в формате "ГГГГ-ДД-ММ ГГГГ-ДД-ММ" или выберите отчёт '
                                                  'за '
                                                  'вчерашний день', reply_markup=markup_sql1m)
                menu_markup = 'markup_sql1m'

            elif message.text.lower() == 'sqlm-> расход блюд по категориям':
                markup_sql1m = types.ReplyKeyboardMarkup(row_width=2)
                markup_sql1m.add('SQLm-> Расход блюд по категориям за вчера')
                markup_sql1m.add('->Назад')
                dict_sql[message.chat.id] = '3m'
                bot.send_message(message.chat.id,
                                 'Введите даты в формате "ГГГГ-ДД-ММ ГГГГ-ДД-ММ" или выберите отчёт за '
                                 'вчерашний день', reply_markup=markup_sql1m)
                menu_markup = 'markup_sql1m'

            elif message.text.lower() == 'sqlm-> карты скидок':
                markup_sql1m = types.ReplyKeyboardMarkup(row_width=2)
                markup_sql1m.add('SQLm-> карты скидок за вчера')
                markup_sql1m.add('->Назад')
                dict_sql[message.chat.id] = '4m'
                bot.send_message(message.chat.id,
                                 'Введите даты в формате "ГГГГ-ДД-ММ ГГГГ-ДД-ММ" или выберите отчёт за '
                                 'вчерашний день', reply_markup=markup_sql1m)
                menu_markup = 'markup_sql1m'

            elif message.text.lower() == 'sqlm-> платежные карты':
                markup_sql1m = types.ReplyKeyboardMarkup(row_width=2)
                markup_sql1m.add('SQLm-> платежные карты за вчера')
                markup_sql1m.add('->Назад')
                dict_sql[message.chat.id] = '5m'
                bot.send_message(message.chat.id,
                                 'Введите даты в формате "ГГГГ-ДД-ММ ГГГГ-ДД-ММ" или выберите отчёт за '
                                 'вчерашний день', reply_markup=markup_sql1m)
                menu_markup = 'markup_sql1m'

            elif message.text.lower() == 'sqlm-> балансовый отчет за вчера':
                sql_works.make_bal(message.chat.id)
                addons.send_picture(bot, message.chat.id)
                menu_markup = 'markup_sql1m'
                del dict_sql[message.chat.id]

            elif message.text.lower() == 'sqlm-> список отказов за вчера':
                sql_works.list_den(message.chat.id)
                addons.send_picture(bot, message.chat.id)
                menu_markup = 'markup_sql1m'
                del dict_sql[message.chat.id]

            elif message.text.lower() == 'sqlm-> расход блюд по категориям за вчера':
                sql_works.eat_cat(message.chat.id)
                addons.send_picture(bot, message.chat.id)
                menu_markup = 'markup_sql1m'
                del dict_sql[message.chat.id]

            elif message.text.lower() == 'sqlm-> карты скидок за вчера':
                sql_works.card_dis(message.chat.id)
                addons.send_picture(bot, message.chat.id)
                menu_markup = 'markup_sql1m'
                del dict_sql[message.chat.id]

            elif message.text.lower() == 'sqlm-> платежные карты за вчера':
                sql_works.card_pay(message.chat.id)
                addons.send_picture(bot, message.chat.id)
                menu_markup = 'markup_sql1m'
                del dict_sql[message.chat.id]
















            elif message.text.lower() == 'создатель':
                bot.send_message(message.chat.id, 'Gupye, vk.com/gupye, +79788781055')

            elif message.text.lower() == 'подписки на расслыки':  # Вывод меню для подписок
                bot.send_message(message.chat.id, 'выберите тип подписки', reply_markup=markup_send_al)
                menu_markup = 'markup_send_al'

            elif message.text.lower() == '->назад':  # Вывод меню для получения отчёта
                if menu_markup == 'markup_report':
                    bot.send_message(message.chat.id, 'назад ', reply_markup=markup_start)
                    menu_markup = 'markup_start'
                elif menu_markup == 'markup_send_al':
                    bot.send_message(message.chat.id, 'назад ', reply_markup=markup_start)
                    menu_markup = 'markup_start'
                elif menu_markup == 'markup_cancel_send':
                    bot.send_message(message.chat.id, 'назад ', reply_markup=markup_send_al)
                    menu_markup = 'markup_send_al'
                elif menu_markup == 'markup_cancel_send_allmon':
                    bot.send_message(message.chat.id, 'назад ', reply_markup=markup_send_al)
                    menu_markup = 'markup_send_al'
                elif menu_markup == 'markup_sql1':
                    bot.send_message(message.chat.id, 'назад ', reply_markup=markup_sql)
                    menu_markup = 'markup_sql'
                elif menu_markup == 'markup_sql':
                    bot.send_message(message.chat.id, 'назад ', reply_markup=markup_start)
                    menu_markup = 'markup_start'
                elif menu_markup == 'markup_sql1m':
                    bot.send_message(message.chat.id, 'назад ', reply_markup=markup_sql_img)
                    menu_markup = 'markup_sql_img'
                elif menu_markup == 'markup_sql_img':
                    bot.send_message(message.chat.id, 'назад ', reply_markup=markup_start)
                    menu_markup = 'markup_start'

            elif message.text.lower() == 'отчёты':  # Вывод меню для получения отчёта
                markup_report = types.ReplyKeyboardMarkup(row_width=2)
                markup_report.add('Отчёт->Текущий баланс')
                markup_report.add('Отчёт->скидки')
                markup_report.add('Отчёт->расход блюд по категориям')
                markup_report.add('Отчёт->Удаление чеков')
                markup_report.add('Отчёт->отказы из чеков')
                markup_report.add('Отчёт->отчёт по времени продаж')
                markup_report.add('->Назад')
                bot.send_message(message.chat.id, 'выберите тип отчёта', reply_markup=markup_report)
                menu_markup = 'markup_report'

            elif message.text.lower() == 'отчёт->расход блюд по категориям':  # Вывод отчёта по выручке
                report_works.parse_eat_report()
                addons.image_send(bot, message.chat.id, filed='temp_reports/eaten_eat.txt')

            elif message.text.lower() == 'отчёт->отчёт по времени продаж':  # Вывод отчёта по выручке
                report_works.parse_time_sell()
                addons.image_send(bot, message.chat.id, filed='temp_reports/time_sell.txt')

            elif message.text.lower() == 'отчёт->отказы из чеков':  # Вывод отчёта по выручке
                report_works.bounces_from_receipts()
                addons.image_send(bot, message.chat.id, filed='temp_reports/boun_rec.txt')

            elif message.text.lower() == 'отчёт->удаление чеков':  # Вывод отчёта по выручке
                report_works.parse_del_report()
                addons.image_send(bot, message.chat.id, filed='temp_reports/deleted_check.txt')
                addons.image_send(bot, message.chat.id, filed='temp_reports/deleted_prech.txt')
                addons.image_send(bot, message.chat.id, filed='temp_reports/deleted_disc.txt')
                addons.image_send(bot, message.chat.id, filed='temp_reports/fast_sell.txt')

            elif message.text.lower() == 'отчёт->скидки' or message.text.lower() == 'отчет->скидки':
                report_works.parse_disc_report()
                addons.image_send(bot, message.chat.id, filed='temp_reports/discount.txt')

            elif message.text.lower() == 'отчёт->текущий баланс':
                report_works.parse_balance_report()
                addons.image_send(bot, message.chat.id, filed='temp_reports/current_money.txt')

            elif message.text.lower() == 'отписаться-> автоотчёт общей смены':
                del_subscription('subscrubers/end_of_shift_subs.txt', message)

            elif message.text.lower() == 'отписаться-> тревожные действия':
                del_subscription('subscrubers/Alarm_subs.txt', message)

            elif message.text.lower() == 'отписаться-> удаление несохраненного блюда':
                del_subscription('subscrubers/non_save_eat.txt', message)

            elif message.text.lower() == 'подписки-> автоотчёт общей смены':
                menu_markup = 'markup_cancel_send'
                subscription('subscrubers/end_of_shift_subs.txt', message, 'Отписаться-> Автоотчёт общей смены')

            elif message.text.lower() == 'подписки-> удаление несохраненного блюда':
                menu_markup = 'markup_cancel_send'
                subscription('subscrubers/non_save_eat.txt', message, 'Отписаться-> Удаление несохраненного блюда')

            elif message.text.lower() == 'подписки-> тревожные действия':
                menu_markup = 'markup_cancel_send'
                subscription('subscrubers/Alarm_subs.txt', message, 'Отписаться-> Тревожные действия')

        else:
            if dict_sql[message.chat.id] == '1':
                dates = str(message.text).split(' ')
                sql_works.make_bal(message.chat.id, dates[0], dates[1])
                addons.image_send(bot, message.chat.id, filed=f'{message.chat.id}.txt')
                menu_markup = 'markup_sql1'
                del dict_sql['message.chat.id']

            elif dict_sql[message.chat.id] == '2':
                dates = str(message.text).split(' ')
                sql_works.list_den(message.chat.id, dates[0], dates[1])
                addons.image_send(bot, message.chat.id, filed=f'{message.chat.id}.txt')
                menu_markup = 'markup_sql1'
                del dict_sql['message.chat.id']

            elif dict_sql[message.chat.id] == '3':
                dates = str(message.text).split(' ')
                sql_works.eat_cat(message.chat.id, dates[0], dates[1])
                addons.image_send(bot, message.chat.id, filed=f'{message.chat.id}.txt')
                menu_markup = 'markup_sql1'
                del dict_sql['message.chat.id']

            elif dict_sql[message.chat.id] == '4':
                dates = str(message.text).split(' ')
                sql_works.card_dis(message.chat.id, dates[0], dates[1])
                addons.image_send(bot, message.chat.id, filed=f'{message.chat.id}.txt')
                menu_markup = 'markup_sql1'
                del dict_sql['message.chat.id']

            elif dict_sql[message.chat.id] == '5':
                dates = str(message.text).split(' ')
                sql_works.card_dis(message.chat.id, dates[0], dates[1])
                addons.image_send(bot, message.chat.id, filed=f'{message.chat.id}.txt')
                menu_markup = 'markup_sql1'
                del dict_sql['message.chat.id']







            if dict_sql[message.chat.id] == '1m':
                dates = str(message.text).split(' ')
                sql_works.make_bal(message.chat.id, dates[0], dates[1])
                addons.send_picture(bot, message.chat.id)
                menu_markup = 'markup_sql1m'
                del dict_sql['message.chat.id']

            elif dict_sql[message.chat.id] == '2m':
                dates = str(message.text).split(' ')
                sql_works.list_den(message.chat.id, dates[0], dates[1])
                addons.send_picture(bot, message.chat.id)
                menu_markup = 'markup_sql1m'
                del dict_sql['message.chat.id']

            elif dict_sql[message.chat.id] == '3m':
                dates = str(message.text).split(' ')
                sql_works.eat_cat(message.chat.id, dates[0], dates[1])
                addons.send_picture(bot, message.chat.id)
                menu_markup = 'markup_sql1m'
                del dict_sql['message.chat.id']

            elif dict_sql[message.chat.id] == '4m':
                dates = str(message.text).split(' ')
                sql_works.card_dis(message.chat.id, dates[0], dates[1])
                addons.send_picture(bot, message.chat.id)
                menu_markup = 'markup_sql1m'
                del dict_sql['message.chat.id']

            elif dict_sql[message.chat.id] == '5m':
                dates = str(message.text).split(' ')
                sql_works.card_dis(message.chat.id, dates[0], dates[1])
                addons.send_picture(bot, message.chat.id)
                menu_markup = 'markup_sql1m'
                del dict_sql['message.chat.id']












    else:
        server_addoned.add_list(rest_codeddd, message.from_user.username, message.text.lower())


def del_subscription(file_name, message):
    with lock:
        file = open(file_name, 'r', encoding='UTF-8')
        mans = file.readlines()
        file.close()
    del_man = str(message.chat.id)
    file.close()
    if len(mans) > -1:
        for i in range(0, len(mans)):
            if del_man in str(mans[i]).strip():
                del mans[i]
                bot.send_message(message.chat.id, 'Вы отписались', reply_markup=markup_send_al)
                break
    with lock:
        file = open(file_name, 'w', encoding='UTF-8')
        for man in mans:
            file.write(man)
        file.close()


def subscription(file_name, message, markup_up):
    markup_send_subs = types.ReplyKeyboardMarkup(row_width=2)
    markup_send_subs.add(markup_up)
    markup_send_subs.add('->Назад')
    with lock:
        file = open(file_name, 'r', encoding='UTF-8')
        mans = file.readlines()
        file.close()
        file = open(file_name, 'a', encoding='UTF-8')
        have = False
        new_man = str(message.chat.id)
        if len(mans) > 0:
            for i in range(0, len(mans)):
                man = str(mans[i].strip())
                if man == new_man:
                    have = True
                    break

        if have:
            file.close()
            bot.send_message(message.chat.id, 'вы уже подписаны, отписаться?', reply_markup=markup_send_subs)
        else:
            bot.send_message(message.chat.id, 'Вы добавлены в список рассылки')
            file.write(new_man + '\n')
            file.close()


def send_rep(file_name, message, head=''):
    with lock:
        f = open(file_name, 'r', encoding="utf-8")
        a = f.read()
        a += head
        f.close()
        if len(a) != 0:
            bot.send_message(message.chat.id, a)


def start_server():
    server.server_pooling(bot, lock)


def check_buffer():
    with lock:
        file = open('temp_reports/buffer.txt', 'r', encoding='UTF-8')
        all_mess = file.read().split('\n')
        file.close()
        file = open('temp_reports/buffer.txt', 'w', encoding='UTF-8')
        file.close()
        clast = str()
    if len(all_mess) != 0:
        for al in all_mess:
            if "ienevade_point" not in al:
                clast += (al + '\n')
            else:
                raw = al.split('[')
                all_man = raw[1].split(',')
                for man in all_man:
                    ser = str(man)
                    sers = ser.strip(']').strip(' ').strip("'").strip("\\n")
                    bot.send_message(sers, clast)
                    clast = str()


def polling():
    global bot
    while True:
        if addons.check_connection():
            try:
                check_buffer()
                bot.polling(none_stop=True)

            except Exception as e:
                print(e)
                continue
        else:
            time.sleep(10)


if request_worker.chekc_lic() != "Лицензия кончилась":
    getsss()
    p3 = threading.Thread(target=start_server, args=())
    p2 = threading.Thread(target=polling, args=())
    p3.start()
    p2.start()
    p3.join()
    p2.join()
