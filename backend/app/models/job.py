from sqlalchemy import Column, DateTime, Float, Integer, String, Text

from app.database.connection import Base


class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True)
    job_title = Column(String)
    company = Column(String)
    location = Column(String)
    job_description = Column(Text)
    experience = Column(String)
    source = Column(String)
    apply_url = Column(String)
    match_score = Column(Float)
    posted_at = Column(DateTime)
