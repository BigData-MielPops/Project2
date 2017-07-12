'''from odo import odo
import os

path_to_csv = os.path.join(os.path.abspath('shared-data'),'mock_data_10000_rows.csv')
if os.path.exists(path_to_csv):
    print 'path exists'
    odo(path_to_csv, 'postgresql://postgres:password@localhost:5433/postgres::customers')
else: print 'path doesnt exist'
    '''
from numpy import genfromtxt
from time import time
from datetime import datetime
from sqlalchemy import Column, Integer, Float, Date, String, VARCHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import csv
import pandas as pd


#def Load_Data(file_name):
    #data = csv.reader(file_name, delimiter=',')# skiprows=1, converters={0: lambda s: str(s)})
    #return data.tolist()

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

engine = create_engine('postgresql+psycopg2://postgres:password@localhost:5433/postgres::customers')
Base.metadata.create_all(engine)
path_to_csv = os.path.join(os.path.abspath('shared-data'),'mock_data_10000_rows.csv')
df = pd.read_csv(path_to_csv)
df.to_sql(con=engine, index_label='id', name=customers.__tablename__, if_exists='replace')