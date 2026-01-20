from sqlalchemy import Column, Integer, String, ForeignKey, JSON
from database import Base

class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True)
    topic_id = Column(Integer, ForeignKey("topics.id", ondelete="CASCADE"))
    question = Column(String, nullable=False)
    options = Column(JSON)  # {"A": "...", "B": "..."}
    correct_answer = Column(String)
    explanation = Column(String)
