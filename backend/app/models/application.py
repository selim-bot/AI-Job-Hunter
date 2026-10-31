from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text

from app.database.connection import Base

STATUSES = [
    "Discovered", "Shortlisted", "Draft Prepared", "Awaiting Approval",
    "Applied", "Assessment", "Interview", "Rejected", "Offer Received",
]


class Application(Base):
    __tablename__ = "applications"

    id = Column(Integer, primary_key=True)
    candidate_id = Column(Integer, ForeignKey("candidates.id"))
    job_id = Column(Integer, ForeignKey("jobs.id"))
    status = Column(String, default="Discovered")
    application_date = Column(DateTime)
    approval_status = Column(String, default="Pending")
    notes = Column(Text)
