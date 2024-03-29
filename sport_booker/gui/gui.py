import os
import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget,QStackedWidget,QTableWidgetItem
from PyQt5.QtGui import QPixmap

import tmp
# --------------------------------------------GET DATA--------------------------------------------------------------

locatie_lijst = tmp.get_location_data()

# --------------------------------------------SHARED STATE--------------------------------------------------------------

# Define StateManager class to hold shared data
class StateManager:
    def __init__(self):
        self.locatie_keuze = None
        self.sport_keuze = None
        self.datum_keuze = None
        self.facility_and_slot_time_keuze = None


# --------------------------------------------STARTSCREEN-----------------------------------------------------------
class Startscreen(QDialog):
    def __init__(self,state_manager):
        super(Startscreen, self).__init__()
        current_dir = os.path.dirname(__file__)
        ui_file = os.path.join(current_dir, "startscreen.ui")
        try:
            loadUi(ui_file, self)
        except Exception as e:
            print("Error loading UI:", e)

        self.state_manager = state_manager

        # volgende 
        self.start_button_reservation.clicked.connect(self.gotoLocationscreen)

    def gotoLocationscreen(self):
        locationscreen=Locationscreen(self.state_manager)
        widget.addWidget(locationscreen)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
# ---------------------------------------------------------------------------------------------------------------------

# --------------------------------------------LOCATIONSCREEN-----------------------------------------------------------
class Locationscreen(QDialog):
    locatie_lijst = tmp.get_location_data()

    def __init__(self, state_manager):
        super(Locationscreen, self).__init__()
        current_dir = os.path.dirname(__file__)
        ui_file = os.path.join(current_dir, "locationscreen.ui")
        try:
            loadUi(ui_file, self)
        except Exception as e:
            print("Error loading UI:", e)

        self.state_manager = state_manager

        # Initialize locatie_keuze as None
        self.locatie_keuze = None

        #get path to image file/ create pixmap object from the image/ set the pixmap to the label/scale to fit
        image_path = os.path.join(current_dir, "..","image", "T2sports.png")
        pixmap = QPixmap(image_path)
        self.location_label_image.setPixmap(pixmap)                           
        self.location_label_image.setScaledContents(True) # Ensure the image scales to fit the label

        # vorige 
        self.location_button_previous.clicked.connect(self.gotoStartscreen)

        # volgende 
        self.location_button_next.clicked.connect(self.gotoSportscreen)

        # location_button  
        self.location_button_1.clicked.connect(lambda: self.gotoLocationpicker(self.location_button_1.text()))
        self.location_button_2.clicked.connect(lambda: self.gotoLocationpicker(self.location_button_2.text()))
        self.location_button_3.clicked.connect(lambda: self.gotoLocationpicker(self.location_button_3.text()))

    def gotoStartscreen(self):
        widget.setCurrentIndex(widget.currentIndex()-1)

    def gotoSportscreen(self):
        sportscreen=Sportscreen(self.state_manager)
        widget.addWidget(sportscreen)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def gotoLocationpicker(self,button_name):
        for location in self.locatie_lijst:
            if location['name'] == button_name:
                location_info = f"Naam: {location['name']}\nAdres: {location['address']}\nTelefoon: {location['phone']}\nEmail: {location['email']}"
                self.location_label_info.setText(location_info)   
                self.state_manager.locatie_keuze = location["name"]
  
    

    
# ---------------------------------------------------------------------------------------------------------------------

# --------------------------------------------SPORTSCREEN--------------------------------------------------------------
class Sportscreen(QDialog):

    # Get the current directory of the script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Define image paths relative to the script directory
    image_paths = {
        "Snooker": os.path.join(script_dir, "..","image", "snooker.jpg"),
        "Pool": os.path.join(script_dir, "..","image", "pool.jpg"),
        "Darts": os.path.join(script_dir, "..","image", "darts.jpg"),
        "Tennis": os.path.join(script_dir, "..","image", "tennis.jpg"),
        "Padel": os.path.join(script_dir, "..","image", "padel.jpg"),
        "Squash": os.path.join(script_dir, "..","image", "squash.jpg"),
    }

    def __init__(self, state_manager):
        super(Sportscreen, self).__init__()
        current_dir = os.path.dirname(__file__)
        ui_file = os.path.join(current_dir, "sportscreen.ui")
        try:
            loadUi(ui_file, self)
        except Exception as e:
            print("Error loading UI:", e)

        self.state_manager = state_manager

        # Initialize Sport_keuze as None
        self.sport_keuze = None

        # vorige 
        self.sport_button_previous.clicked.connect(self.gotoLocationscreen)

        # volgende
        self.sport_button_next.clicked.connect(self.gotoDatescreen)

        # sport_button
        self.sport_button_snooker.clicked.connect(lambda: self.gotoSportimage(self.sport_button_snooker.text()))
        self.sport_button_pool.clicked.connect(lambda: self.gotoSportimage(self.sport_button_pool.text()))
        self.sport_button_darts.clicked.connect(lambda: self.gotoSportimage(self.sport_button_darts.text()))
        self.sport_button_tennis.clicked.connect(lambda: self.gotoSportimage(self.sport_button_tennis.text()))
        self.sport_button_padel.clicked.connect(lambda: self.gotoSportimage(self.sport_button_padel.text()))
        self.sport_button_squash.clicked.connect(lambda: self.gotoSportimage(self.sport_button_squash.text()))


    def gotoLocationscreen(self):
        widget.setCurrentIndex(widget.currentIndex()-1)

    def gotoDatescreen(self):
        datescreen=Datescreen(self.state_manager)
        widget.addWidget(datescreen)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def gotoSportimage(self,button_name):

        image_path = self.image_paths.get(button_name)
        if image_path:
            pixmap = QPixmap(image_path)
            if not pixmap.isNull():
                self.sport_label_image.setPixmap(pixmap)                           
                self.sport_label_image.setScaledContents(True) # Ensure the image scales to fit the label
                self.state_manager.sport_keuze = button_name
            else:
                self.sport_label_image.setText("Failed to load image")
        else:
            self.sport_label_image.setText("No image path found for this button")



# ---------------------------------------------------------------------------------------------------------------------

# --------------------------------------------DATESCREEN--------------------------------------------------------------
class Datescreen(QDialog):
    def __init__(self,state_manager):
        super(Datescreen, self).__init__()
        current_dir = os.path.dirname(__file__)
        ui_file = os.path.join(current_dir, "datescreen.ui")
        try:
            loadUi(ui_file, self)
        except Exception as e:
            print("Error loading UI:", e)

        self.state_manager = state_manager

        # vorige 
        self.date_button_previous.clicked.connect(self.gotoSportscreenback)

        # volgende 
        self.date_button_next.clicked.connect(self.gotoFacilityscreen)

        # Datum
        self.date_calendar.clicked.connect(self.showDate)

    def gotoSportscreenback(self):
        widget.setCurrentIndex(widget.currentIndex()-1)

    def gotoFacilityscreen(self):
        facilityscreen=Facilityscreen(self.state_manager)
        widget.addWidget(facilityscreen)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def showDate(self, date):
        self.date_label.setText(date.toString())
        self.state_manager.datum_keuze = self.date_label.text()

       

# ---------------------------------------------------------------------------------------------------------------------

# --------------------------------------------FACILITYSCREEN--------------------------------------------------------------
class Facilityscreen(QDialog):
    def __init__(self,state_manager):
        super(Facilityscreen, self).__init__()
        current_dir = os.path.dirname(__file__)
        ui_file = os.path.join(current_dir, "facilityscreen.ui")
        try:
            loadUi(ui_file, self)
        except Exception as e:
            print("Error loading UI:", e)

        self.state_manager = state_manager

        # TableWidget
        for i in range(14):    
            self.facility_tableWidget.setColumnWidth(i,50)
        
        #load data
            
        self.loaddata()

        # vorige 
        self.facility_button_previous.clicked.connect(self.gotoDatescreenback)

        # volgende 
        self.facility_button_next.clicked.connect(self.gotoReservationscreen)

        # Facility/time choise
        self.facility_tableWidget.cellClicked.connect(self.storeSelectedFacilityAndTimeSlot)

    def gotoDatescreenback(self):
        widget.setCurrentIndex(widget.currentIndex()-1)

    def gotoReservationscreen(self):
        reservationscreen=Reservationscreen(self.state_manager)
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

    def storeSelectedFacilityAndTimeSlot(self, row, column):
        # Get the facility name from the clicked row
        facility_item = self.facility_tableWidget.item(row, 0)
        if facility_item is not None:
            self.selected_facility = facility_item.text()

        # Get the time slot from the header of the clicked column
        time_slot_header = self.facility_tableWidget.horizontalHeaderItem(column)
        if time_slot_header is not None:
            self.selected_time_slot = time_slot_header.text()
        self.selected_facility_and_slot_time = []
        self.selected_facility_and_slot_time.append((self.selected_facility,self.selected_time_slot))
        self.state_manager.facility_and_slot_time_keuze = self.selected_facility_and_slot_time

# ---------------------------------------------------------------------------------------------------------------------

# --------------------------------------------RESERVATIONSCREEN--------------------------------------------------------
class Reservationscreen(QDialog):
    def __init__(self,state_manager):
        super(Reservationscreen, self).__init__()
        current_dir = os.path.dirname(__file__)
        ui_file = os.path.join(current_dir, "reservationscreen.ui")
        try:
            loadUi(ui_file, self)
        except Exception as e:
            print("Error loading UI:", e)

        self.state_manager = state_manager

        # vorige 
        self.reservation_button_previous.clicked.connect(self.gotoFacilityscreenback)

        # volgende 
        self.reservation_button_next.clicked.connect(self.gotoConfirmreservationscreen)

    def gotoFacilityscreenback(self):
        widget.setCurrentIndex(widget.currentIndex()-1)

    def gotoConfirmreservationscreen(self):
        confirmreservationscreen=Confirmreservationscreen(self.state_manager)
        widget.addWidget(confirmreservationscreen)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
# ---------------------------------------------------------------------------------------------------------------------

# --------------------------------------------CONFIRMRESERVATIONSCREEN-------------------------------------------------
class Confirmreservationscreen(QDialog):
    def __init__(self,state_manager):
        super(Confirmreservationscreen, self).__init__()
        current_dir = os.path.dirname(__file__)
        ui_file = os.path.join(current_dir, "confirmreservationscreen.ui")
        try:
            loadUi(ui_file, self)
        except Exception as e:
            print("Error loading UI:", e)

        self.state_manager = state_manager

        # Set summary
  
        self.confirmreservation_label_summary.setText(f"{self.state_manager.locatie_keuze}\n"
                                                      f"{self.state_manager.sport_keuze}\n"
                                                      f"{self.state_manager.datum_keuze}\n"
                                                      f"{self.state_manager.facility_and_slot_time_keuze}")

        # vorige 
        self.confirmreservation_button_previous.clicked.connect(self.gotoReservationscreenback)

        # volgende 
        self.confirmreservation_button_next.clicked.connect(self.gotoStartscreenback)

    def gotoReservationscreenback(self):
        widget.setCurrentIndex(widget.currentIndex()-1)

    def gotoStartscreenback(self):
        startscreen=Startscreen(self.state_manager)
        widget.addWidget(startscreen)
        widget.setCurrentIndex(widget.currentIndex()+1)
        


# MAIN
        
if __name__ == "__main__":

    app = QApplication(sys.argv)
    widget = QStackedWidget()
    state_manager = StateManager()
    startscreen=Startscreen(state_manager)
    widget = QStackedWidget()
    widget.addWidget(startscreen)   
    widget.setFixedHeight(600)
    widget.setFixedWidth(900)
    widget.show()
    try:
        sys.exit(app.exec_())
    except:
        print("Exiting due to exception:")