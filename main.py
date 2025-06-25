from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from database import Base, engine, SessionLocal
import models, schemas
from datetime import datetime
from utils import convert_utc_to_ist
import logging

logging.basicConfig(level=logging.INFO)
app = FastAPI()
Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/classes", response_model=list[schemas.ClassResponse])
def get_classes(db: Session = Depends(get_db)):
    classes = db.query(models.FitnessClass).all()
    for c in classes:
        c.date_time = convert_utc_to_ist(c.date_time)
    return classes

@app.post("/book", response_model=schemas.BookingResponse)
def book_class(request: schemas.BookingRequest, db: Session = Depends(get_db)):
    class_obj = db.query(models.FitnessClass).filter(models.FitnessClass.id == request.class_id).first()
    if not class_obj:
        raise HTTPException(status_code=404, detail="Class not found")
    if class_obj.available_slots <= 0:
        raise HTTPException(status_code=400, detail="No slots available")

    class_obj.available_slots -= 1
    booking = models.Booking(**request.dict())
    db.add(booking)
    db.commit()
    db.refresh(booking)
    logging.info(f"Booking made: {booking.client_name} for class {booking.class_id}")
    return booking

@app.get("/bookings", response_model=list[schemas.BookingResponse])
def get_bookings(email: str = Query(...), db: Session = Depends(get_db)):
    bookings = db.query(models.Booking).filter(models.Booking.client_email == email).all()
    return bookings
