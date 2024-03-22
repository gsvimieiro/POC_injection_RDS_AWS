import pandas as pd
from sqlite3 import Date,Timestamp
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Float, null,Text
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from requests import Request, Session
from datetime import datetime
from pandas import DatetimeTZDtype
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class tb_venda_tesouro(Base):
    __tablename__ = 'tb_tesouro_venda'
    id = Column(Integer, primary_key=True)
    TipoTitulo = Column(String)
    VencimentodoTitulo = Column(String)
    DataVenda = Column(Text)
    PU = Column(Float)
    Quantidade = Column(Float)
    Valor = Column(Float)
   
    def start():
        db_string = "postgresql://postgres:D4t4science.@server-01.csddqd4agbf7.us-east-1.rds.amazonaws.com/db01"
        engine = create_engine(db_string)
        Session = sessionmaker(bind=engine)
        session = Session()
        Base.metadata.create_all(engine)
        print ('\nTable created on database')
        return session, engine
    
    def load_data(table_name, df, session_db, engine_db):
        # load data on database
        try:
            df.to_sql(table_name, engine_db, index=False, if_exists='replace')
            print ('\nData Loaded on Database')
        except Exception as err:
            print(f"\nFail to load data on database: {err}")

        session_db.commit()
        session_db.close()
        print("\nClose database successfully")
        return

# Instancia o objeto
get_session_db, get_engine = tb_venda_tesouro.start()

# Declaration base
Base = declarative_base()

df = pd.read_csv('VendasTesouroDireto.csv', sep=';')
print (df.head())

# call the function to load data on database
tb_venda_tesouro.load_data('tb_tesouro_venda',df, get_session_db, get_engine)