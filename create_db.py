from sqlalchemy import create_engine, Integer, Column, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///database.db')
engine.connect()

Base = declarative_base()

class Data_files(Base):
    __tablename__ = 'data_files'
    chat_id = Column(Integer(), primary_key=True)
    filename = Column(String(), nullable=False)

class Plots(Base):
    __tablename__ = 'plots'
    filename = Column(Integer(), primary_key=True)
    data_filename = Column(String(), ForeignKey('data_files.filename'), nullable=False)

Base.metadata.create_all(engine)