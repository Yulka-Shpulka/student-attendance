from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog_5(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowIcon(QtGui.QIcon('graduation-hat.png'))
        Dialog.resize(553, 619)
        Dialog.setStyleSheet("background-color: rgb(248, 255, 230);")
        self.label = QtWidgets.QLabel(parent=Dialog)
        self.label.setGeometry(QtCore.QRect(40, 170, 491, 371))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../../Desktop/курсач/About_CSV.png"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 10, 491, 161))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../../Desktop/курсач/Example_CSV_1.png"))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton.setGeometry(QtCore.QRect(220, 560, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(" border-radius: 15px; \n"
"border: 2px solid #094065;\n"
"background-color: qlineargradient(spread:pad, x1:0.9899, y1:0.402, x2:0.930348, y2:0.932, stop:0 rgba(202, 214, 229, 255), stop:0.830846 rgba(254, 237, 206, 255));")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(Dialog.close)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "О CSV-файлах"))
        self.pushButton.setText(_translate("Dialog", "Назад"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog_5()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
