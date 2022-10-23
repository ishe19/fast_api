from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database



url = "mysql+pymysql://root@localhost:3306/interview"


# Create an engine object.
engine = create_engine(url, echo=True)
Base = declarative_base()
# versioning_manager.init(Base)
# Create database if it does not exist.
if not database_exists(engine.url):
    create_database(engine.url)
    # Base.metadata.create_all(engine)
else:
    # Connect the database if exists.
    engine.connect()
Session = sessionmaker(bind=engine)
session = Session()


def get_session():
    return session

# Activity = versioning_manager.activity_cls


