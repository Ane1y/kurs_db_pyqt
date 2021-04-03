from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox, QLineEdit
from cryptography.fernet import Fernet

import filler
import sql
import user_info
from sign_up import Ui_Dialog as sign_up
from pat_lk_controller import pat_lkWindow
#import sign_in_controller as sign_in


class sign_upWindow(QtWidgets.QMainWindow):
    def __init__(self) :
        super().__init__()
        self.ui = sign_up()
        self.ui.setupUi(self)
        self.setWindowTitle("Регистрация нового пациента")

        self.db = sql.Sql()

        self.ui.password_lineEdit.setEchoMode(QLineEdit.Password)
        self.ui.check_password_lineEdit.setEchoMode(QLineEdit.Password)

        self.ui.back_button.clicked.connect(self.back_button_clicked)
        self.ui.sign_up_button.clicked.connect(self.sign_up_button_clicked)

        # self.ui.passwodCheckbox. stateChanged.connect(self.checkboxHandler)
        # self.ui.createAccountButton.clicked.connect(self.createButton_clicked)

    def back_button_clicked(self):
        print("Bibop")
        #self.main = sign_in.loginWindow()
        #self.main.show()
        self.close()

    def sign_up_button_clicked(self):
        name = str(self.ui.name_lineEdit.text())
        date_of_birth = self.ui.date_of_birth_dateEdit.date().toPyDate()
        passport = str(self.ui.passport_lineEdit.text())
        phone = str(self.ui.phone_lineEdit.text())
        password = str(self.ui.password_lineEdit.text())
        check_password = str(self.ui.check_password_lineEdit.text())
        snils = str(self.ui.snils_lineEdit.text())
        insurance = str(self.ui.insurance_lineEdit.text())
        contract_num = str(self.ui.contract_num_lineEdit.text())

        if filler.check_correctness_sign_up_data_for_patient(self, name, date_of_birth, passport, phone, password, check_password, snils, insurance, contract_num):
            try:
                cipher = Fernet(user_info.cipher_key)
                encrypted_password = password.encode('utf8')
                encrypted_password = cipher.encrypt(encrypted_password)

                self.db.cursor.execute("INSERT INTO authentication_data (password, phone) "
                                       "Values ('" + encrypted_password.decode('utf8') + "', '" + phone + "')")
                self.db.cnxn.commit()
                self.db.cursor.execute("SELECT id from authentication_data Where phone = '" + phone + "'")
                new_id = self.db.cursor.fetchone()

                self.db.cursor.execute(
                    "INSERT INTO patients (name, user_id, date_of_birth, passport, snils, insurance_policy, contract_num) "
                    "VALUES (%s, %s, %s, %s, %s, %s, %s)",
                    (name, new_id, date_of_birth, passport, snils, insurance, contract_num))
                self.db.cnxn.commit()

                self.ui.password_lineEdit.clear()
                self.ui.phone_lineEdit.clear()
                self.ui.passport_lineEdit.clear()
                self.ui.date_of_birth_dateEdit.clear()
                self.ui.name_lineEdit.clear()
                self.ui.check_password_lineEdit.clear()
                self.ui.snils_lineEdit.clear()
                self.ui.insurance_lineEdit.clear()
                self.ui.contract_num_lineEdit.clear()
                user_info.current_userID = new_id
                user_info.current_role = "patient"
                self.menu = pat_lkWindow()
                self.main.close()
                self.menu.show()
            except (Exception, sql.psycopg2.Error) as error:
                error_message = QtWidgets.QErrorMessage(self)
                error_message.setWindowTitle("Ошибка")
                error_message.showMessage('Ошибка с подключением к SQL')

