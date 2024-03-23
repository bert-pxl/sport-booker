from sport_booker.logs import logger
from sport_booker.models import models as models

import json
import pathlib
from sqlalchemy import create_engine, select, join, alias
from sqlalchemy.orm import sessionmaker, aliased
from sqlalchemy.exc import SQLAlchemyError


class DatabaseManager:
    def __init__(self):
        logger.debug('Initializing database manager')
        self.engine = create_engine(self.load_config(), echo=False)
        self.session = sessionmaker(bind=self.engine)

    def load_config(self, file_name: str = 'database-config.json'):
        logger.debug('Loading configuration')
        try:
            database_dir = pathlib.Path(__file__).resolve().parent
            config_file = database_dir / file_name

            with config_file.open(mode='r') as f_in:
                config = json.load(f_in)
                if 'mysql' in config:
                    mysql_config = config['mysql']
                    if all(key in mysql_config for key in ['host', 'user', 'passwd', 'db']):
                        return (f'mysql://{mysql_config["user"]}:{mysql_config["passwd"]}@{mysql_config["host"]}/'
                                f'{mysql_config["db"]}')
                    else:
                        logger.error("Incomplete MySQL configuration. Required fields: host, user, passwd, db")
                elif 'sqlite' in config:
                    sqlite_config = config['sqlite']
                    if 'file' in sqlite_config:
                        return f'sqlite:///{sqlite_config["file"]}'
                    else:
                        logger.error("SQLITE configuration not found in the provided configuration file.")
                else:
                    logger.error("MySQL configuration not found in the provided configuration file.")

        except FileNotFoundError:
            logger.error(f"The file '{file_name}' was not found in the same directory as the script.")
            return None

    def get_locations(self):
        logger.debug('Getting all locations')
        try:
            return self.session().execute(select(models.Location.id, models.Location.name)
                                          .order_by(models.Location.name)).all()
        except SQLAlchemyError as e:
            logger.error(f"An error occurred while fetching locations: {e}")
            return None

    def get_location_by_id(self, location_id: int):
        logger.debug('Getting one location')
        try:
            return self.session().scalars(select(models.Location)
                                          .where(models.Location.id == location_id).limit(1)).first()
        except SQLAlchemyError as e:
            logger.error(f"An error occurred while fetching location with ID {location_id}: {e}")
            return None


    def get_facilities(self):
        logger.debug('Getting all facilities')
        try:
            return self.session().execute(select(models.Facility)).all()
        except SQLAlchemyError as e:
            logger.error(f"An error occurred while fetching facilities: {e}")
            return None

    def get_facilities_by_sport_id(self, sport_id: int):
        logger.debug('Getting facilities by sport')
        try:
            return self.session().scalars(select(models.Facility)
                                          .where(models.Facility.sports.any(models.Sport.id == sport_id))).all()
        except SQLAlchemyError as e:
            logger.error(f"An error occurred while fetching facilities by sport with ID {sport_id}: {e}")
            return None

    def get_reservations(self):
        logger.debug('Getting all reservations')
        try:
            return self.session().execute(select(models.Reservation)).all()
        except SQLAlchemyError as e:
            logger.error(f"An error occurred while fetching reservations: {e}")
            return None

    def get_prices(self):
        logger.debug('Getting all prices')
        try:
            return self.session().execute(select(models.Price.id, models.Price.name, models.Price.price)).all()
        except SQLAlchemyError as e:
            logger.error(f"An error occurred while fetching prices: {e}")
            return None

    def get_sports(self):
        logger.debug('Getting all sports')
        try:
            return self.session().scalars(select(models.Sport)).all()
        except SQLAlchemyError as e:
            logger.error(f"An error occurred while fetching sports: {e}")
            return None

    def get_sports_by_location_id(self, location_id: int):
        logger.debug('Getting all possible sports by location id')
        try:
            stmt = (
                select(models.Sport)
                .select_from(join(models.Sport, models.facility_sport))
                .join(aliased(models.facility_sport))
                .where(models.Facility.location_id == location_id)
                .distinct()
            )
            return self.session().scalars(stmt).all()
        except SQLAlchemyError as e:
            logger.error(f"An error occurred while fetching sports by location {location_id}: {e}")
            return None

    def make_reservation(self, customer, reservation_date, reservation_start, reservation_end, facility_id):
        logger.debug('Creating a new reseration')
        db = self.session()
        try:
            reservation = models.Reservation(customer, reservation_date, reservation_start, reservation_end,
                                             facility_id)
            db.add(reservation)
            db.commit()
        except SQLAlchemyError as e:
            logger.error(f"An error occurred trying to create the reservation: {e}")
            return None

    def create_database(self):
        logger.debug('Creating Tables for the Database')
        try:
            models.Base.metadata.create_all(self.engine)
        except SQLAlchemyError as e:
            logger.error(f"An error occurred trying to create the database: {e}")
            return None

    def initialize_database_with_dummy_data(self):
        logger.debug('Initializing dummy data for the database')
        try:
            db = self.session()

            s1 = models.Sport("Tennis", "kleine gele bal")
            s2 = models.Sport("Squash", "hele kleine zwarte bal")
            s3 = models.Sport("Padel", "kleine rode bal")
            s4 = models.Sport("Voetbal", "medium zwart witte bal")
            s5 = models.Sport("Volleybal", "medium gekleurde bal")
            s6 = models.Sport("Basketbal", "grote orange bal")

            db.add_all([s1, s2, s3, s4, s5, s6])
            logger.debug('\tCreating Sports data Database')
            db.commit()

            p1 = models.Price("leden prijs", 5)
            p2 = models.Price("niet leden prijs", 12)
            p3 = models.Price("vriendenprijs", 25)

            db.add_all([p1, p2, p3])
            logger.debug('\tCreating Prices data Database')
            db.commit()

            l1 = models.Location("Eerste Locatie", "Placeholder voor de eerste locatie", "adres van deze locatie",
                                 "123456789",
                                 "email")
            db.add(l1)
            logger.debug('\tCreating Location data Database')
            db.commit()

            f1 = models.Facility("veld 1", l1.id, [s1, s3], [p1, p2, p3])
            f2 = models.Facility("veld 2", l1.id, [s2, s3], [p1, p2, p3])
            f3 = models.Facility("veld 3", l1.id, [s1, s2], [p1, p2, p3])

            db.add_all([f1, f2, f3])
            logger.debug('\tCreating Facility data Database')
            db.commit()

        except SQLAlchemyError as e:
            logger.error(f"An error occurred while initializing dummy data: {e}")
            return None

    def drop_database(self):
        logger.debug('Dropping Database')
        try:
            models.Base.metadata.drop_all(self.engine)
        except SQLAlchemyError as e:
            logger.error(f"An error occurred while dropping the database: {e}")
        return None

    def close_connection(self):
        logger.debug('Closing connection')
        try:
            self.session().close()
        except SQLAlchemyError as e:
            logger.error(f"An error occurred while closing the connection to the database: {e}")
        return None
