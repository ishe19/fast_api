from pydantic import BaseModel
from pydantic.datetime_parse import date, datetime
# from pydantic.schema import List
from typing import List

from pydantic.schema import Optional
from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, func, JSON, Table, Boolean, DECIMAL
from sqlalchemy.orm import relationship

from database.db import Base, engine


class User(Base):
    __tablename__ = 'users'
    __versioned__ = {}
    id = Column(Integer, primary_key=True, autoincrement=True)
    firstName = Column('first_name', String(64))
    lastName = Column('last_name', String(64))
    dob = Column('dob', DateTime)
    # created_on = Column('created_on', DateTime(timezone=True), server_default=func.now())
    # updated_on = Column('updated_on', DateTime(timezone=True), onupdate=func.now())
    phoneNumber = Column('phonenumber', String(32), nullable=False)
    nationality = Column('nationality', String(64))
    password = Column('password', String(64))
    email = Column('email', String(32))

    def __init__(self, firstName, lastName, dob, phoneNumber, email, password, nationality):
        self.email = email
        self.phoneNumber = phoneNumber
        self.dob = dob
        self.firstName = firstName
        self.lastName = lastName
        self.nationality = nationality
        self.password = password


class Pydantic_user(BaseModel):
    firstName: str
    lastName: str
    dob: date
    phoneNumber: str
    nationality: str
    email: str
    password: str

class Pydantic_login(BaseModel):
    email: str
    password: str


Base.metadata.create_all(engine)

