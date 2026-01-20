from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from model import User, OTP, generate_otp, otp_expiry
from .JWTtoken import create_access_token
from datetime import datetime
from fastapi_mail import FastMail, MessageSchema
from pydantic import BaseModel, EmailStr
from .email_config import fm, email_config

router = APIRouter()

class SendOTPRequest(BaseModel):
    identifier: str

class VerifyOTPRequest(BaseModel):
    identifier: str
    code: str

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/auth/send-otp")
async def send_otp(request: SendOTPRequest, db: Session = Depends(get_db)):
    identifier = request.identifier
    # Validate email format
    if "@" not in identifier:
        raise HTTPException(status_code=400, detail="Please provide a valid email address")

    # Generate OTP
    otp_code = generate_otp()
    expiry = otp_expiry()

    # Store OTP in database
    otp = OTP(identifier=identifier, code=otp_code, expires_at=expiry)
    db.add(otp)
    db.commit()

    # Check if email is configured
    if not email_config.mail_username or not email_config.mail_password or fm is None:
        # Return OTP directly for testing when email is not configured
        return {"message": "OTP generated (email not configured)", "otp": otp_code}

    # Send email
    message = MessageSchema(
        subject="Your OTP Code - Study Buddy",
        recipients=[identifier],
        body=f"""Hello!

Your OTP code for Study Buddy is: {otp_code}

This code will expire in 5 minutes.

If you didn't request this code, please ignore this email.

Best regards,
Study Buddy Team""",
        subtype="plain"
    )

    try:
        await fm.send_message(message)
        return {"message": "OTP sent to your email"}
    except Exception as e:
        # If email fails, still allow verification with the code (for testing)
        return {"message": f"Failed to send email ({str(e)}). OTP generated for testing.", "otp": otp_code}

@router.post("/auth/verify-otp")
def verify_otp(request: VerifyOTPRequest, db: Session = Depends(get_db)):
    identifier = request.identifier
    code = request.code
    otp = db.query(OTP).filter(
        OTP.identifier == identifier,
        OTP.code == code,
        OTP.is_used == False
    ).first()

    if not otp:
        raise HTTPException(status_code=400, detail="Invalid OTP")

    if otp.expires_at < datetime.utcnow():
        raise HTTPException(status_code=400, detail="OTP expired")

    otp.is_used = True

    user = db.query(User).filter(
        (User.email == identifier) | (User.phone == identifier)
    ).first()

    if not user:
        user = User(
            email=identifier if "@" in identifier else None,
            phone=identifier if "@" not in identifier else None,
            is_verified=True
        )
        db.add(user)

    user.is_verified = True
    db.commit()

    # Create JWT token
    access_token = create_access_token(data={"user_id": user.id})

    return {
        "message": "Login successful",
        "access_token": access_token,
        "token_type": "bearer"
    }
