
from datetime import date, datetime, time
from decimal import Decimal
from enum import Enum
from typing import List, Optional, Dict
from uuid import UUID

from pydantic import BaseModel


class LengthUnits(str, Enum):
    m = "m"
    km = "km"
    cm = "cm"


class LengthRecord(BaseModel):
    value: float
    unit: LengthUnits
