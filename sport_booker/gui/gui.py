import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget,QStackedWidget

class Select_sport_screen(QDialog):
    def __init__(self):
        super(Select_sport_screen, self).__init__()
        loadUi("select_sport_screen.ui",self)

# MAIN

app = QApplication(sys.argv)
sportscreen=Select_sport_screen()
widget = QStackedWidget()
widget.addWidget(sportscreen)
widget.setFixedHeight(600)
widget.setFixedWidth(900)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting due to exception:")