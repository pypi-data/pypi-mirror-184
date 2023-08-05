
from datetime import date, datetime, time
from decimal import Decimal
from enum import Enum
from typing import List, Optional, Dict
from uuid import UUID

from pydantic import BaseModel


class AuditRecord(BaseModel):
    pass


class ProvenanceRecord(BaseModel):
    sourceName: Optional[str] = None
    sourceId: Optional[str] = None
    auditRecord: Optional[AuditRecord] = None
