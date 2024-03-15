
from logs import logger
from database import database_manager as db


def main():
    db_manager = db.DatabaseManager()
    logger.info("start application")
    while True:
        print("\nMenu:")
        print("1. Create database")
        print("2. Initialize data in database")
        print("3. Drop database")
        print("4. Show Pricing")
        print("5. Show Locations")
        print("6. Get Location by id 1")
        print("7. Show Facilites for sport id 1")
        print("8. Show Sports")
        print("9. Show Sports by location id 1")
        print("10. Show Prices")
        print("20. Close connection")

        choice = input("Enter your choice: ")

        if choice == "1":
            db_manager.create_database()
            print("Database created successfully!")
        elif choice == "2":
            db_manager.initialize_database_with_dummy_data()
            print("Data initialized successfully!")
        elif choice == "3":
            db_manager.drop_database()
            print("Database dropped successfully!")
        elif choice == "4":
            print(db_manager.get_prices())
        elif choice == "5":
            print(db_manager.get_locations())
        elif choice == "6":
            print(db_manager.get_location_by_id(1))
        elif choice == "7":
            print(db_manager.get_facilities_by_sport_id(1))
        elif choice == "8":
            print(db_manager.get_sports())
        elif choice == "9":
            print(db_manager.get_sports_by_location_id(1))
        elif choice == "10":
            print(db_manager.get_prices())
        elif choice == "20":
            db_manager.close_connection()
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
