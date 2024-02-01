from PyQt6 import QtCore, QtGui, QtWidgets
from About_me import Ui_MeDialog_About_me
from about_program import Ui_Dialog
from PyQt6.QtCore import QTimer
from Entrance import Ui_Dialog_Entrance


class Ui_MainWindow(object):
    def openWindowAbout_me(self):
        self.window_1 = QtWidgets.QMainWindow()
        self.ui = Ui_MeDialog_About_me()
        self.ui.setupUi(self.window_1)
        self.window_1.show()

    def openWindowAbout_program(self):
        self.window_2 = QtWidgets.QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.window_2)
        self.window_2.show()

    def openWindowEntrance(self):
        self.window_3 = QtWidgets.QMainWindow()
        self.ui = Ui_Dialog_Entrance()
        self.ui.setupUi(self.window_3)
        self.window_3.show()

    def setupUi(self, MainWindow):
        # Создаем таймер
        self.timer = QTimer()
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(MainWindow.close)

        self.timer.start(60000)  # Время указывается в миллисекундах (60 секунд = 60000 миллисекунд)
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(902, 632)
        MainWindow.setStyleSheet("background-color: rgb(187, 203, 229);\n"
"\n"
"")
        MainWindow.setWindowIcon(QtGui.QIcon('graduation-hat.png'))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_8 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(530, 270, 361, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(130, 70, 771, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(190, 0, 641, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_7 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(280, 220, 401, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.pushButton_5 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(200, 530, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("\n"
"    border-radius: 15px;   \n"
"    border: 2px solid #094065;\n"
"background-color: qlineargradient(spread:pad, x1:0.9899, y1:0.402, x2:0.930348, y2:0.932, stop:0 rgba(202, 214, 229, 255), stop:0.830846 rgba(254, 237, 206, 255));")
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_10 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(400, 470, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_9 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(530, 340, 361, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_11 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(30, 270, 341, 211))
        self.label_11.setText("")
        self.label_11.setPixmap(QtGui.QPixmap("../../Desktop/курсач/window_1.webp"))
        self.label_11.setObjectName("label_11")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(370, 110, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(110, 160, 771, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(210, 40, 641, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(730, 530, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("\n"
"    border-radius: 15px;   \n"
"    border: 2px solid #094065;\n"
"background-color: qlineargradient(spread:pad, x1:0.9899, y1:0.402, x2:0.930348, y2:0.932, stop:0 rgba(202, 214, 229, 255), stop:0.830846 rgba(254, 237, 206, 255));")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(560, 530, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("\n"
"    border-radius: 15px;   \n"
"    border: 2px solid #094065;\n"
"background-color: qlineargradient(spread:pad, x1:0.9899, y1:0.402, x2:0.930348, y2:0.932, stop:0 rgba(202, 214, 229, 255), stop:0.830846 rgba(254, 237, 206, 255));")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(270, 190, 491, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 530, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("\n"
"    border-radius: 15px;   \n"
"    border: 2px solid #094065;\n"
"background-color: qlineargradient(spread:pad, x1:0.9899, y1:0.402, x2:0.930348, y2:0.932, stop:0 rgba(202, 214, 229, 255), stop:0.830846 rgba(254, 237, 206, 255));")
        self.pushButton_3.setObjectName("pushButton_3")


        self.pushButton_3.clicked.connect(self.openWindowAbout_me)
        self.pushButton_5.clicked.connect(self.openWindowAbout_program)
        self.pushButton_4.clicked.connect(self.openWindowEntrance)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 902, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Заставка"))
        self.label_8.setText(_translate("MainWindow", "Выполнила: Студент группы 10701122\n"
"Куликович Юлия Вячеславовна"))
        self.label_2.setText(_translate("MainWindow", "Кафедра программного обеспечения и информационных технологий"))
        self.label.setText(_translate("MainWindow", "Белорусский Национальный Технический Университет"))
        self.label_7.setText(_translate("MainWindow", "Контроль успеваемости студентов"))
        self.pushButton_5.setText(_translate("MainWindow", "О программе"))
        self.label_10.setText(_translate("MainWindow", "Минск 2023"))
        self.label_9.setText(_translate("MainWindow", "Преподаватель: к.ф.-м.н., доц.\n"
"Сидорик Валерий Владимирович"))
        self.label_4.setText(_translate("MainWindow", "Курсовая работа"))
        self.label_5.setText(_translate("MainWindow", "Кафедра программного обеспечения и информационных технологий"))
        self.label_3.setText(_translate("MainWindow", "Факультет информационных систем и робототехники"))
        self.pushButton_4.setText(_translate("MainWindow", "Далее"))
        self.pushButton_2.setText(_translate("MainWindow", "Выход"))

        self.pushButton_2.clicked.connect(MainWindow.close)

        self.pushButton_3.setText(_translate("Dialog", "Об авторе"))
        self.label_6.setText(_translate("MainWindow", "по дисциплине Языки программирования"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
