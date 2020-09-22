import datetime
import configparser


def check_lic(rest_code):
    config = configparser.ConfigParser()  # создаём объекта парсера
    config.read('settings_ser.ini')
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
    config.read('settings_ser.ini')
    deta = config[rest_code]['date_exp_lic'].split('-')
    a = datetime.date.today()
    b = datetime.date(int(deta[0]), int(deta[1]), int(deta[2]))
    if (b - a).days == 5:
        return 'Лизцензия заканчивается через 5 дней'
    else:
        return (b - a).days


def check_in(rest_code, nickname):
    lines = open(f'{rest_code}.txt', 'r', encoding='UTF-8').readlines()
    for line in lines:
        if line == nickname:
            return '200'
        else:
            return 'Ivan Govnov'


def add_list(rest_code, passw):
    config = configparser.ConfigParser()  # создаём объекта парсера
    config.read('settings_ser.ini')
    if passw == config[rest_code]['pass_code']:
        return "200"
    else:
        return 'Пароль неверный'


def get_list(rest_code):
    return open(f'{rest_code}.txt', 'r', encoding='UTF-8').read()


def get_file(rest_code):
    config = configparser.ConfigParser()  # создаём объекта парсера
    config.read('settings_ser.ini')
    pass_code = config[rest_code]['pass_code']
    date_exp_lic = config[rest_code]['date_exp_lic']
    return f'[{rest_code}]\n' \
           f'rest_codee = {rest_code}\n' \
           f'pass_code = {pass_code}\n' \
           f'date_exp_lic = {date_exp_lic}'



