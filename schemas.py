from pydantic import BaseModel, EmailStr
from datetime import datetime

class ClassBase(BaseModel):
    name: str
    date_time: datetime
    instructor: str
    available_slots: int

class ClassResponse(ClassBase):
    id: int

    model_config = {
        "from_attributes": True
    }

class BookingRequest(BaseModel):
    class_id: int
    client_name: str
    client_email: EmailStr

class BookingResponse(BaseModel):
    class_id: int
    client_email: EmailStr
    client_name: str
