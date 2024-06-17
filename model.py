from sqlalchemy import Column, Integer, String, ForeignKey, Date ,create_engine
from sqlalchemy.orm import declarative_base, relationship
from datetime import date




Base = declarative_base()
class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key = True, index= True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    # year_of_publish = Column(datetime, nullable=False)
    copies = Column(Integer )
    # availability = Column(Boolean, default=True)

# class Student(Base):
#     __table_name__ = "students"

#     id = Column(Integer, primary_key= True, index= True)
#     name = Column(String, nullable=False)
#     email = Column(String, nullable=False)

# class Librarian(Base):
#     __table_name__ = "librarians"

#     id = Column(Integer, primary_key= True, index= True)
#     name = Column(String, nullable=False)
#     email = Column(String, nullable=False)

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key= True, index= True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
   
class Status(Base):
    __tablename__= "statuses"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    book_id = Column(Integer, ForeignKey('books.id'))
    borrowed_date = Column(Date, default=date.today)
    returned_date = Column(Date, nullable=True)
    book = relationship('Book')
    user = relationship('User')

    def __init__(self, book_id, user_id, status_date=None):
        self.book_id = book_id
        self.user_id = user_id
        self.status_date = status_date if status_date else date.today()

