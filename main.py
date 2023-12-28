import time
from os.path import exists
from better_proxy import Proxy
from arkana import *
from loguru import logger as lo

lo.add("logger.log", format="{time:YYYY-MM-DD | HH:mm:ss.SSS} | {level} \t| {function}:{line} - {message}")

def main():
    if exists(path='proxy.txt'):
        proxies_list = [proxy.as_url for proxy in Proxy.from_file(filepath='proxy.txt')]
    else:
        proxies_list = []

    if exists(path='email_data.txt'):
        with open(file='email_data.txt', mode='r', encoding='utf-8-sig') as file:
            accounts_list = [row.strip() for row in file]
    else:
        accounts_list = []

    if exists(path='successfully_registered.txt'):
        with open(file='successfully_registered.txt', mode='r', encoding='utf-8-sig') as file:
            successfully_accounts_list = [row.strip() for row in file]
    else:
        successfully_accounts_list = []

    if exists(path='ref.txt'):
        with open(file='ref.txt', mode='r', encoding='utf-8-sig') as file:
            ref_code_list = [row.strip() for row in file]
    else:
        ref_code_list = []

    lo.success(f'Успешно загружены {len(accounts_list)} аккаунты для регистрации | {len(ref_code_list)} реферальные коды')
    lo.success(
        f'Успешно загружены {len(successfully_accounts_list)} успешно зарегистрированные аккаунты | {len(proxies_list)} прокси')
    time.sleep(2)

    software_method = int(input('\n1. Регистрация аккаунтов\n'
                                '2. Фарминг ежедневных поинтов\n'
                                'Сделайте свой выбор:\n'))
    print()

    if software_method == 1:
        for account in accounts_list:
            email_adress, apps_password, imap = account.split(';')
            make_arkana_acounts(email_adress, apps_password, imap)
            time.sleep(3)
            print()
    elif software_method == 2:
        for account in accounts_list:
            email_adress, apps_password, imap = account.split(';')
            total_daily_claim(email_adress, apps_password, imap)
            time.sleep(31)
            print()
    else:
        lo.error("Неизвестный метод, выберите 1 или 2!")

    time.sleep(5)
    print()
    lo.success('Работа успешно завершена')

    time.sleep(5)
    input('\nНажмите Enter, чтобы выйти..')

main()


