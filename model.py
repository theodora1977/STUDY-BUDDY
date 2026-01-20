from sqlalchemy import Column, Integer, String, Boolean, DateTime
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=True)
    email = Column(String, unique=True, index=True, nullable=True)
    phone = Column(String, unique=True, index=True, nullable=True)
    exam_type = Column(String)
    is_verified = Column(Boolean, default=False)

class OTP(Base):
    __tablename__ = "otps"

    id = Column(Integer, primary_key=True, index=True)
    identifier = Column(String, nullable=False)  # email or phone
    code = Column(String, nullable=False)
    expires_at = Column(DateTime, nullable=False)
    is_used = Column(Boolean, default=False)

# generate otp for user verification
import random
from datetime import datetime, timedelta

def generate_otp():
    return str(random.randint(100000, 999999))

def otp_expiry():
    return datetime.utcnow() + timedelta(minutes=5)
