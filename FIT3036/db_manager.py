import mysql.connector
from mysql.connector import errorcode


class DatabaseUtility:
    def __init__(self):
        self.db = 'enron'
        self.table_name = 'employeelist'

        f = open('/home/osboxes/Desktop/FIT3036/password.txt', 'r')
        p = f.read().rstrip('\n')
        f.close()
        self.cnx = mysql.connector.connect(user = 'root',
                                           password = p,
                                           host = '127.0.0.1')
        self.cursor = self.cnx.cursor()

        self.connect_to_database()

    def connect_to_database(self):
        try:
            self.cnx.database = self.db
        except mysql.connector.Error as err:
            print(err.msg)

    def get_table(self, table_name):
        return self.run_command("SELECT * FROM %s;" % table_name)

    def get_table_names(self):
        return self.run_command("SHOW TABLES;")

    def get_columns(self, table_name):
        return self.run_command("SHOW COLUMNS FROM %s;" % table_name)

    def get_eid(self):
        return sorted(self.run_command("SELECT * FROM employeelist;"))

    def get_communication(self):
        return self.run_command("SELECT * FROM contact;")

    def run_command(self, cmd):
        print("RUNNING COMMAND: " + cmd)
        try:
            self.cursor.execute(cmd)
        except mysql.connector.Error as err:
            print('ERROR MESSAGE: ' + str(err.msg))
            print('WITH ' + cmd)
        try:
            msg = self.cursor.fetchall()
        except:
            msg = self.cursor.fetchone()

        return msg

    # def __del__(self):
    #     self.cnx.commit()
    #     self.cursor.close()
    #
    #     self.cnx.close()


if __name__ == '__main__':
    dbu = DatabaseUtility()
    print(str(dbu.get_eid()))