from database import session
from model import User

def add_user(name, email):
    new_user = User(name=name, email=email)
    session.add(new_user)
    session.commit()

def get_all_user():
    return session.query(User).all()

def delete_user(user_id):
    user = session.query(User).filter_by(id=user_id).first()
    if user:
        session.delete(user)
        session.commit()