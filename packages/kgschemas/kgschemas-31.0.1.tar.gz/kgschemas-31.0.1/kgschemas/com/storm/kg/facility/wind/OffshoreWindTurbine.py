
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


class OffshoreHeightReferences(str, Enum):
    LAT = "LAT"
    MSL = "MSL"
    SEABED = "SEABED"
    TOTAL = "TOTAL"


class HubHeightRecord(BaseModel):
    height: LengthRecord
    reference: OffshoreHeightReferences


class OffshoreWindTurbine(BaseModel):
    metadata: MetadataRecord
    id: str
    name: str
    shortName: Optional[str] = None
    originalEngineeringCode: Optional[str] = None
    commissionedDate: Optional[str] = None
    hubHeight: Optional[HubHeightRecord] = None
