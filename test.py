import configparser

import pyodbc

import sql_setings

def make_config():
    confige = configparser.ConfigParser()  # создаём объекта парсера
    confige.read("sql.ini")  # читаем конфиг
    return confige

def connecting_ds(confs, numser='1'):
    try:
        cn = pyodbc.connect(f"Driver={confs[numser]['Driver']};"
                        f"Server={confs[numser]['Server']};"
                        f"Database={confs[numser]['Database']};"
                        f"uid={sql_setings.uid};"
                        f"pwd={sql_setings.pwd}")
        print('удалось, слава те господи')
    except Exception as e:
        print('не удалось', e)


connecting_ds(make_config())