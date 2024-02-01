from PyQt6 import QtCore, QtGui, QtWidgets
from Teacher_logic_Window import Ui_Dialog_4
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QFileDialog, QMessageBox
import sqlite3


class Ui_Dialog_7(object):

    def setupUi(self, Dialog):
        Dialog.setWindowIcon(QtGui.QIcon('graduation-hat.png'))
        Dialog.setObjectName("Dialog")
        Dialog.resize(746, 484)
        self.label = QtWidgets.QLabel(parent=Dialog)
        self.label.setGeometry(QtCore.QRect(0, -10, 761, 491))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../../Downloads/photo_2023-11-25_14-09-45___2.jpg"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=Dialog)
        self.label_2.setGeometry(QtCore.QRect(240, 20, 361, 51))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=Dialog)
        self.label_3.setGeometry(QtCore.QRect(290, 90, 361, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(parent=Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(250, 140, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.label_4 = QtWidgets.QLabel(parent=Dialog)
        self.label_4.setGeometry(QtCore.QRect(290, 180, 361, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(250, 240, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(parent=Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(250, 340, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_5 = QtWidgets.QLabel(parent=Dialog)
        self.label_5.setGeometry(QtCore.QRect(290, 280, 361, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.pushButton = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton.setGeometry(QtCore.QRect(90, 410, 261, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("\n"
"    border-radius: 15px;   \n"
"    border: 2px solid #094065;\n"
"background-color: qlineargradient(spread:pad, x1:0.9899, y1:0.402, x2:0.930348, y2:0.932, stop:0 rgba(202, 214, 229, 255), stop:0.830846 rgba(254, 237, 206, 255));")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(420, 410, 261, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("\n"
"    border-radius: 15px;   \n"
"    border: 2px solid #094065;\n"
"background-color: qlineargradient(spread:pad, x1:0.9899, y1:0.402, x2:0.930348, y2:0.932, stop:0 rgba(202, 214, 229, 255), stop:0.830846 rgba(254, 237, 206, 255));")
        self.pushButton_2.setObjectName("pushButton_2")
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.pushButton.clicked.connect(self.login)
        self.pushButton_2.clicked.connect(self.register)

    def openWindowMain(self):
        self.window_4 = QtWidgets.QDialog()
        self.ui= Ui_Dialog_4()
        self.ui.setupUi(self.window_4)
        self.window_4.show()

    def login(self):
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Warning)
        # Check if the key matches
        key = self.lineEdit_3.text().strip()
        if not username or not password:  # Check if either username or password field is empty
            msg.setWindowTitle("Ошибка")
            msg.setText("Ошибка, не заполнены все поля!")
            msg.exec()
        else:
            if key == "123":
                conn = sqlite3.connect("my_database.db")
                cursor = conn.cursor()
                # Check if the user exists in the database
                cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
                result = cursor.fetchone()

                if result:
                    self.openWindowMain()
                else:
                    msg.setWindowTitle("Ошибка")
                    msg.setText("Ошибка, неверно введён логин или пароль!")
                    msg.exec()
            else:
                msg.setText("Введён неверный ключ!")
                msg.setWindowTitle("Ошибка")
                msg.exec()

    def register(self):
        conn = sqlite3.connect("my_database.db")
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)")

        username = self.lineEdit.text()
        password = self.lineEdit_2.text()

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Warning)
        if not username or not password:  # Check if either username or password field is empty
            msg.setWindowTitle("Ошибка")
            msg.setText("Ошибка, не заполнены все поля!")
            msg.exec()
        else:
            # Check if the key matches
            key = self.lineEdit_3.text().strip()
            if key == "123":
                cursor.execute("INSERT INTO users VALUES (?, ?)", (username, password))
                conn.commit()
                msg.setWindowTitle("Успех")
                msg.setText("Вы успешно были зарегистрированы!")
                msg.exec()
            else:
                msg.setWindowTitle("Ошибка")
                msg.setText("Введён неверный ключ!")
                msg.exec()


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Вход (для преподавателя)"))
        self.label_2.setText(_translate("Dialog", "Вход  в систему"))
        self.label_3.setText(_translate("Dialog", "Введите логин:"))
        self.label_4.setText(_translate("Dialog", "Введите пароль:"))
        self.label_5.setText(_translate("Dialog", "Введите ключ:"))
        self.pushButton.setText(_translate("Dialog", "Войти"))
        self.pushButton_2.setText(_translate("Dialog", "Зарегистрироваться"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog_7()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
