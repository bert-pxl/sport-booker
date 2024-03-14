
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
        print("6. Show Fields")
        print("7. Show Sports")
        print("8. Close connection")

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
            print(db_manager.show_pricing())
        elif choice == "5":
            print(db_manager.show_locations())
        elif choice == "6":
            print(db_manager.show_fields())
        elif choice == "7":
            print(db_manager.show_sports())
        elif choice == "8":
            db_manager.close_connection()
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
