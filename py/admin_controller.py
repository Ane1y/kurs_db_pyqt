import datetime

import psycopg2
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMessageBox

import filler
import sql
from admin_panel import  Ui_Dialog as admin_panel


class Admin_Controller(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = admin_panel()
        self.ui.setupUi(self)
        self.setWindowTitle("Medical Clinic -- для администратора")

        self.db = sql.Sql()
        self.initialValues()

        self.ui.delete_button.clicked.connect(self.delete_patient_clicked)
        self.ui.show_all_ph_button.clicked.connect(self.show_all_physicians)
        self.ui.queue_button.clicked.connect(self.queue_button_clicked)
        self.ui.choose_spec_comboBox.currentIndexChanged.connect(self.show_by_spec_clicked)
        self.ui.show_lazy_doctors_button.clicked.connect(self.show_lazy_doctors)
        self.ui.finance_button.clicked.connect(self.create_finance_report)
        self.ui.sign_up_button.clicked.connect(self.sign_up_button_clicked)
        self.ui.delete_physician_button.clicked.connect(self.delete_physician)
        self.ui.all_physician_report_button.clicked.connect(self.finrep_for_all_physician)
        self.ui.show_all_med_card_button.clicked.connect(self.show_all_med_card)
        self.ui.show_all_med_card_changes.clicked.connect(self.show_all_changes_med_card)
        self.ui.spec_who_change_med_card_comboBox.currentIndexChanged.connect(self.show_changer_of_med_card)
        self.ui.physician_med_card_comboBox.currentIndexChanged.connect(self.physician_med_card_changed)
        self.ui.patients_med_card_comboBox.currentIndexChanged.connect(self.patient_med_card_changed)
        self.ui.delete_service_button.clicked.connect(self.delete_service)
        self.ui.add_service_button.clicked.connect(self.add_service)
        self.ui.add_specialization_button.clicked.connect(self.add_specialization)
        self.ui.delete_specialization_button.clicked.connect(self.delete_specialization)

    def initialValues(self) :
        self.db.cursor.execute("SELECT name, date_of_birth, ad.phone, passport, snils, insurance_policy, contract_num "
                               "FROM patients "
                               "LEFT JOIN authentication_data ad on ad.id = user_id")
        filler.fillTable(self.ui.patients_tableWidget, self.db.cursor, 7)

        self.queue_button_clicked()
        self.show_all_physicians()
        self.ui.finance_info_label.setVisible(False)
        self.db.cursor.execute("SELECT name from specialization")
        filler.fillComboBox(self.ui.choose_spec_comboBox, self.db.cursor)
        self.db.cursor.execute("SELECT name from specialization")
        filler.fillComboBox(self.ui.spec_comboBox, self.db.cursor)

        self.db.cursor.execute("SELECT name from physicians")
        filler.fillComboBox(self.ui.physicians_finance_comboBox, self.db.cursor)

        self.show_all_med_card()

        self.db.cursor.execute("SELECT Distinct Ph.name from medical_record_audit "
                               "LEFT JOIN medical_records mr on medical_record_audit.mr_id = mr.id "
                               "Left Join physicians ph on mr.physician_id = ph.id")
        filler.fillComboBox(self.ui.spec_who_change_med_card_comboBox, self.db.cursor)

        self.db.cursor.execute("SELECT Ph.name from medical_records mr "
                               "Left Join physicians ph on mr.physician_id = ph.id")
        filler.fillComboBox(self.ui.physician_med_card_comboBox, self.db.cursor)

        self.db.cursor.execute("SELECT P.name from medical_records mr "
                               "Left Join patients p on mr.patient_id = p.id")
        filler.fillComboBox(self.ui.patients_med_card_comboBox, self.db.cursor)

        self.show_all_changes_med_card()

        self.db.cursor.execute("Select name from specialization")
        filler.fillComboBox(self.ui.specialization_comboBox, self.db.cursor)
        self.show_services()
        self.show_specializations()


    def delete_service(self) :
        for index in sorted(self.ui.service_tableWidget.selectionModel().selectedRows()):
            row = index.row()
            index = self.ui.service_tableWidget.model().index(row, 0)
            name = str(self.ui.service_tableWidget.model().data(index))
            self.ui.service_tableWidget.model().removeRow(row)
            self.db.cursor.execute("DELETE FROM services WHERE name = '" + name + "'")
            self.db.cnxn.commit()
            self.show_services()

    def show_specializations(self) :
        self.db.cursor.execute("SELECT name from specialization")
        filler.fillTable(self.ui.specialization_tableWidget, self.db.cursor, 1)

    def add_specialization(self) :
        spec_name = str(self.ui.specialization_lineEdit.text())
        self.db.cursor.execute("INSERT INTO specialization (name) Values ( '" + spec_name + "')")
        self.db.cnxn.commit()
        self.show_specializations()

    def delete_specialization(self):
        try:
            for index in sorted(self.ui.specialization_tableWidget.selectionModel().selectedRows()):
                row = index.row()
                index = self.ui.specialization_tableWidget.model().index(row, 0)
                name = str(self.ui.specialization_tableWidget.model().data(index))
                self.db.cursor.execute("DELETE from specialization Where name = '" + name + "'")
                self.db.cnxn.commit()
                self.show_specializations()

        except (Exception, psycopg2.Error) as error :
            error_message = QtWidgets.QErrorMessage(self)
            error_message.setWindowTitle("Некорректное действие")
            error_message.showMessage('Удаление этой услуги повлияет на данные в таблице медицинских записей. Невозможно выполнить действие')


    def show_services(self) :
        self.db.cursor.execute("SELECT s.name, cost, sp.name from Services S "
                               "left join specialization sp on sp.id = S.specialization_id")
        filler.fillTable(self.ui.service_tableWidget, self.db.cursor, 3)


    def add_service(self) :
        name = str(self.ui.service_name_lineEdit.text())
        cost = str(self.ui.servise_cost_lineEdit.text())
        spec = str(self.ui.specialization_comboBox.currentText())
        self.db.cursor.execute("SELECT id FROM specialization WHERE name = '" + spec + "'")
        spec_id = self.db.cursor.fetchone()
        self.db.cursor.execute("INSERT INTO services(name, cost, specialization_id) "
                               "VALUES (%s, %s, %s)", (name, cost, spec_id[0]))
        self.db.cnxn.commit()
        self.show_services()

    def patient_med_card_changed(self) :
        self.ui.physician_med_card_comboBox.setCurrentIndex(0)
        name = str(self.ui.patients_med_card_comboBox.currentText())
        self.db.cursor.execute("SELECT date, p.name, ph.name, diagnosis, s.name from medical_records mr "
                               "LEFT JOIN services s on s.id = mr.service_id "
                               "LEFT JOIN patients p on mr.patient_id = p.id "
                               "LEFT JOIN physicians ph on mr.physician_id = ph.id "
                               "Where p.name = '" + name + "'")
        filler.fillTable(self.ui.med_card_tableWidget, self.db.cursor, 5)

    def physician_med_card_changed(self):
        self.ui.patients_med_card_comboBox.setCurrentIndex(0)
        name = str(self.ui.physician_med_card_comboBox.currentText())
        self.db.cursor.execute("SELECT date, p.name, ph.name, diagnosis, s.name from medical_records mr "
                               "LEFT JOIN services s on s.id = mr.service_id "
                               "LEFT JOIN patients p on mr.patient_id = p.id "
                               "LEFT JOIN physicians ph on mr.physician_id = ph.id "
                               "Where ph.name = '" + name + "'")
        filler.fillTable(self.ui.med_card_tableWidget, self.db.cursor, 5)

    def show_changer_of_med_card(self):
        name = str(self.ui.spec_who_change_med_card_comboBox.currentText())
        self.db.cursor.execute("SELECT Ph.name, mra.time, mr.diagnosis, mr.date, mra.old_diagnosis from medical_record_audit mra "
                               "LEFT JOIN medical_records mr on mra.mr_id = mr.id "
                               "Left Join physicians ph on mr.physician_id = ph.id "
                               "WHERE Ph.name = '" + name + "'")
        filler.fillTable(self.ui.med_record_audit_tableWidget, self.db.cursor, 5)

    def show_all_changes_med_card(self):
        self.db.cursor.execute(
            "SELECT Ph.name, mra.time, mr.diagnosis, mr.date, mra.old_diagnosis from medical_record_audit mra "
            "LEFT JOIN medical_records mr on mra.mr_id = mr.id "
            "Left Join physicians ph on mr.physician_id = ph.id")
        filler.fillTable(self.ui.med_record_audit_tableWidget, self.db.cursor, 5)

    def delete_patient_clicked(self) :
        filler.delete_row(self, self.ui.patients_tableWidget, "Patients", 3)

    def delete_physician(self) :
        filler.delete_row(self, self.ui.physician_tableWidget, "Physicians",4)

    def open_doc_menu(self) :
        self.menu = Admin_Controller()
        self.main.close()
        self.menu.show()

    def show_all_med_card(self):
        self.db.cursor.execute("SELECT date, p.name, ph.name, diagnosis, s.name from medical_records mr "
                               "LEFT JOIN services s on s.id = mr.service_id "
                               "LEFT JOIN patients p on mr.patient_id = p.id "
                               "LEFT JOIN physicians ph on mr.physician_id = ph.id")
        filler.fillTable(self.ui.med_card_tableWidget, self.db.cursor, 5)

    def queue_button_clicked(self):
        days = str(self.ui.queue_day_spinBox.value())

        self.db.cursor.execute("SELECT Q.time, Ph.name, P.name FROM Queue Q "
                               "LEFT JOIN Patients P on P.id = Q.patient_id "
                               "LEFT JOIN Physicians Ph on Ph.id = Q.physician_id "
                               "WHERE (time > current_timestamp) AND (time < current_timestamp + interval '" + days + "' day) "
                               "ORDER BY Q.time desc")

        filler.fillTable(self.ui.queue_tableWidget, self.db.cursor, 3)


    def show_all_physicians(self) :
        self.db.cursor.execute(
            "SELECT ph.name, sp.name, ad.phone, date_of_birth, passport, r.name FROM physicians ph "
            "LEFT JOIN specialization sp on sp.id = specialization_id "
            "LEFT JOIN authentication_data ad on ad.id = ph.user_id "
            "LEFT JOIN roles r on r.id = role_id")
        filler.fillTable(self.ui.physician_tableWidget, self.db.cursor, 6)

    def show_by_spec_clicked(self):
        spec = str(self.ui.choose_spec_comboBox.currentText())
        if len(spec) > 0:
            self.db.cursor.execute("SELECT ph.name, S.name, ad.phone, date_of_birth, passport, r.name FROM Physicians Ph "
                                   "LEFT JOIN Specialization S ON Ph.specialization_id = S.id "
                                   "LEFT JOIN roles r on r.id = role_id "
                                   "LEFT JOIN authentication_data ad on ad.id = ph.user_id "
                                   "WHERE S.name = '" + spec + "'")
            filler.fillTable(self.ui.physician_tableWidget, self.db.cursor, 6)


        else:
            self.ui.physician_tableWidget.setRowCount(0)

    def show_lazy_doctors(self):

        hours = str(self.ui.hours_spinBox.value())
        days = str(self.ui.days_spinBox.value())
        if hours.isdecimal() and days.isdecimal():
            self.db.cursor.execute("SELECT ph.name, S.name, ad.phone, date_of_birth, passport, r.name FROM Physicians Ph "
                               "LEFT JOIN Specialization S ON Ph.specialization_id = S.id "
                               "LEFT JOIN roles r on r.id = role_id "
                               "LEFT JOIN authentication_data ad on ad.id = ph.user_id "                               
                               "RIGHT JOIN (SELECT * FROM printListOfLazyDoctors(%s, %s)) as foo on foo.name = ph.name", (hours, days))

            filler.fillTable(self.ui.physician_tableWidget, self.db.cursor, 6)

    def create_finance_report(self) :
        self.ui.finance_info_label.setVisible(False)

        self.ui.finance_tableWidget.clear()

        self.ui.finance_tableWidget.setColumnCount(3)
        #self.finance_tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.ui.finance_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.ui.finance_tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.ui.finance_tableWidget.setHorizontalHeaderItem(2, item)

        _translate = QtCore.QCoreApplication.translate
        item = self.ui.finance_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "ФИО пациента"))
        item = self.ui.finance_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Услуга"))
        item = self.ui.finance_tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Стоимость"))

        current_doc = str(self.ui.physicians_finance_comboBox.currentText())
        days_interval = str(self.ui.finance_day_spinBox.value())
        if len(current_doc) > 0:
            self.db.cursor.execute("SELECT * FROM getfinanceReport(%s, %s)", (current_doc, days_interval))
            filler.fillTable(self.ui.finance_tableWidget, self.db.cursor, 3)
            self.db.cursor.execute("SELECT sum(foo.cost) from (SELECT * FROM getfinanceReport(%s, %s)) as foo", (current_doc, days_interval))
            result = self.db.cursor.fetchone()
            self.ui.total_label.setText(str(result[0]))

    def finrep_for_all_physician(self):
        self.ui.finance_info_label.setVisible(True)

        self.ui.finance_tableWidget.clear()
        self.ui.finance_tableWidget.setColumnCount(2)

        item = QtWidgets.QTableWidgetItem()
        self.ui.finance_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.ui.finance_tableWidget.setHorizontalHeaderItem(1, item)

        _translate = QtCore.QCoreApplication.translate

        item = self.ui.finance_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "ФИО врача"))
        item = self.ui.finance_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Заработал"))

        self.db.cursor.execute("SELECT Ph.name, cost From finance_report fr Left Join physicians Ph on Ph.id = fr.physician_id")
        filler.fillTable(self.ui.finance_tableWidget, self.db.cursor, 2)

    def sign_up_button_clicked(self) :
        name = str(self.ui.name_lineEdit.text())
        date_of_birth = self.ui.date_of_birth_dateEdit.date().toPyDate()
        passport = str(self.ui.passport_lineEdit.text())
        spec = str(self.ui.spec_comboBox.currentText())
        phone = str(self.ui.phone_lineEdit.text())
        password = str(self.ui.password_lineEdit.text())

        if filler.check_correctness(self, name, date_of_birth, passport, phone, password, 18) :
            try :
                self.db.cursor.execute("Select id from specialization where name = '" + spec + "'")
                spec_id = self.db.cursor.fetchone()
                self.db.cursor.execute("INSERT INTO authentication_data (password, phone) "
                                       "Values ('" + password + "', '" + phone + "')")
                self.db.cnxn.commit()
                self.db.cursor.execute("SELECT id from authentication_data Where phone = '" + phone + "'")
                new_id = self.db.cursor.fetchone()
                role_id = 1
                if self.ui.admin_checkBox.isChecked():
                    role_id = 2
                self.db.cursor.execute("INSERT INTO physicians (name, role_id, user_id, passport, date_of_birth, specialization_id) "
                                       "Values (%s, %s, %s, %s, %s, %s)", (name, role_id, new_id[0], passport, date_of_birth, spec_id[0]))
                self.db.cnxn.commit()
                msg = QtWidgets.QMessageBox(self)
                msg.setIcon(QMessageBox.Information)
                msg.setWindowTitle("Успех")
                msg.setText("Успешно!")
                msg.show()

                self.ui.password_lineEdit.clear()
                self.ui.phone_lineEdit.clear()
                self.ui.passport_lineEdit.clear()
                self.ui.date_of_birth_dateEdit.clear()
                self.ui.name_lineEdit.clear()

            except (Exception, psycopg2.Error) as error:
                error_message = QtWidgets.QErrorMessage(self)
                error_message.setWindowTitle("Проверьте корректность ввода")
                error_message.showMessage('Такой телефон уже зарегистрирован в базе')

