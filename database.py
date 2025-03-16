from sqlalchemy import create_engine, Column, Integer, String, Float, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# Získej připojovací údaje z Koyeb
DATABASE_URL='postgresql://koyeb-adm:RmiEvoMz7a3s@ep-white-band-a2h03cgc.eu-central-1.pg.koyeb.app:5432/sensor_data'

# Vytvoření připojení k databázi
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()

class SensorData(Base):
    __tablename__ = "sensor_data"
    id = Column(Integer, primary_key=True, index=True)
    sensor_name = Column(String(50))
    temperature = Column(Float)
    humidity = Column(Float)
    timestamp = Column(TIMESTAMP)

def init_db():
    # Tohle vytvoří tabulky v databázi, pokud ještě neexistují
    Base.metadata.create_all(bind=engine)