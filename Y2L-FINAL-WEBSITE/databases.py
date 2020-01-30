from model import Base, User

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///users.db?check_same_thread=False')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()


def register_user(first_name, last_name, username, email, password):
	new_user = User(
		first_name = first_name,
		last_name = last_name,
		username = username,
		email = email
		)
	new_user.hash_password(password)
	session.add(new_user)
	session.commit()

def get_user(username):
	return session.query(User).filter_by(username = username).first()

def get_all_users():
	return session.query(User).all()

