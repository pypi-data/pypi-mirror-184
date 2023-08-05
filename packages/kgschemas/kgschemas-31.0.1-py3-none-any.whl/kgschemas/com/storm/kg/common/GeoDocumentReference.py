
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


class ResolutionType(str, Enum):
    LOWRES = "LOWRES"
    HIGHRES = "HIGHRES"


class GeoDocumentReference(BaseModel):
    metadata: MetadataRecord
    id: str
    name: Optional[str] = None
    dataStoreId: str
    resolutionType: Optional[ResolutionType] = None
