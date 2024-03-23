from sport_booker.logs import logger
from sport_booker.database import database_manager as db


def main():
    db_manager = db.DatabaseManager()
    logger.info("start application")
    while True:
        print("\nMenu:")
        print("1. Create database")
        print("2. Initialize data in database")
        print("3. Drop database")
        print("99. Close connection")

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
        elif choice == "99":
            db_manager.close_connection()
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
