from sqlalchemy import Column, Integer, String, Float
from database import Base

class Subject(Base):
    __tablename__ = "subjects"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    exam_type = Column(String, nullable=False)
    version = Column(Float, default=1.0)  # for updates
