from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine('postgres://jlhugqod:IBsRppzzcEkEy7jClBTXjx4S4_UkSiYx@mouse.db.elephantsql.com/jlhugqod')
db_session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()