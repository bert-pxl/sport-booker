import os
import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget,QStackedWidget,QTableWidgetItem

# --------------------------------------------STARTSCREEN-----------------------------------------------------------
class Startscreen(QDialog):
    def __init__(self):
        super(Startscreen, self).__init__()
        current_dir = os.path.dirname(__file__)
        ui_file = os.path.join(current_dir, "startscreen.ui")
        try:
            loadUi(ui_file, self)
        except Exception as e:
            print("Error loading UI:", e)

        # volgende 
        self.start_button_reservation.clicked.connect(self.gotoLocationscreen)

    def gotoLocationscreen(self):
        locationscreen=Locationscreen()
        widget.addWidget(locationscreen)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
# ---------------------------------------------------------------------------------------------------------------------

# --------------------------------------------LOCATIONSCREEN-----------------------------------------------------------
class Locationscreen(QDialog):
    def __init__(self):
        super(Locationscreen, self).__init__()
        current_dir = os.path.dirname(__file__)
        ui_file = os.path.join(current_dir, "locationscreen.ui")
        try:
            loadUi(ui_file, self)
        except Exception as e:
            print("Error loading UI:", e)

        # vorige 
        self.location_button_previous.clicked.connect(self.gotoStartscreen)

        # volgende 
        self.location_button_next.clicked.connect(self.gotoSportscreen)

    def gotoStartscreen(self):
        widget.setCurrentIndex(widget.currentIndex()-1)

    def gotoSportscreen(self):
        sportscreen=Sportscreen()
        widget.addWidget(sportscreen)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
# ---------------------------------------------------------------------------------------------------------------------

# --------------------------------------------SPORTSCREEN--------------------------------------------------------------
class Sportscreen(QDialog):
    def __init__(self):
        super(Sportscreen, self).__init__()
        current_dir = os.path.dirname(__file__)
        ui_file = os.path.join(current_dir, "sportscreen.ui")
        try:
            loadUi(ui_file, self)
        except Exception as e:
            print("Error loading UI:", e)

        # vorige 
        self.sport_button_previous.clicked.connect(self.gotoLocationscreen)

        # volgende
        self.sport_button_next.clicked.connect(self.gotoDatescreen)

    def gotoLocationscreen(self):
        widget.setCurrentIndex(widget.currentIndex()-1)

    def gotoDatescreen(self):
        datescreen=Datescreen()
        widget.addWidget(datescreen)
        widget.setCurrentIndex(widget.currentIndex()+1)


# ---------------------------------------------------------------------------------------------------------------------

# --------------------------------------------DATESCREEN--------------------------------------------------------------
class Datescreen(QDialog):
    def __init__(self):
        super(Datescreen, self).__init__()
        current_dir = os.path.dirname(__file__)
        ui_file = os.path.join(current_dir, "datescreen.ui")
        try:
            loadUi(ui_file, self)
        except Exception as e:
            print("Error loading UI:", e)

        # vorige 
        self.date_button_previous.clicked.connect(self.gotoSportscreenback)

        # volgende 
        self.date_button_next.clicked.connect(self.gotoFacilityscreen)

        # Datum
        self.date_calendar.clicked.connect(self.showDate)

    def gotoSportscreenback(self):
        widget.setCurrentIndex(widget.currentIndex()-1)

    def gotoFacilityscreen(self):
        facilityscreen=Facilityscreen()
        widget.addWidget(facilityscreen)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def showDate(self, date):
        self.date_label.setText(date.toString())

# ---------------------------------------------------------------------------------------------------------------------

# --------------------------------------------FACILITYSCREEN--------------------------------------------------------------
class Facilityscreen(QDialog):
    def __init__(self):
        super(Facilityscreen, self).__init__()
        current_dir = os.path.dirname(__file__)
        ui_file = os.path.join(current_dir, "facilityscreen.ui")
        try:
            loadUi(ui_file, self)
        except Exception as e:
            print("Error loading UI:", e)

        # TableWidget
        for i in range(14):    
            self.facility_tableWidget.setColumnWidth(i,50)
        
        #load data
            
        self.loaddata()

        # vorige 
        self.facility_button_previous.clicked.connect(self.gotoDatescreenback)

        # volgende 
        self.facility_button_next.clicked.connect(self.gotoReservationscreen)

    def gotoDatescreenback(self):
        widget.setCurrentIndex(widget.currentIndex()-1)

    def gotoReservationscreen(self):
        reservationscreen=Reservationscreen()
        widget.addWidget(reservationscreen)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def loaddata(self):
        facility_names= ["veld1","veld2"]
        facility_lijst=[{"name":"veld1","tijdstip":"19u-20u","availability":"vrij"},
                   {"name":"veld2","tijdstip":"9u-10u","availability":"vrij"}
                   ]
        # self.facility_tableWidget.setRowCount(len(facility_names))  # Set the number of rows

        # for row,facility in enumerate(facility_names):
        #     self.facility_tableWidget.setItem(row,0,QtWidgets.QTableWidgetItem(facility))

        self.facility_tableWidget.setRowCount(len(facility_names))  # Set the number of rows
        
        for row, facility in enumerate(facility_names):
            self.facility_tableWidget.setItem(row, 0, QTableWidgetItem(facility)) # Set name of rows

        for item in facility_lijst:

            facility_name = item["name"]
            time_slot = item["tijdstip"]
            availability = item["availability"]

            facility_index = facility_names.index(facility_name)  # Find the index of the facility

            # Determine the column index based on the time slot
        
            column_index = None
            if item["tijdstip"] == "9u-10u":
                column_index = 1
            elif item["tijdstip"] == "10u-11u":
                column_index = 2
            elif item["tijdstip"] == "11u-12u":
                column_index = 3
            elif item["tijdstip"] == "13u-14u":
                column_index = 4
            elif item["tijdstip"] == "14u-15u":
                column_index = 5
            elif item["tijdstip"] == "15u-16u":
                column_index = 6
            elif item["tijdstip"] == "16u-17u":
                column_index = 7    
            elif item["tijdstip"] == "17u-18u":
                column_index = 8
            elif item["tijdstip"] == "18u-19u":
                column_index = 9
            elif item["tijdstip"] == "19u-20u":
                column_index = 10
            elif item["tijdstip"] == "20u-21u":
                column_index = 11
            elif item["tijdstip"] == "21u-22u":
                column_index = 12

            # Set availability item if column index is valid
            if column_index is not None:
                self.facility_tableWidget.setItem(facility_index, column_index, QTableWidgetItem(availability))

# ---------------------------------------------------------------------------------------------------------------------

# --------------------------------------------RESERVATIONSCREEN--------------------------------------------------------
class Reservationscreen(QDialog):
    def __init__(self):
        super(Reservationscreen, self).__init__()
        current_dir = os.path.dirname(__file__)
        ui_file = os.path.join(current_dir, "reservationscreen.ui")
        try:
            loadUi(ui_file, self)
        except Exception as e:
            print("Error loading UI:", e)

        # vorige 
        self.reservation_button_previous.clicked.connect(self.gotoFacilityscreenback)

        # volgende 
        self.reservation_button_next.clicked.connect(self.gotoConfirmreservationscreen)

    def gotoFacilityscreenback(self):
        widget.setCurrentIndex(widget.currentIndex()-1)

    def gotoConfirmreservationscreen(self):
        confirmreservationscreen=Confirmreservationscreen()
        widget.addWidget(confirmreservationscreen)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
# ---------------------------------------------------------------------------------------------------------------------

# --------------------------------------------CONFIRMRESERVATIONSCREEN-------------------------------------------------
class Confirmreservationscreen(QDialog):
    def __init__(self):
        super(Confirmreservationscreen, self).__init__()
        current_dir = os.path.dirname(__file__)
        ui_file = os.path.join(current_dir, "confirmreservationscreen.ui")
        try:
            loadUi(ui_file, self)
        except Exception as e:
            print("Error loading UI:", e)

        # vorige 
        self.confirmreservation_button_previous.clicked.connect(self.gotoReservationscreenback)

        # volgende 
        self.confirmreservation_button_next.clicked.connect(self.gotoStartscreenback)

    def gotoReservationscreenback(self):
        widget.setCurrentIndex(widget.currentIndex()-1)

    def gotoStartscreenback(self):
        startscreen=Startscreen()
        widget.addWidget(startscreen)
        widget.setCurrentIndex(widget.currentIndex()+1)
        


# MAIN
        
if __name__ == "__main__":

    app = QApplication(sys.argv)
    widget = QStackedWidget()
    startscreen=Startscreen()
    widget = QStackedWidget()
    widget.addWidget(startscreen)   
    widget.setFixedHeight(600)
    widget.setFixedWidth(900)
    widget.show()
    try:
        sys.exit(app.exec_())
    except:
        print("Exiting due to exception:")