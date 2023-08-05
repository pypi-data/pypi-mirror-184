
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


class LengthUnits(str, Enum):
    m = "m"
    km = "km"
    cm = "cm"


class LengthRecord(BaseModel):
    value: float
    unit: LengthUnits


class GeofenceTypes(str, Enum):
    UNKNOWN = "UNKNOWN"
    SAFETYZONE = "SAFETYZONE"
    BOUNDARY = "BOUNDARY"


class Geofence(BaseModel):
    metadata: MetadataRecord
    id: str
    name: str
    buffer: Optional[LengthRecord] = None
    type: GeofenceTypes
