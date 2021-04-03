import sys

from PyQt5 import QtWidgets
from sign_in_controller import loginWindow
from sign_up_controller import sign_upWindow as signUpWindow
from sql import Sql
from admin_controller import Admin_Controller
if __name__ == '__main__':
    db = Sql()

    app = QtWidgets.QApplication([])
    #window = Admin_Controller()
    window = loginWindow()
    window.show()
    db.cnxn.close()
    sys.exit(app.exec())
