import pymysql.cursors
import typing

import dataSource
from core.logging_handler import Logging
from dataSource.DAO import DAO


class AccountData(DAO):

    def __init__(self):
        self.log = Logging()

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

    # Use databank account ID to find the right account
    def get_from_id(self, idwis):
        '''
        preloading necessary!
        '''
        if not idwis == 0:
            account = idwis - 1
            return self.Datasource[account]
        else:
            self.log.warning('account_data.py - Can\'t load account id 0')

    def get_from_name(self, name):
        data = super().get_data("SELECT * FROM accounts WHERE account = '" + str(name) + "';")
        if (isinstance(data, typing.List)):
            if (isinstance(data[0], typing.Dict)):
                return data[0]
            return 0
        return 0
