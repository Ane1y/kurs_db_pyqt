import psycopg2
from PyQt5 import QtWidgets

import filler
import sql
from user_info import current_userID as doc_id
from doc_lk import Ui_Dialog as Doc_lk
import user_info
import datetime
from admin_controller import Admin_Controller
class doc_lkWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Doc_lk()
        self.ui.setupUi(self)
        self.setWindowTitle("Medical Clinic -- для врача")
        if user_info.admin :
            self.ui.admin_menu_button.clicked.connect(self.admin_menu_button_clicked)
        else:
            self.ui.admin_menu_button.setVisible(False)
        self.db = sql.Sql()

        self.setInitialValues()

        self.ui.change_nummer_button.clicked.connect(self.change_nummer_button_clicked)
        self.ui.exit_button.clicked.connect(self.exit_button_clicked)
        self.ui.add_record_Button.clicked.connect(self.add_record_Button_clicked)
        self.ui.patients_comboBox.currentIndexChanged.connect(self.patients_change)
        self.ui.form_queue_button.clicked.connect(self.form_queue_button_clicked)
        self.ui.show_all_med_record_button.clicked.connect(self.show_all_med_records)
        self.ui.change_med_record_button.clicked.connect(self.change_med_record)
        self.ui.date_med_record_button.clicked.connect(self.show_by_date)

        self.show()

    def show_by_date(self) :
        date = self.ui.date_med_record_dateEdit.date().toPyDate()
        self.db.cursor.execute("SELECT date, P.name, diagnosis FROM medical_records "
                               "LEFT JOIN Patients P on P.id = patient_id "
                               "WHERE physician_id = (SELECT id FROM physicians WHERE user_id = '"
                               + str(user_info.current_userID) + "') and date = '" + str(date) + "' ORDER BY date desc")
        filler.fillTable(self.ui.med_journal_tableWidget, self.db.cursor, 3)

    def change_med_record(self) :
        new_diagnosis = str(self.ui.new_diagnosis_textEdit.toPlainText())
        self.db.cursor.execute("UPDATE Medical_records "
                                   "SET diagnosis = %s "
                                   "WHERE (id = (SELECT id FROM Medical_records WHERE physician_id = %s "
                                   "ORDER BY id DESC LIMIT 1))", (new_diagnosis, str(user_info.current_userID)));

        self.db.cnxn.commit()
        self.show_all_med_records()

    def show_all_med_records(self) :
        self.db.cursor.execute("SELECT date, P.name, diagnosis FROM medical_records "
                               "LEFT JOIN Patients P on P.id = patient_id "
                               "WHERE physician_id = (SELECT id FROM physicians WHERE user_id = '"
                               + str(user_info.current_userID) + "') ORDER BY date desc")
        filler.fillTable(self.ui.med_journal_tableWidget, self.db.cursor, 3)

    def show_in_selected_date(self) :
        date = self.ui.date_med_record_dateEdit.date().toPyDate()
        self.db.cursor.execute("SELECT date, P.name, diagnosis FROM medical_records "
                               "LEFT JOIN Patients P on P.id = patient_id "
                               "WHERE physician_id = (SELECT id FROM physicians WHERE user_id = '"
                               + str(user_info.current_userID) + "' and date = '" + str(date) + "') ORDER BY date desc")
        filler.fillTable(self.ui.med_journal_tableWidget, self.db.cursor, 3)

    def patients_change(self):
        print("Change patient")
        self.ui.med_card_tableWidget.setRowCount(0)
        current_patient = str(self.ui.patients_comboBox.currentText())

        sqlcmd = ("SELECT date, Ph.name, diagnosis FROM medical_records "
                               "LEFT JOIN Physicians Ph on Ph.id = physician_id "
                               "WHERE patient_id = (SELECT id FROM patients WHERE name = '"
                               + current_patient + "') ORDER BY date desc")
        self.db.cursor.execute(sqlcmd)

        filler.fillTable(self.ui.med_card_tableWidget, self.db.cursor, 3)


    def change_nummer_button_clicked(self):
        filler.changeNummer(self)

    def admin_menu_button_clicked(self) :
        self.menu = Admin_Controller()
        self.menu.show()

    def exit_button_clicked(self):
        filler.exitButton(self)


    def form_queue_button_clicked(self):
        days = str(self.ui.queue_days_box.value())

        self.db.cursor.execute("SELECT P.name, Q.time FROM Queue Q LEFT JOIN Patients P on P.id = Q.patient_id "
                               "WHERE ((physician_id = %s)  AND (time > current_timestamp) AND (time < current_timestamp + interval %s day))",
                               (user_info.current_userID, days))

        filler.fillTable(self.ui.Queue_tableWidget, self.db.cursor, 2)


    def add_record_Button_clicked(self):
        diagnosis = str(self.ui.diagnosis_textBrowser.toPlainText())
        if not(diagnosis.isalnum()) and len(diagnosis) < 3 :
            error_message = QtWidgets.QErrorMessage(self)
            error_message.setWindowTitle("Некорректный ввод")
            error_message.showMessage('Подозрительный диагноз')
        else :
            name = str(self.ui.patients_comboBox.currentText())
            service = str(self.ui.service_comboBox.currentText())
            try:
                self.db.cursor.execute("INSERT INTO medical_records(patient_id, physician_id, date, diagnosis, service_id)" \
                        "VALUES ((SELECT id FROM patients WHERE name = %s), %s, %s, %s, "
                        "(SELECT id FROM Services WHERE name = %s))",
                        (name, user_info.current_userID, datetime.datetime.today().strftime('%Y-%m-%d'), diagnosis, service))

                self.db.cnxn.commit()
                self.patients_change()
                print("smth happened")
            except (Exception, psycopg2.Error) as error:
                print("Error while connecting to PostgreSQL", error)


    def setInitialValues(self):
        self.ui.date_label.setText(str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M")))

        doc_id = user_info.current_userID
        self.db.cursor.execute("SELECT name from Physicians where user_id= '" + str(doc_id) + "'")
        doc_name = self.db.cursor.fetchone()
        self.ui.name_label.setText(doc_name[0])

        self.db.cursor.execute(
            "SELECT S.name, S.id from Physicians Ph LEFT JOIN Specialization S on Ph.specialization_id = S.id WHERE Ph.user_id=" + str(
                doc_id))
        spec_name = self.db.cursor.fetchone()
        self.ui.spezialization_label.setText(spec_name[0])

        self.db.cursor.execute("SELECT passport from Physicians where user_id=" + str(doc_id))
        pas_name = self.db.cursor.fetchone()
        self.ui.passport_label.setText(str(pas_name[0]))

        self.db.cursor.execute("SELECT date_of_birth from Physicians where user_id=" + str(doc_id))
        date_of_birth = self.db.cursor.fetchone()
        self.ui.date_of_birth_label.setText(str(date_of_birth[0]))

        self.db.cursor.execute("SELECT phone from  authentication_data  WHERE id= %s", str(user_info.current_userID))
        phone = self.db.cursor.fetchone()
        self.ui.phone_number_box.setText(str(phone[0]))

        self.db.cursor.execute("SELECT name from Patients")
        filler.fillComboBox(self.ui.patients_comboBox, self.db.cursor)

        self.db.cursor.execute("SELECT name from Services where specialization_id = %s" , str(spec_name[1]))
        filler.fillComboBox(self.ui.service_comboBox, self.db.cursor)

        self.form_queue_button_clicked()
        self.show_all_med_records()

