
from datetime import date, datetime, time
from decimal import Decimal
from enum import Enum
from typing import List, Optional, Dict
from uuid import UUID

from pydantic import BaseModel


class VoltUnits(str, Enum):
    kV = "kV"
    MV = "MV"
    mV = "mV"


class VoltRecord(BaseModel):
    value: float
    unit: VoltUnits
