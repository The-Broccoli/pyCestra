import os

from core.logging_handler import Logging, bcolors
from exchange.exchange_client import ExchangeClient

def main():
    #  ======================================================
    #  start message

    log = Logging()

    def clear(): return os.system('cls')
    clear()

    def wel():
        welmsg = [31*"─", "|   pyCestra - Logon Server   |", 31*"─"]
        for x in welmsg:
            print(bcolors.blue + x + bcolors.cend)
    wel()

    #  ======================================================
    #  exchange client test

    log.debug('Client Start')
    ExchangeClient().test()

if __name__ == '__main__':
    main()
