import pymysql.cursors

import dataSource
from core.logging_handler import Log
from dataSource.DAO import DAO


class AccountData(DAO):

    def __init__(self):
        self.log = Log()


    def load(self):
            '''
            DataFrame:
            
            '''
            self.Datasource = []
            connection = dataSource.Database().get_connection()
            cursor = connection.cursor()
            try:
                cursor.execute('SELECT * FROM accounts;')
                data = cursor.fetchall()
                for row in data:
                    Rows = [row]
                    self.Datasource.append(Rows)
            except:
                self.log.warning(' account_data.py - Can\'t load table accounts')
                cursor.close()
                connection.close()
            finally:
                cursor.close()
                connection.close()
                self.log.debug('cursor.close, connection.close')

    # Use databank account ID to find the right account
    def get_from_id(self, idwis):
        if not idwis == 0:
            account = idwis - 1
            return self.Datasource[account]
        else:
            self.log.warning('account_data.py - Can\'t load account id 0')
    
    def set(self, ip):
        pass
