from datetime import date
from database import session
from model import Status, Book

def status_book(book_id, user_id):
    book = session.query(Book).filter_by(id=book_id).first()
    if book and book.copies > 0:
        new_status = Status(book_id=book_id, user_id=user_id, status_date=date.today())
        book.copies -= 1
        session.add(new_status)
        session.commit()
    else:
        print("Book not available")


def return_book(status_id):
    status = session.query(Status).filter_by(id=status_id).first()
    if status and status.return_date is None:
        status.return_date = date.today()
        book = session.query(Book).filter_by(id=status.book_id).first()
        book.copies += 1
        session.commit()