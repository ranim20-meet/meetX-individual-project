from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from passlib.apps import custom_app_context as pwd_security


Base = declarative_base()

class User(Base):
	__tablename__ = "users"
	id = Column(Integer, primary_key = True)
	first_name = Column(String)
	last_name = Column(String)
	email = Column(String)
	username = Column(String)
	password_hash = Column(String)

	def hash_password(self, password):
		self.password_hash = pwd_security.encrypt(password)

	def verify_password(self, password):
		return pwd_security.verify(password, self.password_hash)

	def __repr__(self):
		return ("first_name: {}\n"
				"last_name: {}\n"
				"email: {}\n"
				"username: {}\n"
				).format(
					self.first_name,
					self.last_name,
					self.email,
					self.username)