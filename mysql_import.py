from sqlalchemy import Column, Integer, Float, Date, String, VARCHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import csv
import pandas as pd
import os
import warnings

#To ignore warnings from already existing mock database
warnings.filterwarnings('ignore')

Base = declarative_base()

class customers(Base):
    #Tell SQLAlchemy what the table name is and if there's any table-specific arguments it should know about
    __tablename__ = 'customers'

    #tell SQLAlchemy the name of column and its attributes: 
    first_name = Column(VARCHAR(30))
    last_name = Column(VARCHAR(30))
    email = Column(VARCHAR(40))
    income = Column(Integer)
    ip_address = Column(VARCHAR(30))
    Id = Column(Integer, primary_key=True, nullable=False, autoincrement=False)

def sql_import(path, verbose=False):
    #Create Mysql database if not exists

    engine = create_engine('mysql+pymysql://root:password@localhost:3307')
    conn = engine.connect()
    conn.execute("commit")
    conn.execute("create database if not exists mock")
    conn.close()

    #Import csv to Mysql
    engine = create_engine('mysql+pymysql://root:password@localhost:3307/mock')
    Base.metadata.create_all(engine)
    path_to_csv = path
    df = pd.read_csv(path_to_csv)
    df.to_sql(con=engine, name='customers', if_exists='replace')