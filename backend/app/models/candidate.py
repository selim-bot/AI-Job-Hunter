from sqlalchemy import JSON, Column, Integer, String

from app.database.connection import Base


class Candidate(Base):
    __tablename__ = "candidates"

    id = Column(Integer, primary_key=True)
    full_name = Column(String)
    email = Column(String)
    education = Column(String)
    resume_path = Column(String)
    skills = Column(JSON, default=list)
    preferred_roles = Column(JSON, default=list)
    preferred_locations = Column(JSON, default=list)
