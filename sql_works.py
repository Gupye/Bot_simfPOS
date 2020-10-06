import threading

from sql_req import group_val, nacenck, dencheck, delcheck, cat_eat, cat_eatter, den_list, cards, cards_dis
import pyodbc
import pandas as pd
import configparser
from datetime import datetime, timedelta
import sql_setings

import setings

lock = threading.RLock()


def centr(text):
    fir = ((41 - len(text)) // 2) * " "
    sec = (41 - (len(fir) + len(text))) * " "
    a = fir + text + sec
    return a


def centr2(text):
    fir = ((48 - len(text)) // 2) * " "
    sec = (48 - (len(fir) + len(text))) * " "
    a = fir + text + sec
    return a


def centr3(text):
    fir = ((26 - len(text)) // 2) * " "
    sec = (26 - (len(fir) + len(text))) * " "
    a = fir + text + sec
    return a


def centr4(text):
    fir = ((48 - len(text)) // 2) * " "
    sec = (48 - (len(fir) + len(text))) * " "
    a = fir + text + sec
    return a


def get_dates():
    date_format = '%Y-%d-%m'
    today = datetime.now()
    yestarday = today - timedelta(days=1)

    return yestarday.strftime(date_format)

def get_dates2():
    date_format = '%Y-%m-%d'
    today = datetime.now()
    yestarday = today - timedelta(days=1)

    return yestarday.strftime(date_format)


def make_config():
    confige = configparser.ConfigParser()  # создаём объекта парсера
    confige.read("sql.ini")  # читаем конфиг
    return confige


def connecting_ds(confs, numser='1'):
    cn = pyodbc.connect(f"Driver={confs[numser]['Driver']};"
                        f"Server={confs[numser]['Server']};"
                        f"Database={confs[numser]['Database']};"
                        f"uid={sql_setings.uid};"
                        f"pwd={sql_setings.pwd}"
                        )
    return cn


def make_bal(ds, d1=get_dates(), d2=get_dates(),pdf=False):
    cnxn = connecting_ds(make_config())
    df = pd.read_sql_query(group_val(d1, d2), cnxn)
    df.rename(columns={'CURRENCYTYPE': 'Валюта'}, inplace=True)
    df3 = df[['Валюта', 'CHECKQNT', 'BASICSUM']].groupby('Валюта').sum()
    df3.rename(columns={'CHECKQNT': 'Чеков', 'BASICSUM': 'Сумма'}, inplace=True)
    df3.loc['Итого'] = df3.sum()
    pd.options.display.float_format = '{:,.1f}'.format

    df4 = df[['Валюта', 'CHECKQNT', 'BASICSUM', 'GUESTCNT']].groupby('Валюта').sum()
    df4['Сум/Чек'] = df4['BASICSUM'] / df4['CHECKQNT']
    df4['Сум/Гость'] = df4['BASICSUM'] / df4['GUESTCNT']
    df4.drop(['CHECKQNT', 'BASICSUM', 'GUESTCNT'], axis='columns', inplace=True)
    df4.loc['Итого'] = df4.sum()

    disf = pd.read_sql_query(nacenck(d1, d2), cnxn)
    disf.rename(columns={'NAME': 'Название', 'CHECKCNT': 'Чеков', 'B_SUM': 'Сумма'}, inplace=True)
    disf.drop(['NUM', 'SHIFTDATE'], axis='columns', inplace=True)
    disf2 = disf.groupby('Название').sum()

    dden = pd.read_sql_query(dencheck(d1, d2), cnxn)

    dden.loc['Отказы из чеков'] = dden.sum()
    adsd = dden.tail(1)

    adsd.rename(columns={'PRLISTSUM': 'Сумма', 'PAID': 'Чеков'}, inplace=True)

    delch = pd.read_sql_query(delcheck(d1, d2), cnxn)
    delch.loc['Удаления чеков'] = delch.sum()
    delch.rename(columns={'SUM': 'Сумма', 'CASHSHIFTPRINTED': 'Чеков'}, inplace=True)

    ads = delch.tail(1)
    dden2 = pd.concat([adsd, ads], ignore_index=False)

    catden = pd.read_sql_query(cat_eat(d1, d2), cnxn)
    catden.rename(columns={'PAYSUM': 'Сумма', 'CATEGORY': 'Категория'}, inplace=True)
    catden2 = catden[['Категория', 'Сумма']].groupby('Категория').sum()

    messsagek = f'{centr("Балансовый отчет")}\n' \
                f'{centr(f"Дата: {d1} - {d2}")}\n' \
                f'{centr(f"Ресторан:{setings.rest_name}")}\n\n' \
                f'{centr("ВЫРУЧКА")}\n' \
                f'{df3}\n\n' \
                f'{centr("СРЕДНИЙ ЧЕК")}\n' \
                f'{df4}\n\n' \
                f'{centr("Потраты бонусов и купонов")}\n' \
                f'{disf2}\n\n' \
                f'{centr("УДАЛЕНИЯ")}\n' \
                f'{dden2}\n\n' \
                f'{centr("Суммы по категориям")}\n' \
                f'{catden2}'
    with lock:
        open(f'{ds}.txt', 'w', encoding='UTF-8').write(messsagek)
    return messsagek


def eat_cat(ds, d1=get_dates(), d2=get_dates()):
    cnxn = connecting_ds(make_config())

    df = pd.read_sql_query(cat_eatter(d1, d2), cnxn)
    df.rename(columns={'DISH': 'Блюдо', 'CATEGORY': 'Категория', 'QUANTITY': 'Кол-во', 'PAYSUM': 'Сумма(по оплате)'},
              inplace=True)
    df2 = df[['Категория', 'Блюдо', 'Кол-во', 'Сумма(по оплате)']].groupby(['Категория', 'Блюдо']).sum()

    messsagek = f'{centr2("Расход блюд по категориям")}\n' \
                f'{centr2(f"Дата: {d1} - {d2}")}\n' \
                f'{centr2(f"Ресторан:{setings.rest_name}")}\n\n' \
                f'{df2}'
    with lock:
        open(f'{ds}.txt', 'w', encoding='UTF-8').write(messsagek)
    return messsagek


def list_den(ds, d1=get_dates(), d2=get_dates(),pdf=False):
    cnxn = connecting_ds(make_config())

    df = pd.read_sql_query(den_list(d1, d2), cnxn)

    messages = f'{centr2("Список отказов")}\n' \
               f'{centr2(f"Дата: {d1} - {d2}")}\n' \
               f'{centr2(f"Ресторан:{setings.rest_name}")}\n\n'
    first = True
    for i in range(0, len(df.index)):
        if first:
            first = False
        else:
            messages += '-------------------------------------------------\n'
        messages += f'Дата; время         Блюдо\n' \
                    f'{df.loc[i]["DATETIME___3"]} {df.loc[i]["DISH"]}\n' \
                    f'Кол-во	            Цена    Сумма\n' \
                    f'{df.loc[i]["QUANTITY"]}                 {df.loc[i]["PRLISTSUM"] / df.loc[i]["QUANTITY"]}  {df.loc[i]["PRLISTSUM"]}\n' \
                    f'{df.loc[i]["DELETEPERSON"]} {df.loc[i]["WAITER"]}\n'
    with lock:
        open(f'{ds}.txt', 'w', encoding='UTF-8').write(messages)
    return messages


def card_pay(ds, d1='0', d2='0',pdf=False):
    cnxn = connecting_ds(make_config())

    df = pd.read_sql_query(cards(d1, d2), cnxn)
    df.to_csv('test.csv')
    if d1 == '0':
        d1 = get_dates2()
        d2 = get_dates2()
    df2 = df[(df['SHIFTDATE'] >= d1) & (df['SHIFTDATE'] <= d2) & (df['CURRENCYFORMAT'] == 'Платежная карта')].groupby(['OWNER', 'CARDNUM'], as_index=False).sum()
    messages = f'{centr3("Карты оплаты")}\n' \
               f'{centr3(f"Ресторан:{setings.rest_name}")}\n\n'

    first = True
    for i in range(0, len(df2.index)):
        if first:
            first = False
        else:
            messages += '--------------------------\n'
        messages += f'Номер карты    Владелец\n' \
                    f'{df2.loc[i]["CARDNUM"]}          {df2.loc[i]["OWNER"]}\n' \
                    f'Чеков	       Сумма\n' \
                    f'{df2.loc[i]["CHECKCOUNT"]}              {df2.loc[i]["BINDEDSUM"]}\n'
    with lock:
        open(f'{ds}.txt', 'w', encoding='UTF-8').write(messages)
    return messages


def card_dis(ds, d1='0', d2='0'):
    cnxn = connecting_ds(make_config())
    pd.options.display.float_format = '{:,.2f}'.format
    df = pd.read_sql_query(cards_dis(), cnxn)

    if d1 == '0':
        d1 = get_dates2()
        d2 = get_dates2()


    df2 = df[(df['SHIFTDATE'] >= d1) & (df['SHIFTDATE'] <= d2)].groupby(['HOLDER', 'CARDCODE'], as_index=False).sum()

    messages = f'{centr4("Карты скидок")}\n' \
               f'{centr4(f"Дата: {d1} - {d2}")}\n' \
               f'{centr4(f"Ресторан:{setings.rest_name}")}\n\n'

    first = True
    for i in range(0, len(df2.index)):
        if first:
            first = False
        else:
            messages += '------------------------------------------------\n'
        messages += f'Номер карты         Владелец\n' \
                    f'{df2.loc[i]["CARDCODE"]}          {df2.loc[i]["HOLDER"]}\n' \
                    f'Скидка       Сумма     Чеков\n' \
                    f'{df2.loc[i]["DISCSUM"]}          {df2.loc[i]["BINDEDSUM"]}        {df2.loc[i]["CHECKCOUNT"]}\n'
    with lock:
        open(f'{ds}.txt', 'w', encoding='UTF-8').write(messages)

    return messages


