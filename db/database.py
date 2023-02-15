import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

db_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'database.db')

engine = create_engine(f'sqlite:///{db_file_path}')

Session = sessionmaker(bind=engine)
