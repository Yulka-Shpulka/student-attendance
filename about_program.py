from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setStyleSheet("background-color: rgb(187, 203, 229);")
        self.label = QtWidgets.QLabel(parent=Dialog)
        self.label.setGeometry(QtCore.QRect(180, 20, 411, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=Dialog)
        self.label_2.setGeometry(QtCore.QRect(390, 60, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(parent=Dialog)
        self.label_4.setGeometry(QtCore.QRect(320, 100, 361, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(parent=Dialog)
        self.label_6.setGeometry(QtCore.QRect(320, 150, 361, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(parent=Dialog)
        self.label_7.setGeometry(QtCore.QRect(320, 200, 361, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(parent=Dialog)
        self.label_8.setGeometry(QtCore.QRect(320, 260, 361, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(parent=Dialog)
        self.label_9.setGeometry(QtCore.QRect(320, 290, 361, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(parent=Dialog)
        self.label_10.setGeometry(QtCore.QRect(320, 340, 361, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(parent=Dialog)
        self.label_11.setGeometry(QtCore.QRect(320, 400, 361, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_3 = QtWidgets.QLabel(parent=Dialog)
        self.label_3.setGeometry(QtCore.QRect(40, 80, 241, 321))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("../../Desktop/курсач/about_program_1.jpg"))
        self.label_3.setObjectName("label_3")
        self.pushButton_4 = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(420, 460, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("\n"
"    border-radius: 15px;   \n"
"    border: 2px solid #094065;\n"
"background-color: qlineargradient(spread:pad, x1:0.9899, y1:0.402, x2:0.930348, y2:0.932, stop:0 rgba(202, 214, 229, 255), stop:0.830846 rgba(254, 237, 206, 255));")
        self.pushButton_4.setObjectName("pushButton_4")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "О программе"))
        self.label.setText(_translate("Dialog", "Контроль успеваемости студентов"))
        self.label_2.setText(_translate("Dialog", "Программа позволяет:"))
        self.label_4.setText(_translate("Dialog", "1. Посмотреть таблицу со списком студентов\n"
" и количеством заданий по дисциплине. "))
        self.label_6.setText(_translate("Dialog", "2. Студенты могут  посмотреть текущее\n"
"состояние дел. "))
        self.label_7.setText(_translate("Dialog", "3. Преподаватель, после ввода пароля, \n"
"может устанавливать факт сдачи задания."))
        self.label_8.setText(_translate("Dialog", "4. Cортировка списка студентов по алфавиту."))
        self.label_9.setText(_translate("Dialog", "5. Возможность проставления \n"
"экзаменационной оценки студентам."))
        self.label_10.setText(_translate("Dialog", "6. Преподаватель, после ввода пароля, может \n"
"устанавливать факт сдачи задания."))
        self.label_11.setText(_translate("Dialog", "7. Ввод дисциплины и количества\n"
" контрольных точек."))
        self.pushButton_4.setText(_translate("Dialog", "Назад"))
        self.pushButton_4.clicked.connect(Dialog.close)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
