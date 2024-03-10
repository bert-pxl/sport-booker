import database
from logs import LOGGER
from sqlalchemy import create_engine, exc
import models


def create_db_if_not_exists():
    try:
        engine = create_engine(database.CONNECTION_STRING)
        with engine.connect():
            models.Base.metadata.create_all(engine)
            LOGGER.info('Database initialized.')
    except exc.OperationalError as e:
        if 'no such database' in str(e):  # Check if the error indicates that the database doesn't exist
            LOGGER.info('Database does not exist. Creating now.')
        else:
            LOGGER.error('An error occurred:', e)


if __name__ == "__main__":
    create_db_if_not_exists()

