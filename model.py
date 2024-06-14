from sqlalchemy import Column, Integer, String, ForeignKey, Date ,create_engine
from sqlalchemy.orm import declarative_base, relationship




Base = declarative_base()

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key = True, index= True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    # year_of_publish = Column(datetime, nullable=False)
    copies = Column(Integer, default= 1)
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
    borrowed_date = Column(Date)
    returned_date = Column(Date)
    book = relationship('Book')
    user = relationship('User')

