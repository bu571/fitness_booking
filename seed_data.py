from database import SessionLocal, Base, engine
from models import FitnessClass
from datetime import datetime, timedelta
import pytz

# ✅ Create tables before seeding
Base.metadata.create_all(bind=engine)

def seed():
    db = SessionLocal()
    db.query(FitnessClass).delete()  # Optional: clears existing data
    class1 = FitnessClass(
        name="Yoga Morning",
        date_time=datetime.now(pytz.utc) + timedelta(days=1),
        instructor="Anjali",
        available_slots=5
    )
    db.add(class1)
    db.commit()
    db.close()
    print("Seed complete ✅")

if __name__ == "__main__":
    seed()

