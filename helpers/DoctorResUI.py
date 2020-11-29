


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CDres(object):
    def setupUi(self, CDres):
        CDres.setObjectName("CDres")
        CDres.resize(704, 520)
        CDres.setStyleSheet("background-color: #2C3336;\n"
"font: 63 12pt \"Nunito\";")
        self.centralwidget = QtWidgets.QWidget(CDres)
        self.centralwidget.setObjectName("centralwidget")
        self.CDheading = QtWidgets.QLabel(self.centralwidget)
        self.CDheading.setGeometry(QtCore.QRect(240, 60, 241, 41))
        self.CDheading.setStyleSheet("color: cyan;\n"
"font: 81 24pt \"Nunito ExtraBold\";\n"
"")
        self.CDheading.setObjectName("CDheading")
        self.CDresult = QtWidgets.QTextBrowser(self.centralwidget)
        self.CDresult.setGeometry(QtCore.QRect(30, 130, 661, 311))
        self.CDresult.setStyleSheet("background-color: white;\n"
"border-radius: 10px;")
        self.CDresult.setObjectName("CDresult")
        self.CDgo = QtWidgets.QPushButton(self.centralwidget)
        self.CDgo.setGeometry(QtCore.QRect(300, 460, 121, 31))
        self.CDgo.setStyleSheet("border-radius:10px;\n"
"background-color: #3CB7A1;\n"
"color: white;")
        self.CDgo.setObjectName("CDgo")
        CDres.setCentralWidget(self.centralwidget)

        self.retranslateUi(CDres)
        QtCore.QMetaObject.connectSlotsByName(CDres)

    def retranslateUi(self, CDres):
        _translate = QtCore.QCoreApplication.translate
        CDres.setWindowTitle(_translate("CDres", "Doctors result"))
        self.CDheading.setText(_translate("CDres", "Doctor\'s List"))
        self.CDgo.setText(_translate("CDres", "Save as text file"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CDres = QtWidgets.QMainWindow()
    ui = Ui_CDres()
    ui.setupUi(CDres)
    CDres.show()
    sys.exit(app.exec_())
