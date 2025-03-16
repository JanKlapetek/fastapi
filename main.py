from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from database import SessionLocal, SensorData, init_db

app = FastAPI()

# Povolení requestů zvenčí (např. z Raspberry Pi)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Inicializace DB
init_db()

# Dependency pro získání session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Endpoint pro přidání dat
@app.post('/sensor/')
def add_sensor_data(sensor_name: str, temperature: float, humidity: float, db: Session = Depends(get_db)):
    new_data = SensorData(sensor_name=sensor_name, temperature=temperature, humidity=humidity)
    db.add(new_data)
    db.commit()
    return {'message': 'Data uložena'}

# Endpoint pro získání všech dat
@app.get('/sensor/')
def get_sensor_data(db: Session = Depends(get_db)):
    return db.query(SensorData).all()