


from PyQt5 import QtCore, QtGui, QtWidgets
from bs4 import BeautifulSoup
import requests
import html5lib
from PyQt5.QtWidgets import QMessageBox


class Ui_Drugs(object):
    def setupUi(self, Drugs):
        Drugs.setObjectName("Drugs")
        Drugs.resize(572, 449)
        font = QtGui.QFont()
        font.setFamily("Nunito")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        Drugs.setFont(font)
        Drugs.setStyleSheet("background-color: rgb(44, 51, 54);\n"
"font: 75 12pt \"Nunito\";\n"
"color:white;\n"
"")
        self.centralwidget = QtWidgets.QWidget(Drugs)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(200, 50, 231, 51))
        self.label.setStyleSheet("color: cyan;\n"
"font: 81 24pt \"Nunito ExtraBold\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 200, 241, 31))
        self.label_2.setStyleSheet("font: 81 14pt \"Nunito ExtraBold\";")
        self.label_2.setObjectName("label_2")
        self.drugsearch = QtWidgets.QLineEdit(self.centralwidget)
        self.drugsearch.setGeometry(QtCore.QRect(290, 200, 221, 31))
        self.drugsearch.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"font: 87 12pt \"Nunito\";\n"
"color:black;")
        self.drugsearch.setObjectName("drugsearch")
        self.drugres = QtWidgets.QTextBrowser(self.centralwidget)
        self.drugres.setGeometry(QtCore.QRect(180, 330, 231, 41))
        self.drugres.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"font: 87 12pt \"Nunito\";\n"
"color:black;")
        self.drugres.setObjectName("drugres")
        self.drugo = QtWidgets.QPushButton(self.centralwidget)
        self.drugo.setGeometry(QtCore.QRect(220, 270, 151, 31))
        self.drugo.setStyleSheet("border-radius:10px;\n"
"background-color: #3CB7A1;\n"
"color: white;")
        self.drugo.setObjectName("drugo")
        Drugs.setCentralWidget(self.centralwidget)

        self.retranslateUi(Drugs)
        QtCore.QMetaObject.connectSlotsByName(Drugs)

        self.drugo.clicked.connect(self.getDrug)


    def getDrug(self):
        try:
            disease = self.drugsearch.text()
            url = f"https://www.medindia.net/drugs/medical-condition/{disease}.htm"
            html_content = requests.get(url)
            soup = BeautifulSoup(html_content.content,"html5lib")
            main_class = soup.find_all("article")[0]
            link = main_class.find_all("a")
            self.drugres.append(str(link[0].getText()))
        except:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Zero Input Error")
            msg.setInformativeText("An error occured")
            msg.setWindowTitle('Error')
            msg.exec_()


    def retranslateUi(self, Drugs):
        _translate = QtCore.QCoreApplication.translate
        Drugs.setWindowTitle(_translate("Drugs", "Drugs"))
        self.label.setText(_translate("Drugs", "Find Drugs"))
        self.label_2.setText(_translate("Drugs", "Enter disease to find drugs"))
        self.drugo.setText(_translate("Drugs", "Search"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Drugs = QtWidgets.QMainWindow()
    ui = Ui_Drugs()
    ui.setupUi(Drugs)
    Drugs.show()
    sys.exit(app.exec_())