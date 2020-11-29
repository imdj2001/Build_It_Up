from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from bs4 import BeautifulSoup
import requests


# main function
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MyDoctorApp = QtWidgets.QMainWindow()
    ui = Ui_MyDoctorApp()
    ui.setupUi(MyDoctorApp)
    MyDoctorApp.show()
    sys.exit(app.exec_())