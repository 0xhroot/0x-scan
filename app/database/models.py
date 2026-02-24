from sqlalchemy import (
    Column,
    String,
    DateTime,
    Integer,
    JSON,
    ForeignKey
)
from sqlalchemy.orm import relationship
from datetime import datetime
import uuid

from app.database.session import Base


def generate_id():
    return str(uuid.uuid4())


class Target(Base):
    __tablename__ = "targets"

    id = Column(String, primary_key=True, default=generate_id)
    target = Column(String, unique=True, nullable=False)
    description = Column(String)
    tags = Column(JSON)

    created_at = Column(DateTime, default=datetime.utcnow)

    scans = relationship("Scan", back_populates="target")


class Scan(Base):
    __tablename__ = "scans"

    id = Column(String, primary_key=True, default=generate_id)
    target_id = Column(String, ForeignKey("targets.id"))
    status = Column(String, default="pending")

    created_at = Column(DateTime, default=datetime.utcnow)

    target = relationship("Target", back_populates="scans")
    results = relationship("Result", back_populates="scan")


class Result(Base):
    __tablename__ = "results"

    id = Column(String, primary_key=True, default=generate_id)
    scan_id = Column(String, ForeignKey("scans.id"))

    data = Column(JSON)
    severity = Column(String, default="info")

    created_at = Column(DateTime, default=datetime.utcnow)

    scan = relationship("Scan", back_populates="results")
