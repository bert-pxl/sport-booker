import os
import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget,QStackedWidget

class SelectSportScreen(QDialog):
    def __init__(self):
        super(SelectSportScreen, self).__init__()
        current_dir = os.path.dirname(__file__)
        ui_file = os.path.join(current_dir, "select_sport_screen.ui")
        loadUi(ui_file,self)
        # self.padel.clicked.connect(self.gotoA)

# MAIN
        
if __name__ == "__main__":

    app = QApplication(sys.argv)
    sportscreen=SelectSportScreen()
    widget = QStackedWidget()
    widget.addWidget(sportscreen)
    widget.setFixedHeight(600)
    widget.setFixedWidth(900)
    widget.show()
    try:
        sys.exit(app.exec_())
    except:
        print("Exiting due to exception:")