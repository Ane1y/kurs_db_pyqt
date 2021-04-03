import psycopg2
from cryptography.fernet import Fernet

import user_info


class Sql:
    def __init__(self):  # конструктор, self = this, если используется нужно обьявлять, неявно не задано
        try:
            self.cnxn = psycopg2.connect(user="postgres",
                                         password="admin",
                                         host="localhost",
                                         port="5432",
                                         database="polyclinic",
                                         options="-c search_path=dbo,public")
            self.cursor = self.cnxn.cursor()

            print(self.cnxn.get_dsn_parameters(), "\n")

        # Print PostgreSQL version
            self.cursor.execute("SELECT version();")
            record = self.cursor.fetchone()
            print("You are connected to - ", record, "\n")

        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgreSQL", error)

    def checkPassword(self, login, password):
        cipher = Fernet(user_info.cipher_key)
        temp = "(SELECT id from authentication_data WHERE phone = '" + login + "')"
        self.cursor.execute("SELECT id, password, CASE " \
            "when exists (select true from physicians where user_id = " + temp + ") then 'physician' " \
            "when exists (select true from patients where user_id = " + temp + ") then 'patient' " \
            "ELSE '0' " \
            "END FROM authentication_data WHERE phone = '" + login + "'")
        row = self.cursor.fetchone()
        if row is not None:
            passw = cipher.decrypt(str.encode(row[1])).decode('utf8')
            if password == passw:
                return True, row[2], row[0]
            else:
                return False, row[2], row[0]
        else:
            return False, 0, 0