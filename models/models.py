from datetime import datetime

from sqlalchemy import Column, Integer, String, Date, Text, ForeignKey
from sqlalchemy.orm import relationship, DeclarativeBase

import hashlib

from db.database import engine


class Base(DeclarativeBase):
    pass


class UserLocation(Base):
    __tablename__ = 'user_location'

    user_id = Column(String, primary_key=True)
    lat = Column(String)
    lon = Column(String)
