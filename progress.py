from sqlalchemy import Column, Integer, ForeignKey, Float, DateTime, Boolean
from sqlalchemy.sql import func
from database import Base

class UserProgress(Base):
    __tablename__ = "user_progress"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    topic_id = Column(Integer, ForeignKey("topics.id", ondelete="CASCADE"))
    attempts = Column(Integer, default=0)
    correct = Column(Integer, default=0)
    accuracy = Column(Float, default=0.0)
    last_updated = Column(DateTime(timezone=True), onupdate=func.now())
    synced = Column(Boolean, default=False)
