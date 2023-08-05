
from datetime import date, datetime, time
from decimal import Decimal
from enum import Enum
from typing import List, Optional, Dict
from uuid import UUID

from pydantic import BaseModel


class ComplianceRecord(BaseModel):
    pass


class AuditRecord(BaseModel):
    pass


class ProvenanceRecord(BaseModel):
    sourceName: Optional[str] = None
    sourceId: Optional[str] = None
    auditRecord: Optional[AuditRecord] = None


class TransformationRecord(BaseModel):
    pass


class MetadataRecord(BaseModel):
    complianceRecord: Optional[ComplianceRecord] = None
    provenanceRecord: Optional[ProvenanceRecord] = None
    transformationRecord: Optional[TransformationRecord] = None


class VelocityUnits(str, Enum):
    mps = "mps"
    kn = "kn"


class VelocityRecord(BaseModel):
    value: float
    unit: VelocityUnits


class Vessel(BaseModel):
    metadata: MetadataRecord
    id: str
    name: Optional[str] = None
    trackActive: bool = False
    yearBuilt: Optional[int] = None
    vesselType: Optional[str] = None
    imo: Optional[int] = None
    mmsi: int
    callSign: Optional[str] = None
    capacityCrew: Optional[int] = None
    capacityPassengers: Optional[int] = None
    cabins: Optional[int] = None
    maxSpeed: Optional[VelocityRecord] = None
