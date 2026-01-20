from sqlalchemy import Column, Integer, ForeignKey, DateTime, Boolean
from sqlalchemy.sql import func
from database import Base

class UserLibrary(Base):
    __tablename__ = "user_library"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    subject_id = Column(Integer, ForeignKey("subjects.id", ondelete="CASCADE"))
    added_at = Column(DateTime(timezone=True), server_default=func.now())
    is_synced = Column(Boolean, default=True)
