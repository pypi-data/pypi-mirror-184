
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


class UnitlessUnits(str, Enum):
    integerCategorical = "integerCategorical"
    unitlessMeasurement = "unitlessMeasurement"


class UnitlessRecord(BaseModel):
    value: float
    unit: UnitlessUnits


class FoundationFatigueDesignLife(BaseModel):
    metadata: MetadataRecord
    id: str
    name: str
    elevationLAT: LengthRecord
    pilingDamage: UnitlessRecord
