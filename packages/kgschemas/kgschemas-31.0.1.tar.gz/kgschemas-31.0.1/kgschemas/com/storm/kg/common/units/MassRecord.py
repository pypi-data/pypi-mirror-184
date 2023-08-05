
from datetime import date, datetime, time
from decimal import Decimal
from enum import Enum
from typing import List, Optional, Dict
from uuid import UUID

from pydantic import BaseModel


class MassUnits(str, Enum):
    kg = "kg"
    t = "t"
    g = "g"


class MassRecord(BaseModel):
    value: float
    unit: MassUnits
