from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import Base, Book, User, Status

engine = create_engine("sqlite:///library.db", echo=True)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
