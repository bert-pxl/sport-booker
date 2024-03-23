from sport_booker.logs import logger
from sport_booker.database import database_manager as db
from datetime import datetime


def main():
    db_manager = db.DatabaseManager()
    logger.info("start application")
    while True:
        print("\nMenu:")
        print("1. Show all reservations")
        print("2. Show all locations")
        print("3. Show all facilities")
        print("4. Show Pricing")
        print("5. Show Sports")
        print("6. Show Prices")
        print("10. Get location")
        print("11. Get Facilities by sport")
        print("12. Get sports by location")
        print("21. Make a reservation")
        print("99. Close connection")

        choice = input("Enter your choice: ")

        if choice == "1":
            print(db_manager.get_reservations())
        elif choice == "2":
            print(db_manager.get_locations())
        elif choice == "3":
            print(db_manager.get_facilities())
        elif choice == "4":
            print(db_manager.get_prices())
        elif choice == "5":
            print(db_manager.get_sports())
        elif choice == "6":
            print(db_manager.get_prices())
        elif choice == "10":
            location_id = int(input("Input the location id: "))
            print(db_manager.get_location_by_id(location_id))
        elif choice == "11":
            sport_id = int(input("Input the sport id: "))
            print(db_manager.get_facilities_by_sport_id(sport_id))
        elif choice == "12":
            location_id = int(input("Input the location id: "))
            print(db_manager.get_sports_by_location_id(location_id))
        elif choice == "21":
            location_id = int(input("Input the location id: "))
            print(db_manager.get_sports_by_location_id(location_id))
            sport_id = int(input("Input the sport id: "))
            print(db_manager.get_facilities_by_sport_id(sport_id))
            facility_id = int(input("Input the facility id: "))
            reservation_date_str = input("Input the date (YYYY-MM-DD): ")
            reservation_date = datetime.strptime(reservation_date_str, "%Y-%m-%d")
            reservation_start_str = input("Input the start time (HH:MM): ")
            reservation_start = datetime.strptime(reservation_start_str, "%H:%M")
            reservation_end_str = input("Input the end time (HH:MM): ")
            reservation_end = datetime.strptime(reservation_end_str, "%H:%M")
            name = input("Input the name : ")
            db_manager.make_reservation(name, reservation_date, reservation_start, reservation_end, facility_id)
        elif choice == "99":
            db_manager.close_connection()
            print("Exiting...")
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
