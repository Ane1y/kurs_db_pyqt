from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QLineEdit

import user_info
from sign_in import Ui_Dialog as loginmain
from doc_lk_controller import doc_lkWindow
from sign_up_controller import sign_upWindow
from pat_lk_controller import pat_lkWindow
import sql

class loginWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = loginmain()
        self.ui.setupUi(self)
        self.setWindowTitle("Вход")
        self.ui.sign_in_button.clicked.connect(self.sign_in_button_clicked)
        self.ui.sign_up_button.clicked.connect(self.sign_up_button_clicked)
        self.ui.password_lineEdit.setEchoMode(QLineEdit.Password)

        self.db = sql.Sql()

    def sign_in_button_clicked(self):
        l = self.ui.phone_lineEdit.text()
        p = self.ui.password_lineEdit.text()
        if (l.strip() == ''):
            message = "Введите номер телефона"
            error_message = QtWidgets.QErrorMessage(self)
            error_message.setModal(True)
            error_message.setWindowTitle("Ошибка входа")
            error_message.showMessage(message)
            if len(l) != 0:
                self.ui.phone_lineEdit.clear()
            self.ui.password_lineEdit.clear()
        elif (p.strip() == ''):
            message = "Пароль не введен. Попробуйте еще раз!"
            error_message = QtWidgets.QErrorMessage(self)
            error_message.setModal(True)
            error_message.setWindowTitle("Ошибка входа")
            error_message.showMessage(message)
            if len(p) != 0:
                self.ui.password_lineEdit.clear()

        elif not(l.isdecimal()):

            message = "Недопустимый символ в поле логина. Проверьте правильность данных и повторите вход."
            error_message = QtWidgets.QErrorMessage(self)
            error_message.setModal(True)
            error_message.setWindowTitle("Ошибка входа")
            error_message.showMessage(message)
            self.ui.phone_lineEdit.clear()
            self.ui.password_lineEdit.clear()

        elif (p.find(' ') != -1):
            message = "Данного пользователя не существует или введен неверный пароль! Проверьте правильность данных и повторите вход."
            error_message = QtWidgets.QErrorMessage(self)
            error_message.setModal(True)
            error_message.setWindowTitle("Ошибка входа")
            error_message.showMessage(message)
            self.ui.password_lineEdit.clear()

        else: # если прошли все проверки начинаем проверку пользователя по БД
            status, role, id = self.db.checkPassword(l, p)
            if (status == False):
                message = "Не найден пользователь с таким логином/паролем"
                error_message = QtWidgets.QErrorMessage(self)
                error_message.setModal(True)
                error_message.setWindowTitle("Ошибка входа")
                error_message.showMessage(message)
                self.ui.password_lineEdit.clear()
            else:
                user_info.current_role = role
                user_info.current_userID = id
                if user_info.current_role == "physician":
                    self.db.cursor.execute("SELECT role_id from physicians where user_id = %s", str(id))
                    role_id = self.db.cursor.fetchone()
                    if role_id[0] == 2:
                        user_info.admin = True
                    self.menu = doc_lkWindow()
                else:
                     self.menu = pat_lkWindow()
                self.close()
                self.menu.show()



    def sign_up_button_clicked(self):
        self.main = sign_upWindow()
        self.main.show()
        self.close()