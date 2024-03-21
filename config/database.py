import os
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

sqlite_database = "../database.sqlite"
base_dir = os.path.dirname(os.path.realpath(__file__))

databse_url = f"sqlite:///{os.path.join(base_dir,sqlite_database)}"

engine = create_engine(databse_url,echo=True)

Session = sessionmaker(bind=engine)

Base = declarative_base()