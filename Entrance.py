from PyQt6 import QtCore, QtGui, QtWidgets
from Enter_teacher import Ui_Dialog_7
from Enter_student import Ui_Dialog_8


class Ui_Dialog_Entrance(object):
    def setupUi(self, Dialog):
        Dialog.setWindowIcon(QtGui.QIcon('graduation-hat.png'))
        Dialog.setObjectName("Dialog")
        Dialog.resize(729, 471)
        Dialog.setStyleSheet("background-color: rgb(187, 203, 229);\n"
"\n"
"")
        self.label = QtWidgets.QLabel(parent=Dialog)
        self.label.setGeometry(QtCore.QRect(280, 10, 231, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 110, 331, 301))
        self.label_2.setStyleSheet(".scale {\n"
"    transition: 1s; /* Время эффекта */\n"
"   }\n"
"   .scale:hover {\n"
"    transform: scale(1.2); /* Увеличиваем масштаб */\n"
"   }")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../../Desktop/курсач/man-teacher_1.png"))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=Dialog)
        self.label_3.setGeometry(QtCore.QRect(450, 130, 231, 271))
        self.label_3.setStyleSheet(".scale {\n"
"    transition: 1s; /* Время эффекта */\n"
"   }\n"
".scale:hover {\n"
"   transform: scale(1.2); /* Увеличиваем масштаб */\n"
"   }")
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("../../Desktop/курсач/student (2).png"))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=Dialog)
        self.label_4.setGeometry(QtCore.QRect(50, 70, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=Dialog)
        self.label_5.setGeometry(QtCore.QRect(510, 70, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.pushButton_4 = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(290, 420, 151, 41))
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

        self.label_2.enterEvent = self.start_animation
        self.label_3.enterEvent = self.start_animation
        self.pushButton_4.clicked.connect(Dialog.close)
        self.label_2.mousePressEvent = self.on_teacher_label_clicked
        self.label_3.mousePressEvent = self.on_student_label_clicked

    def start_animation(self, event):
        self.label_2.setToolTip("<p>Нажмите для авторизации</p>")
        self.label_3.setToolTip("<p>Нажмите для авторизации</p>")

    def on_teacher_label_clicked(self,event):
        self.window_7 = QtWidgets.QDialog()
        self.ui = Ui_Dialog_7()
        self.ui.setupUi(self.window_7)
        self.window_7.show()

    def on_student_label_clicked(self,event):
        self.window_8 = QtWidgets.QDialog()
        self.ui = Ui_Dialog_8()
        self.ui.setupUi(self.window_8)
        self.window_8.show()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Вход"))
        self.label.setText(_translate("Dialog", "Вход в систему"))
        self.label_4.setText(_translate("Dialog", "Я-преподаватель"))
        self.label_5.setText(_translate("Dialog", "Я-студент"))
        self.pushButton_4.setText(_translate("Dialog", "Назад"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog_Entrance()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
