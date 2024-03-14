from sport_booker.logs import logger
from sport_booker.models import models as models

import json
import pathlib
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DatabaseManager:

    def __init__(self):
        logger.info('Loading database configuration')
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

    def show_locations(self):
        return self.session().query(models.Location).all()

    def show_fields(self):
        return self.session().query(models.Facility).all()

    def show_pricing(self):
        return self.session().query(models.Price).all()

    def show_sports(self):
        return self.session().query(models.Sport).all()

    def create_database(self):
        models.Base.metadata.create_all(self.engine)

    def initialize_database_with_dummy_data(self):

        db = self.session()

        s1 = models.Sport("Tennis", "kleine gele bal")
        s2 = models.Sport("Squash", "hele kleine zwarte bal")
        s3 = models.Sport("Padel", "kleine rode bal")
        s4 = models.Sport("Voetbal", "medium zwart witte bal")
        s5 = models.Sport("Volleybal", "medium gekleurde bal")
        s6 = models.Sport("Basketbal", "grote orange bal")

        db.add(s1)
        db.add(s2)
        db.add(s3)
        db.add(s4)
        db.add(s5)
        db.add(s6)
        db.commit()

        p1 = models.Price("leden prijs", 5)
        p2 = models.Price("niet leden prijs", 12)
        p3 = models.Price("vriendenprijs", 25)

        db.add(p1)
        db.add(p2)
        db.add(p3)
        db.commit()

        l1 = models.Location("Eerste Locatie", "Placeholder voor de eerste locatie", "adres van deze locatie",
                             "123456789",
                             "email")
        db.add(l1)
        db.commit()

        f1 = models.Facility("veld 1", l1.id,[s1, s3], [p1,p2,p3])
        f2 = models.Facility("veld 2", l1.id,[s2, s3], [p1,p2,p3])
        f3 = models.Facility("veld 3", l1.id, [s1, s2], [p1,p2,p3])

        db.add_all([f1,f2,f3])
        db.commit()

    def drop_database(self):
        models.Base.metadata.drop_all(self.engine)

    def close_connection(self):
        self.session().close()
