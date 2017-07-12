from sqlalchemy import Column, Integer, Float, Date, String, VARCHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import csv
import pandas as pd
import os

Base = declarative_base()

class customers(Base):
    #Tell SQLAlchemy what the table name is and if there's any table-specific arguments it should know about
    __tablename__ = 'customers'

    #tell SQLAlchemy the name of column and its attributes: 
    first_name = Column(VARCHAR)
    last_name = Column(VARCHAR)
    email = Column(VARCHAR)
    income = Column(Integer)
    ip_address = Column(VARCHAR)
    id = Column(Integer, primary_key=True, nullable=False)

#Create Postgres database if not exists

engine = create_engine('postgresql+psycopg2://postgres:password@localhost:5433')
conn = engine.connect()
conn.execute("commit")

value = conn.execute("select count(*) from pg_catalog.pg_database where datname = 'mock' ;").fetchone()
if value[0] == 1:
    print "db already exists"
else: 
    print "creating new db"
    conn.execute("create database if not exists mock")
conn.close()

#Import csv to Postgres
engine = create_engine('postgresql+psycopg2://postgres:password@localhost:5433/mock')
Base.metadata.create_all(engine)
path_to_csv = os.path.join(os.path.abspath('../shared-data'),'mock_data_10000_rows_utf8.csv')
df = pd.read_csv(path_to_csv)
df.to_sql(con=engine, index_label='id', name=customers.__tablename__, if_exists='replace')