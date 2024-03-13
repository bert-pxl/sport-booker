from logs.logger import LOGGER
from models.models import Base, Location, Sport, Pricing, Field
import json
import pathlib
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DatabaseManager:

    def __init__(self):
        LOGGER.info('Loading database configuration')
        self.engine = create_engine(self.load_config(), echo=True)
        self.session = sessionmaker(bind=self.engine)

    def load_config(self, file_name: str = 'database-config.json'):
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
                        LOGGER.error("Incomplete MySQL configuration. Required fields: host, user, passwd, db")
                elif 'sqlite' in config:
                    sqlite_config = config['sqlite']
                    if 'file' in sqlite_config:
                        return f'sqlite:///{sqlite_config["file"]}'
                    else:
                        LOGGER.error("SQLITE configuration not found in the provided configuration file.")
                else:
                    LOGGER.error("MySQL configuration not found in the provided configuration file.")

        except FileNotFoundError:
            LOGGER.error(f"The file '{file_name}' was not found in the same directory as the script.")
            return None

    def show_locations(self):
        return self.session().query(Location).all()

    def show_fields(self):
        return self.session().query(Field).all()

    def show_pricing(self):
        return self.session().query(Pricing).all()

    def show_sports(self):
        return self.session().query(Sport).all()

    def create_database(self):
        Base.metadata.create_all(self.engine)

    def initialize_database_with_dummy_data(self):

        db = self.session()

        s1 = Sport("Tennis", "Standaard tennis")
        s2 = Sport("Squash", "Kleine tennis")
        s3 = Sport("Padel", "Nieuwe tennis")

        db.add(s1)
        db.add(s2)
        db.add(s3)
        db.commit()

        p1 = Pricing(10, 5)
        p2 = Pricing(20, 12)
        p3 = Pricing(40, 25)

        db.add(p1)
        db.add(p2)
        db.add(p3)
        db.commit()

        l1 = Location("Eerste Locatie", "Placeholder voor de eerste locatie", "adres van deze locatie", "123456789",
                      "email")
        db.add(l1)
        db.commit()

        f1 = Field("veld 1", l1.id, s1.id, p1.id)
        f2 = Field("veld 2", l1.id, s2.id, p2.id)
        f3 = Field("veld 3", l1.id, s3.id, p3.id)

        db.add(f1)
        db.add(f2)
        db.add(f3)
        db.commit()

    def drop_database(self):
        Base.metadata.drop_all(self.engine)

    def close_connection(self):
        self.session().close()
