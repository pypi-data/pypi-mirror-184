
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


class AssetStates(str, Enum):
    UNKNOWN = "UNKNOWN"
    CONSTRUCTION = "CONSTRUCTION"
    PLANNING = "PLANNING"
    OPERATION = "OPERATION"
    COMMISSIONING = "COMMISSIONING"


class WattUnits(str, Enum):
    MW = "MW"
    kW = "kW"
    GW = "GW"
    W = "W"
    kVAr = "kVAr"
    MVAr = "MVAr"


class WattRecord(BaseModel):
    value: float
    unit: WattUnits


class OffshoreWindFarm(BaseModel):
    metadata: MetadataRecord
    id: str
    name: str
    shortName: Optional[str] = None
    state: AssetStates
    ratedCapacity: Optional[WattRecord] = None
    commercialDateTimeOfOperation: Optional[datetime] = None
