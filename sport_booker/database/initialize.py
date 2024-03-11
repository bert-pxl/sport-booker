from database import ENGINE, LOCAL_SESSION
from logs import LOGGER
from models.models import Base, Sport, Pricing, Location, Field


def initialize_db():
    LOGGER.info("Creating database ....")
    Base.metadata.create_all(ENGINE)
    LOGGER.info('Database created.')


def create_dummy_data():
    db = LOCAL_SESSION()

    s1 = Sport("Tennis", "Standaard tennis")
    s2 = Sport("Squash", "Kleine tennis")
    s3 = Sport("Padel", "Nieuwe tennis")

    db.add(s1)
    db.add(s2)
    db.add(s3)
    db.commit()

    p1 = Pricing(10,5)
    p2 = Pricing(20,12)
    p3 = Pricing(40, 25)

    db.add(p1)
    db.add(p2)
    db.add(p3)
    db.commit()

    l1 = Location("Eerste Locatie","Placeholder voor de eerste locatie","adres van deze locatie","123456789", "email")
    db.add(l1)
    db.commit()

    f1 = Field("veld 1", l1.id, s1.id,p1.id)
    f2 = Field("veld 2", l1.id, s2.id, p2.id)
    f3 = Field("veld 3", l1.id, s3.id, p3.id)

    db.add(f1)
    db.add(f2)
    db.add(f3)
    db.commit()
