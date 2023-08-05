
from datetime import date, datetime, time
from decimal import Decimal
from enum import Enum
from typing import List, Optional, Dict
from uuid import UUID

from pydantic import BaseModel


class VelocityUnits(str, Enum):
    mps = "mps"
    kn = "kn"


class VelocityRecord(BaseModel):
    value: float
    unit: VelocityUnits
