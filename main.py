from fastapi import FastAPI, Depends, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from database import engine, Base, SessionLocal
from model import User
from subject import Subject
from topic import Topic
from question import Question
from progress import UserProgress
from library import UserLibrary
from app.otp import router as otp_router
from app.protectroutes import get_current_user
from app.email_config import email_config, EmailConfig, fm
from pydantic import BaseModel
import os

class ProgressUpdate(BaseModel):
    topic_id: int
    correct: bool

app = FastAPI()

app.include_router(otp_router)

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Admin endpoints for configuration
@app.get("/admin/config")
def get_email_config():
    """Get current email configuration (without password)"""
    return {
        "mail_username": email_config.mail_username,
        "mail_from": email_config.mail_from,
        "mail_port": email_config.mail_port,
        "mail_server": email_config.mail_server,
        "mail_tls": email_config.mail_tls,
        "mail_ssl": email_config.mail_ssl,
        "is_configured": bool(email_config.mail_username and email_config.mail_password)
    }

@app.post("/admin/config/email")
def update_email_config(config: EmailConfig):
    """Update email configuration"""
    from app.email_config import email_config, fm, get_mail_config, FastMail
    # Update global config
    email_config.__dict__.update(config.__dict__)
    # Reinitialize FastMail with new config
    import app.email_config
    app.email_config.fm = FastMail(get_mail_config())
    return {"message": "Email configuration updated successfully"}

@app.get("/")
def root():
    return {"message": "Study Buddy backend running"}

@app.get("/subjects")
def get_subjects(db: Session = Depends(get_db)):
    return db.query(Subject).all()

@app.get("/subjects/{subject_id}/topics")
def get_topics(subject_id: int, db: Session = Depends(get_db)):
    return db.query(Topic).filter(Topic.subject_id == subject_id).all()

@app.get("/topics/{topic_id}/questions")
def get_questions(topic_id: int, shuffle: bool = False, limit: int = 20, db: Session = Depends(get_db)):
    questions = db.query(Question).filter(Question.topic_id == topic_id).all()
    
    if shuffle:
        import random
        random.shuffle(questions)
    
    return questions[:limit]

@app.post("/progress")
def update_progress(data: ProgressUpdate, user_id: int = Depends(get_current_user), db: Session = Depends(get_db)):
    try:
        progress = db.query(UserProgress).filter(UserProgress.user_id == user_id, UserProgress.topic_id == data.topic_id).first()
        if not progress:
            progress = UserProgress(
                user_id=user_id, 
                topic_id=data.topic_id,
                attempts=0,
                correct=0,
                accuracy=0.0
            )
            db.add(progress)
            db.flush()
        
        progress.attempts += 1
        if data.correct:
            progress.correct += 1
        progress.accuracy = progress.correct / progress.attempts
        db.commit()
        return {"message": "Progress updated", "success": True}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error updating progress: {str(e)}")

@app.get("/progress")
def get_progress(user_id: int = Depends(get_current_user), db: Session = Depends(get_db)):
    return db.query(UserProgress).filter(UserProgress.user_id == user_id).all()

# This must be after all other API routes
# It serves the built React app (the 'assets' directory)
if os.path.exists("frontend/dist/assets"):
    app.mount("/assets", StaticFiles(directory="frontend/dist/assets"), name="assets")

@app.get("/{catchall:path}")
async def serve_spa(catchall: str):
    """Serves the single-page app for any path not caught by an API endpoint."""
    index_path = "frontend/dist/index.html"
    if not os.path.exists(index_path):
        raise HTTPException(status_code=404, detail="Frontend not built. Run 'npm run build' in the 'frontend' directory.")
    return FileResponse(index_path)
