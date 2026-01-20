from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base

class Topic(Base):
    __tablename__ = "topics"

    id = Column(Integer, primary_key=True)
    subject_id = Column(Integer, ForeignKey("subjects.id", ondelete="CASCADE"))
    title = Column(String, nullable=False)
