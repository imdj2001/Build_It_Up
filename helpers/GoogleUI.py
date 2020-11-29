


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from bs4 import BeautifulSoup
import requests
import html5lib
# UI of google
class Ui_Google(object):
    def setupUi(self, Google):
        Google.setObjectName("Google")
        Google.resize(1074, 520)
        Google.setStyleSheet("background-color: #2C3336;\n"
"font: 63 12pt \"Nunito\";")
        self.centralwidget = QtWidgets.QWidget(Google)
        self.centralwidget.setObjectName("centralwidget")
        self.google = QtWidgets.QLabel(self.centralwidget)
        self.google.setGeometry(QtCore.QRect(290, 50, 271, 41))
        self.google.setStyleSheet("color: cyan;\n"
"font: 81 24pt \"Nunito ExtraBold\";\n"
"")
        self.google.setObjectName("google")
        self.Gquery = QtWidgets.QLineEdit(self.centralwidget)
        self.Gquery.setGeometry(QtCore.QRect(280, 140, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Nunito")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.Gquery.setFont(font)
        self.Gquery.setStyleSheet("border-radius:10px;\n"
"background-color: white;")
        self.Gquery.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.Gquery.setClearButtonEnabled(False)
        self.Gquery.setObjectName("Gquery")
        self.Ggo = QtWidgets.QPushButton(self.centralwidget)
        self.Ggo.setGeometry(QtCore.QRect(580, 140, 81, 31))
        self.Ggo.setStyleSheet("border-radius:10px;\n"
"background-color: #3CB7A1;\n"
"color: white;")
        self.Ggo.setObjectName("Ggo")
        self.Gres = QtWidgets.QTextBrowser(self.centralwidget)
        self.Gres.setGeometry(QtCore.QRect(80, 221, 721, 271))
        self.Gres.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 87 12pt \"Nunito Black\";\n"
"border-radius: 10px;")
        self.Gres.setObjectName("Gres")
      
        Google.setCentralWidget(self.centralwidget)

        self.retranslateUi(Google)
        QtCore.QMetaObject.connectSlotsByName(Google)

        self.Ggo.clicked.connect(self.googleProject)

#google project
    def googleProject(self):
        try:
            input1 = self.Gquery.text()
            if len(input1) == 0:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Zero Input Error")
                msg.setInformativeText("Type something to search")
                msg.setWindowTitle('Error')
                msg.exec_()
            else:
                lsd=" "
                url="https://www.google.com/search?q="+input1+"&start=1&sa=N&ved=2ahUKEwi7_fTxvcPrAhUy6XMBHahXAuc4ChDy0wN6BAgLEC8&biw=1600&bih=757"
                r=requests.get(url)
                soup=BeautifulSoup(r.content,'html5lib')
                f=soup.find(id="main")
                for i in range(1,len(f)-1):
                    try:
                        g=f.find_all(class_='ZINbbc xpd O9g5cc uUPGi')[i]
                        desc=g.find(class_="BNeawe vvjwJb AP7Wnd").getText()
                        desc2=g.find(class_="BNeawe s3v9rd AP7Wnd").getText()
                        
                        try:
                            u=g.find('a')['href']
                            x=u.split('&')[0].split('?q=')[1]
                            lsd=lsd+"\n"+desc+"\n"+desc2+"\n"+x+"\n"+"__________________"+"\n"
                            
                        except:
                            u=g.find('a')['href']
                            x=u.split('&')[0]
                            gh={"url":x,"desc":desc,"desc2":desc2}
                            l=l+[gh]
                            lsd=lsd+"\n"+desc+"\n"+desc2+"\n"+x+"\n"+"__________________"+"\n"
                            
                    except:
                        print(" ")
                self.Gres.append(str(lsd))
        except:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Error")
            msg.setInformativeText("An error occured")
            msg.setWindowTitle('Error')
            msg.exec_()

    def retranslateUi(self, Google):
        _translate = QtCore.QCoreApplication.translate
        Google.setWindowTitle(_translate("Google", "Google"))
        self.google.setText(_translate("Google", "Google Search"))
        self.Gquery.setText(_translate("Google", ""))
        self.Gquery.setPlaceholderText(_translate("Google", "                        Search here"))
        self.Ggo.setText(_translate("Google", "GO"))
        

# main app
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Google = QtWidgets.QMainWindow()
    ui = Ui_Google()
    ui.setupUi(Google)
    Google.show()
    sys.exit(app.exec_())