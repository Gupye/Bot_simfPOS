import datetime
import configparser
import os

import request_worker


def check_lic(rest_code):
    config = configparser.ConfigParser()  # создаём объекта парсера
    config.read('a/secureet/ser.ini')
    deta = config[rest_code]['date_exp_lic'].split('-')
    a = datetime.date.today()
    b = datetime.date(int(deta[0]), int(deta[1]), int(deta[2]))
    if a > b:
        mess = "Лицензия кончилась"
    elif a == b:
        mess = 'Лицензия кончается сегодня'
    else:
        mess = f'Лицензия действительна, истекает {b}'
    return mess


def check_lic_day(rest_code):
    config = configparser.ConfigParser()  # создаём объекта парсера
    config.read('a/secureet/ser.ini')
    deta = config[rest_code]['date_exp_lic'].split('-')
    a = datetime.date.today()
    b = datetime.date(int(deta[0]), int(deta[1]), int(deta[2]))
    if (b - a).days == 5:
        return 'Лизцензия заканчивается через 5 дней'
    else:
        return '200'


def check_in(rest_code, nickname):
    if not os.path.exists(f'a/secureet/{rest_code}.txt'):
        open(f'a/secureet/{rest_code}.txt', 'w', encoding='UTF-8')

    lines = open(f'a/secureet/{rest_code}.txt', 'r', encoding='UTF-8').readlines()

    for line in lines:
        if nickname == str(line).strip('\n'):
            print(nickname, '==', str(line).strip('\n'))
            return '200'

    return 'Ivan Govnov'


def add_list(rest_code, nickname, passw):
    config = configparser.ConfigParser()  # создаём объекта парсера
    config.read('a/secureet/ser.ini')
    try:
        if request_worker.add_list() == '200':
            open(f'a/secureet/{rest_code}.txt', 'a', encoding='UTF-8').write(nickname + '\n')
            return "200"
        else:
            return 'sdfsdfsdf'
    except:
        if passw == config[rest_code]['pass_code']:
            open(f'a/secureet/{rest_code}.txt', 'a', encoding='UTF-8').write(nickname + '\n')
            return "200"
        else:
            return 'sdfsdfsdf'


def get_list(rest_code):
    return open(f'a/secureet/{rest_code}.txt', 'r', encoding='UTF-8').read()
