from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from bs4 import BeautifulSoup
import requests
from helpers.WikipediaUI import Ui_Wikipedia
from helpers.GoogleUI import Ui_Google
from helpers.dbres import Ui_Saved

# class start
class Ui_MyDoctorApp(object):
    def savedUi(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Saved()
        self.ui.setupUi(self.window)
        self.window.show()
    def WikipediaSearch(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Wikipedia()
        self.ui.setupUi(self.window)
        self.window.show()
    def GoogleSearch(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Google()
        self.ui.setupUi(self.window)
        self.window.show()    
    def setupUi(self, MyDoctorApp):
        MyDoctorApp.setObjectName("MyDoctor")
        MyDoctorApp.resize(846, 600)
        MyDoctorApp.setStyleSheet("background-color: #2C3336;\n"
"font: 63 12pt \"Nunito\";")
        self.centralwidget = QtWidgets.QWidget(MyDoctorApp)
        self.centralwidget.setObjectName("centralwidget")
        self.query = QtWidgets.QLineEdit(self.centralwidget)
        self.query.setGeometry(QtCore.QRect(280, 170, 291, 31))
        font = QtGui.QFont()
        font.setFamily("Nunito")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.query.setFont(font)
        self.query.setStyleSheet("border-radius:10px;\n"
"background-color: white;")
        self.query.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.query.setClearButtonEnabled(False)
        self.query.setObjectName("query")
        self.go = QtWidgets.QPushButton(self.centralwidget)
        self.go.setGeometry(QtCore.QRect(590, 170, 81, 31))
        self.go.setStyleSheet("border-radius:10px;\n"
"background-color: #3CB7A1;\n"
"color: white;")
        self.go.setObjectName("go")
        self.result = QtWidgets.QTextBrowser(self.centralwidget)
        self.result.setGeometry(QtCore.QRect(210, 230, 511, 201))
        self.result.setStyleSheet("background-color: white;\n"
"border-radius: 10px;")
        self.result.setObjectName("result")
        self.heading = QtWidgets.QLabel(self.centralwidget)
        self.heading.setGeometry(QtCore.QRect(320, 60, 241, 41))
        self.heading.setStyleSheet("color: cyan;\n"
"font: 81 24pt \"Nunito ExtraBold\";\n"
"")
        self.heading.setObjectName("heading")
        self.wikipedia = QtWidgets.QPushButton(self.centralwidget)
        self.wikipedia.setGeometry(QtCore.QRect(250, 460, 121, 31))
        self.wikipedia.setStyleSheet("border-radius:10px;\n"
"background-color: #3CB7A1;\n"
"color: white;")
        self.wikipedia.setObjectName("wikipedia")
        self.google = QtWidgets.QPushButton(self.centralwidget)
        self.google.setGeometry(QtCore.QRect(410, 460, 121, 31))
        self.google.setStyleSheet("border-radius:10px;\n"
"background-color: #3CB7A1;\n"
"color: white;")
        self.google.setObjectName("google")
        self.left = QtWidgets.QFrame(self.centralwidget)
        self.left.setGeometry(QtCore.QRect(0, 0, 141, 571))
        self.left.setStyleSheet("background-color: rgb(66, 76, 81);\n"
"")
        self.left.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.left.setFrameShadow(QtWidgets.QFrame.Raised)
        self.left.setObjectName("left")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.left)
        self.verticalLayout.setObjectName("verticalLayout")
        self.cdoctor = QtWidgets.QPushButton(self.left)
        self.cdoctor.setStyleSheet("color: cyan;\n"
"font: 81 11pt \"Nunito ExtraBold\";\n"
"")
        self.cdoctor.setFlat(True)
        self.cdoctor.setObjectName("cdoctor")
        self.verticalLayout.addWidget(self.cdoctor)
        self.covid = QtWidgets.QPushButton(self.left)
        self.covid.setStyleSheet("color: cyan;\n"
"font: 81 11pt \"Nunito ExtraBold\";")
        self.covid.setFlat(True)
        self.covid.setObjectName("covid")
        self.verticalLayout.addWidget(self.covid)
        self.drugs_2 = QtWidgets.QPushButton(self.left)
        self.drugs_2.setStyleSheet("color: cyan;\n"
"font: 81 11pt \"Nunito ExtraBold\";")
        self.drugs_2.setFlat(True)
        self.drugs_2.setObjectName("drugs_2")
        self.verticalLayout.addWidget(self.drugs_2)
        self.credits = QtWidgets.QPushButton(self.left)
        self.credits.setStyleSheet("color: cyan;\n"
"font: 81 11pt \"Nunito ExtraBold\";")
        self.credits.setFlat(True)
        self.credits.setObjectName("credits")
        self.verticalLayout.addWidget(self.credits)
        self.databaseB = QtWidgets.QPushButton(self.centralwidget)
        self.databaseB.setGeometry(QtCore.QRect(560, 460, 121, 31))
        self.databaseB.setStyleSheet("border-radius:10px;\n"
"background-color: #3CB7A1;\n"
"color: white;")
        self.databaseB.setObjectName("databaseB")
        MyDoctorApp.setCentralWidget(self.centralwidget)

        self.retranslateUi(MyDoctorApp)
        QtCore.QMetaObject.connectSlotsByName(MyDoctorApp)
#         self.go.clicked.connect(self.diseaseSearchX)
#         self.cdoctor.clicked.connect(self.consultDoctor)
#         self.covid.clicked.connect(self.covidUI)
#         self.drugs_2.clicked.connect(self.drugUI)
        self.wikipedia.clicked.connect(self.WikipediaSearch)
        self.google.clicked.connect(self.GoogleSearch)
        self.databaseB.clicked.connect(self.savedUi)  
    def retranslateUi(self, MyDoctorApp):
        _translate = QtCore.QCoreApplication.translate
        MyDoctorApp.setWindowTitle(_translate("MyDoctorApp", "MainWindow"))
        self.query.setPlaceholderText(_translate("MyDoctorApp", "                      Search here"))
        self.go.setText(_translate("MyDoctorApp", "GO"))
        self.heading.setText(_translate("MyDoctorApp", "     MyDoctorApp"))
        self.wikipedia.setText(_translate("MyDoctorApp", "Wikipedia"))
        self.google.setText(_translate("MyDoctorApp", "Google"))
        self.cdoctor.setText(_translate("MyDoctorApp", "Consult Doctor"))
        self.covid.setText(_translate("MyDoctorApp", "CovidAnalyser"))
        self.drugs_2.setText(_translate("MyDoctorApp", "Drugs"))
        self.credits.setText(_translate("MyDoctorApp", "Credits"))
        self.databaseB.setText(_translate("MyDoctorApp", "Saved"))    


# main function
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MyDoctorApp = QtWidgets.QMainWindow()
    ui = Ui_MyDoctorApp()
    ui.setupUi(MyDoctorApp)
    MyDoctorApp.show()
    sys.exit(app.exec_())
