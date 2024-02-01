from PyQt6 import QtCore, QtGui, QtWidgets, QtSql
from PyQt6.QtSql import QSqlDatabase, QSqlQuery
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QFileDialog, QMessageBox
import sqlite3
import csv
from About_CSV import Ui_Dialog_5
from PyQt6.QtCore import Qt
from add_student_dialog import Ui_Dialog_6
import random


class Ui_Dialog_4(object):

    def openWindow_add_student(self):
        self.window_6 = QtWidgets.QDialog()
        self.ui = Ui_Dialog_6()
        self.ui.setupUi(self.window_6)
        self.window_6.show()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1005, 697)
        font = QtGui.QFont()
        font.setPointSize(15)
        Dialog.setFont(font)
        ui = Ui_Dialog_4()
        self.label = QtWidgets.QLabel(parent=Dialog)
        Dialog.setWindowIcon(QtGui.QIcon('graduation-hat.png'))
        self.label.setGeometry(QtCore.QRect(0, 10, 1001, 691))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../../Downloads/1678348032_bogatyr-club-p-tuchi-estetika-foni-pinterest-57.jpg"))
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(parent=Dialog)
        self.line.setGeometry(QtCore.QRect(620, 50, 20, 511))
        self.line.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(parent=Dialog)
        self.line_2.setGeometry(QtCore.QRect(20, 30, 941, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(parent=Dialog)
        self.line_3.setGeometry(QtCore.QRect(20, 580, 941, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_3.setObjectName("line_3")
        self.pushButton_4 = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(690, 520, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("\n"
"    border-radius: 15px;   \n"
"    border: 2px solid #094065;\n"
"background-color: qlineargradient(spread:pad, x1:0.9899, y1:0.402, x2:0.930348, y2:0.932, stop:0 rgba(202, 214, 229, 255), stop:0.830846 rgba(254, 237, 206, 255));")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(690, 450, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("\n"
"    border-radius: 15px;   \n"
"    border: 2px solid #094065;\n"
"background-color: qlineargradient(spread:pad, x1:0.9899, y1:0.402, x2:0.930348, y2:0.932, stop:0 rgba(202, 214, 229, 255), stop:0.830846 rgba(254, 237, 206, 255));")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton_6.setGeometry(QtCore.QRect(690, 390, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("\n"
"    border-radius: 15px;   \n"
"    border: 2px solid #094065;\n"
"background-color: qlineargradient(spread:pad, x1:0.9899, y1:0.402, x2:0.930348, y2:0.932, stop:0 rgba(202, 214, 229, 255), stop:0.830846 rgba(254, 237, 206, 255));")
        self.pushButton_6.setObjectName("pushButton_6")
        self.label_2 = QtWidgets.QLabel(parent=Dialog)
        self.label_2.setGeometry(QtCore.QRect(650, 60, 311, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=Dialog)
        self.label_3.setGeometry(QtCore.QRect(650, 110, 311, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=Dialog)
        self.label_4.setGeometry(QtCore.QRect(650, 150, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=Dialog)
        self.label_5.setGeometry(QtCore.QRect(770, 150, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.pushButton_7 = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton_7.setGeometry(QtCore.QRect(690, 250, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("\n"
"    border-radius: 15px;   \n"
"    border: 2px solid #094065;\n"
"background-color: qlineargradient(spread:pad, x1:0.9899, y1:0.402, x2:0.930348, y2:0.932, stop:0 rgba(202, 214, 229, 255), stop:0.830846 rgba(254, 237, 206, 255));")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton_8.setGeometry(QtCore.QRect(690, 320, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("\n"
"    border-radius: 15px;   \n"
"    border: 2px solid #094065;\n"
"background-color: qlineargradient(spread:pad, x1:0.9899, y1:0.402, x2:0.930348, y2:0.932, stop:0 rgba(202, 214, 229, 255), stop:0.830846 rgba(254, 237, 206, 255));")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton_9.setGeometry(QtCore.QRect(30, 630, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet("\n"
"    border-radius: 15px;   \n"
"    border: 2px solid #094065;\n"
"background-color: qlineargradient(spread:pad, x1:0.9899, y1:0.402, x2:0.930348, y2:0.932, stop:0 rgba(202, 214, 229, 255), stop:0.830846 rgba(254, 237, 206, 255));")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton_10.setGeometry(QtCore.QRect(240, 630, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setStyleSheet("\n"
"    border-radius: 15px;   \n"
"    border: 2px solid #094065;\n"
"background-color: qlineargradient(spread:pad, x1:0.9899, y1:0.402, x2:0.930348, y2:0.932, stop:0 rgba(202, 214, 229, 255), stop:0.830846 rgba(254, 237, 206, 255));")
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton_11.setGeometry(QtCore.QRect(460, 630, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setStyleSheet("\n"
"    border-radius: 15px;   \n"
"    border: 2px solid #094065;\n"
"background-color: qlineargradient(spread:pad, x1:0.9899, y1:0.402, x2:0.930348, y2:0.932, stop:0 rgba(202, 214, 229, 255), stop:0.830846 rgba(254, 237, 206, 255));")
        self.pushButton_11.setObjectName("pushButton_11")
        self.line_4 = QtWidgets.QFrame(parent=Dialog)
        self.line_4.setGeometry(QtCore.QRect(660, 190, 301, 20))
        self.line_4.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_4.setObjectName("line_4")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.students = QtWidgets.QTableWidget(parent=Dialog)
        self.students.setGeometry(QtCore.QRect(30, 60, 560, 520))
        self.students.setObjectName("tableWidget")
        self.students.setColumnCount(7)
        self.students.setRowCount(0)
        self.students.raise_()
        self.students.setHorizontalHeaderLabels(['ФИО'] + [str(i) for i in range(1, 8)])


        names = [
            'Киселев Алексей Иванович',
            'Игнатьев Александр Иванович',
            'Сорокина Елизавета Степановна',
            'Калинина Мария Тимуровна',
            'Филимонов Фёдор Николаевич',
            'Родионов Антон Алексеевич',
            'Сергеева Юлия Тимуровна',
            'Лукьянов Тимофей Степанович',
            'Максимов Дмитрий Романович',
            'Кулешова Юлия Елисеевна',
            'Захарова Вероника Дмитриевна',
            'Мельникова Майя Олеговна',
            'Филимонов Артём Владиславович',
            'Фомин Даниил Никитич',
            'Соболева Полина Никитична',
            'Иванова Екатерина Дмитриевна',
            'Макарова Дарья Давидовна',
            'Акимова София Михайловна',
            'Степанова Таисия Кирилловна',
            'Киселева Камила Фёдоровна',
            'Чернов Марк Фёдорович',
            'Колесников Даниил Ярославович',
            'Егорова Ульяна Вадимовна',
            'Горбунов Марк Даниилович',
            'Журавлева Варвара Макаровна',
            'Мартынова Анна Юрьевна',
            'Шмелева Кристина Макаровна',
            'Миронова Виктория Ивановна',
            'Прокофьев Руслан Германович',
            'Маркин Константин Билалович'
        ]

        conn = sqlite3.connect("student.db")
        cur = conn.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS students(
                                 name TEXT,
                                 tag TEXT,
                                 base30 BLOB);
                          """)

        # Вставить данные в таблицу, только если их еще нет
        for name in names:
            cur.execute("""
                      INSERT OR IGNORE INTO students (name, tag) 
                      SELECT ?, ?
                      WHERE NOT EXISTS (
                          SELECT name FROM students WHERE name = ?
                      );
                  """, (name, '', name))

        conn.commit()
        cur.close()
        conn.close()

        # Получить данные из таблицы
        conn = sqlite3.connect("student.db")
        cur = conn.cursor()
        cur.execute("SELECT name, tag FROM students")
        data = cur.fetchall()
        cur.close()
        conn.close()


        # Добавить данные в таблицу
        for row_number, row_data in enumerate(data):
            if any(column_data for column_data in row_data):
                self.students.insertRow(row_number)
                for column_number, column_data in enumerate(row_data):
                    cell_widget = QtWidgets.QTableWidgetItem(str(column_data))
                    self.students.setItem(row_number, column_number, cell_widget)

        self.students.resizeColumnsToContents()
        self.students.setHorizontalHeaderLabels(['ФИО', '1', '2','3', '4','5', '6'])
        self.students.resizeColumnsToContents()

        self.pushButton_10.clicked.connect(Dialog.close)
        self.pushButton_6.clicked.connect(self.load_data_from_csv)
        self.pushButton_11.clicked.connect(self.show_csv_info)
        self.pushButton_9.clicked.connect(self.close_all_windows)
        self.pushButton_5.clicked.connect(self.sort_table_by_alphabet)
        self.pushButton_4.clicked.connect(self.sort_table_by_rating)
        self.pushButton_7.clicked.connect(self.add_student_to_database)
        self.pushButton_8.clicked.connect(self.delete_student)

    def add_student_to_database(self):
        name, ok = QtWidgets.QInputDialog.getText(None, "Добавить студента", "Введите ФИО студента:")
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Warning)
        if ok and name:
            if len(name.split()) == 3:
                # Add the student to the table
                row_num = self.students.rowCount()
                self.students.insertRow(row_num)
                # Создание нового элемента таблиц с помощью введенного ФИО.
                name_item = QtWidgets.QTableWidgetItem(name)
                self.students.setItem(row_num, 0, name_item)
            # Добавление студента в базу данных
                try:
                    connection = sqlite3.connect('student.db')
                    cursor = connection.cursor()
                    cursor.execute("INSERT INTO students (name) VALUES (?)", (name,))
                    connection.commit()
                    connection.close()
                except Exception as e:
                    msg.setText("Ошибка при попытке подключения к базе данных")
                    msg.setWindowTitle("Ошибка")
                    msg.exec()
            else:
                msg.setText("Будьте внимательны! Введите ФИО ученика в формате 'Фамилия Имя Отчество'.")
                msg.setWindowTitle("Ошибка")
                msg.exec()
        else:
            msg.setWindowTitle("Ошибка")
            msg.setText("Будьте внимательны! Заполните поле")
            msg.exec()

    def delete_student(self):
        name, ok = QtWidgets.QInputDialog.getText(None, "Удалить студента", "Введите ФИО студента:")
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Warning)
        if name and ok:
            if len(name.split()) == 3:
                row = None
                # Search for the row containing the entered name
                for i in range(self.students.rowCount()):
                    item = self.students.item(i, 0)
                    if item.text() == name:
                        row = i
                        break
                if row is not None:
                    self.students.removeRow(row)  # Remove the row if found
                    # Добавление студента в базу данных
                    try:
                        sqlite_connection = sqlite3.connect('student.db')
                        cursor = sqlite_connection.cursor()
                        print("Подключен к SQLite")

                        cursor.execute("DELETE FROM students WHERE name=?", (name,))
                        sqlite_connection.commit()
                        print("Запись успешно удалена")
                        cursor.close()
                    except sqlite3.Error as error:
                        print("Ошибка при работе с SQLite", error)
                else:
                    msg.setWindowTitle("Ошибка")
                    msg.setText("Ошибка.Студент не найден!")
                    msg.exec()
            else:
                msg.setWindowTitle("Ошибка")
                msg.setText("Будьте внимательны! Введите ФИО ученика в формате 'Фамилия Имя Отчество'.")
                msg.exec()
        else:
            msg.setWindowTitle("Ошибка")
            msg.setText("Будьте внимательны! Заполните поле")
            msg.exec()

    def close_all_windows(self):
        app = QtWidgets.QApplication.instance()
        for widget in app.topLevelWidgets():
            if widget.isVisible():
                widget.close()

    def show_csv_info(self):
        self.window_3 = QtWidgets.QMainWindow()
        self.ui = Ui_Dialog_5()
        self.ui.setupUi(self.window_3)
        self.window_3.show()
    def load_data_from_csv(self):
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Выберите CSV-файл", "", "CSV Files (*.csv)")
        if file_path:
            with open(file_path, 'r', newline='', encoding='utf-8') as csvfile:
                csv_reader = csv.reader(csvfile, delimiter=';')
                headers = next(csv_reader)  # Get the column headers from the first row
                self.students.setColumnCount(len(headers))
                self.students.setHorizontalHeaderLabels(headers)
                self.students.setRowCount(0)  # Clear the existing data in the table
                for row_data in csv_reader:
                    row_num = self.students.rowCount()
                    self.students.insertRow(row_num)
                    total_score = 0
                    for col_num, col_data in enumerate(row_data):
                        item = QtWidgets.QTableWidgetItem(col_data)
                        if col_num > 0:  # Игнорируем первый столбец (ФИО) при вычислении среднего балла
                            total_score += int(col_data)  # Предполагая, что баллы представлены целыми числами
                        self.students.setItem(row_num, col_num, item)
                    # После вычисления среднего балла
                    average_score = round(total_score / (len(row_data) - 1),2)  # Округляем до двух знаков после запятой
                    item = QtWidgets.QTableWidgetItem(str(average_score))
                    item.setData(QtCore.Qt.ItemDataRole.DisplayRole,f'{average_score:.2f}')
                    self.students.setItem(row_num, len(row_data) - 1,item)  # Добавляем ячейку среднего балла в новый столбец
                    self.students.setHorizontalHeaderItem(len(headers) - 1,QtWidgets.QTableWidgetItem("Средний балл"))
            self.students.resizeColumnsToContents()


    def sort_table_by_alphabet(self, column):
        self.students.sortItems(column)

    def sort_table_by_rating(self, column):
        self.students.sortItems(column + 6, Qt.SortOrder.DescendingOrder)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Окно преподавателя"))
        self.pushButton_4.setText(_translate("Dialog", "Сортировать по рейтингу"))
        self.pushButton_5.setText(_translate("Dialog", "Сортировать по алфавиту"))
        self.pushButton_6.setText(_translate("Dialog", "Загрузить данные из csv-файла"))
        self.label_2.setText(_translate("Dialog", "Великая цель образования-"))
        self.label_3.setText(_translate("Dialog", "это не знания, а действия"))
        self.label_5.setText(_translate("Dialog", "Герберт Спенсер"))
        self.pushButton_7.setText(_translate("Dialog", "Добавить студента"))
        self.pushButton_8.setText(_translate("Dialog", "Удалить студента"))
        self.pushButton_9.setText(_translate("Dialog", "Выход"))
        self.pushButton_10.setText(_translate("Dialog", "Назад"))
        self.pushButton_11.setText(_translate("Dialog", "О csv-файлах"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog_4()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
