import socket
import threading
import addons
import configparser
from XMLpars import detect_situation


def server_pooling(bot, lock):
    config = configparser.ConfigParser()  # создаём объекта парсера
    config.read("settings.ini")  # читаем конфиг
    addr = config['settings']['ip_addres']
    port = config['settings']['port']
    HOST = str(addr).strip("'")
    PORT = int(port)
    srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    srv.bind((HOST, PORT))
    byted = False
    ifwanted = False
    print(f'Server started {addr}:{port}')
    while 1:
        srv.listen(1)
        sock, addr = srv.accept()
        while 1:
            pal = sock.recv(524288)
            if not pal:
                break
            try:
                print("UTF - 8 Получено от %s:%s:" % addr)
                textes = pal.decode(encoding="UTF-8")
                print(textes)
                se = len(textes) - 20
                sre = len(textes)
                partec = textes[0:20]
                if '<DeletePrecheck' in partec \
                        or '<ScreenCheck' in partec or \
                        '<DeleteCheck' in partec or \
                        '<StoreCheck' in partec or \
                        '<QuitOrder' in partec or \
                        '<OpenOrder' in partec or \
                        '<CloseCheck' in partec:

                    ifwanted = True
                    print('То, что нужно')

                if '</DeletePrecheck>' in textes[se:sre]\
                        or '</ScreenCheck>' in textes[se:sre] \
                        or '</DeleteCheck>' in textes[se:sre] \
                        or '</StoreCheck>' in textes[se:sre] \
                        or '</QuitOrder>' in textes[se:sre] \
                        or '</OpenOrder>' in textes[se:sre] \
                        or '</CloseCheck>' in textes[se:sre]:
                    if byted:
                        new_textes = temp + textes
                        textes = new_textes
                        print('Собрано\n'
                              , textes)

                    if ifwanted:
                        d = threading.Thread(target=detect_situation, args=(textes, bot, lock))
                        d.start()
                    ifwanted = False
                    byted = False
                else:
                    if ifwanted:
                        temp = textes
                        byted = True

            except Exception as e:
                textes = pal.decode(encoding="WINDOWS-1251")
                d = threading.Thread(target=detect_situation, args=(textes, bot, lock))
                d.start()
                clear = ['temp_reports/buffer.txt', 'temp_reports/current_money.txt', 'temp_reports/deleted_check.txt',
                         'temp_reports/deleted_prech.txt', 'temp_reports/eaten_eat.txt', 'temp_reports/deleted_disc.txt'
                    , 'temp_reports/fast_sell.txt', 'temp_reports/boun_rec.txt', 'temp_reports/discount.txt',
                         'temp_reports/time_sell.txt']
                print(e)
                print("Windows 1251 Получено от %s:%s:" % addr)
                pal.decode(encoding="WINDOWS-1251")
                x = threading.Thread(target=addons.send_new_alarm, args=(
                    pal.decode(encoding="WINDOWS-1251"), 'subscrubers/end_of_shift_subs.txt', bot, lock))
                x.start()
                for file in clear:
                    with open(file, 'w', encoding='UTF-8') as e:
                        print('очищено')

                print(pal.decode(encoding="WINDOWS-1251"))
