
from PyQt5 import QtWidgets

import filler
import sql
import psycopg2
import user_info
from pat_lk import Ui_Dialog as pat_lk
import datetime

class pat_lkWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()


        self.ui = pat_lk()
        self.ui.setupUi(self)
        self.setWindowTitle("Medical Clinic -- для пациента")

        self.db = sql.Sql()
        self.db.cursor.execute(
            "SELECT id from patients where user_id = " + str(user_info.current_userID))
        global patient_id
        patient_id = self.db.cursor.fetchone()

        self.setInitialValues()

        self.ui.change_nummer_button.clicked.connect(self.change_nummer_button_clicked)
        self.ui.exit_button.clicked.connect(self.exit_button_clicked)
        self.ui.add_queue_record_button.clicked.connect(self.add_queue_record_button_clicked)
        self.ui.physician_comboBox.currentIndexChanged.connect(self.physician_change)
        self.ui.date_comboBox.currentIndexChanged.connect(self.date_change)
        self.ui.reload_button.clicked.connect(self.queue_change)
        self.ui.specialization_comboBox.currentIndexChanged.connect(self.specialization_change)
        self.show()



    def specialization_change(self) :
        current_spec = str(self.ui.specialization_comboBox.currentText())
        self.db.cursor.execute("SELECT name from physicians where specialization_id = (Select id from specialization where name = '" + current_spec + "')")
        filler.fillComboBox(self.ui.physician_comboBox, self.db.cursor)

    def physician_change(self) :
        arr = []
        today = datetime.date.today() + datetime.timedelta(days=1)
        print(today + datetime.timedelta(days=1))
        for i in range(7) :
            arr.append(str(today + datetime.timedelta(days=i)))
        self.ui.date_comboBox.clear()
        self.ui.date_comboBox.addItem("")
        for i in arr:
            self.ui.date_comboBox.addItem(i)

    def date_change(self):
        global selected_date
        selected_date = str(self.ui.date_comboBox.currentText())
        if len(selected_date) != 0 :
            self.db.cursor.execute("SELECT id from physicians where name = '" + str(self.ui.physician_comboBox.currentText()) + "'")
            global selected_doctor
            selected_doctor = self.db.cursor.fetchone()
            self.db.cursor.execute("SELECT x FROM (SELECT x::time, CASE WHEN Q.time = x IS NULL "
                    "THEN false ELSE true END flag "
                    "FROM generate_series(date %s + time '08:00', date %s + time '18:00', interval  '30 min' ) t(x) "
                    "left JOIN (SELECT * FROM Queue WHERE physician_id = %s and time::date = %s "
                                   "and time::time between time '08:00' and '18:00') AS Q on time = x) as foo where flag = false",
                                   (selected_date, selected_date, selected_doctor[0], selected_date))
            filler.fillComboBox(self.ui.time_comboBox, self.db.cursor)

    def change_nummer_button_clicked(self):
        filler.changeNummer(self)

    def exit_button_clicked(self):
        filler.exitButton(self)

    def add_queue_record_button_clicked(self):
        print("Bibop")
        try:
            current_time = str(self.ui.time_comboBox.currentText())
            if len(selected_doctor) > 0 and len(current_time) > 0:
                self.db.cursor.execute("INSERT INTO queue(patient_id, physician_id, time) "
                                   "VALUES(%s, %s, timestamp %s)", (patient_id[0], selected_doctor, str(selected_date + " " + current_time)))
                self.db.cnxn.commit()
                self.ui.time_comboBox.clear()
                self.ui.date_comboBox.clear()
                self.ui.physician_comboBox.clear()
                self.queue_change()

        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgreSQL", error)


    def queue_change(self) :
        self.db.cursor.execute("SELECT  Q.time, P.name FROM queue Q "
                               "LEFT JOIN Physicians P on P.id = Q.physician_id "
                               "WHERE ((time >= current_timestamp) AND (patient_id = '" + str(patient_id[0]) + "'))")

        filler.fillTable(self.ui.Queue_tableWidget, self.db.cursor, 2)


    def setInitialValues(self):
        self.db.cursor.execute("SELECT name from patients where user_id=" + str(user_info.current_userID))
        pat_name = self.db.cursor.fetchone()
        self.ui.name_label.setText(pat_name[0])

        self.db.cursor.execute("SELECT passport from patients where user_id=" + str(user_info.current_userID))
        pas_name = self.db.cursor.fetchone()
        self.ui.passport_label.setText(str(pas_name[0]))

        self.db.cursor.execute("SELECT date_of_birth from patients where user_id=" + str(user_info.current_userID))
        date_of_birth = self.db.cursor.fetchone()
        self.ui.date_of_birth_label.setText(str(date_of_birth[0]))

        self.db.cursor.execute("SELECT phone from  authentication_data  WHERE id= '" + str(user_info.current_userID) + "'")
        phone = self.db.cursor.fetchone()
        self.ui.phone_number_box.setText(str(phone[0]))

        self.db.cursor.execute("SELECT insurance_policy from patients where user_id=" + str(user_info.current_userID))
        policy = self.db.cursor.fetchone()
        self.ui.insurance_policy_label.setText(str(policy[0]))

        self.db.cursor.execute("SELECT snils from patients where user_id=" + str(user_info.current_userID))
        snils = self.db.cursor.fetchone()
        self.ui.snils_label.setText(str(snils[0]))

        self.db.cursor.execute("SELECT name from specialization")
        filler.fillComboBox(self.ui.specialization_comboBox, self.db.cursor)

        self.queue_change()

        self.db.cursor.execute("SELECT Mr.date, Ph.name, Mr.diagnosis, S.name as Service FROM Medical_records Mr "
                               "LEFT JOIN Physicians Ph on Ph.id = Mr.physician_id "
                               "LEFT JOIN Services S on S.id = Mr.service_id "
                               "WHERE Mr.patient_id = %s ORDER BY date desc" %str(patient_id[0]))
        filler.fillTable(self.ui.med_record_tableWIdget, self.db.cursor, 4)

        self.db.cursor.execute("SELECT SUM(cost) FROM (SELECT S.cost FROM Medical_records Mr "
                               "LEFT JOIN Services S on S.id = Mr.service_id "
                               "WHERE Mr.patient_id = %s and Mr.date > (select cast(date_trunc('month', current_date) as date)) "
                               "ORDER BY date desc) as foo" %str(patient_id[0]))
        cost = self.db.cursor.fetchone()
        self.ui.cost_label.setText(str(cost[0]))