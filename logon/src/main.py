import sys

from Database import Database
from PacketHandler import PacketHandler

if __name__ == "__main__":

    def wel():
        welmsg = [31*"─","|   pyCestra - Logon Server   |",31*"─"]
        for x in welmsg:
            print(x)

    wel()
    
    # PacketHandler().TestSocket()

    if Database().testConnection():
        print("Datenbank Connection Test Erfolgreich")
    else:
        print("Datanbank nicht gefunden!")
        sys.exit
    pass