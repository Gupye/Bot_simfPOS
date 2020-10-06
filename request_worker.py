import requests
import report_works
import setings
from a.secureet import server_addoned


def chekc_lic():
    try:
        rest_code = report_works.check_rest_code()
        r = requests.get(f'{setings.serv_addr}/check_lic?rest_code={rest_code}')
        return r.json()
    except:
        r = server_addoned.check_lic(report_works.check_rest_code())
        return r



def check_lic_day():
    rest_code = report_works.check_rest_code()
    r = requests.get(f'{setings.serv_addr}/check_lic_day?rest_code={rest_code}')
    return r.json()


def check_in(nickname):
    rest_code = report_works.check_rest_code()
    r = requests.get(f'{setings.serv_addr}/check_in?rest_code={rest_code}&nickname={nickname}')
    return r.json()


def add_list(passw):
    rest_code = report_works.check_rest_code()
    r = requests.get(f'{setings.serv_addr}/add_list?rest_code={rest_code}&passw={passw}')
    return r.json()


def get_list():
    rest_code = report_works.check_rest_code()
    r = requests.get(f'{setings.serv_addr}/get_list?rest_code={rest_code}')
    return r.json()

def get_file():
    rest_code = report_works.check_rest_code()
    r = requests.get(f'{setings.serv_addr}/get_file?rest_code={rest_code}')
    return r.json()