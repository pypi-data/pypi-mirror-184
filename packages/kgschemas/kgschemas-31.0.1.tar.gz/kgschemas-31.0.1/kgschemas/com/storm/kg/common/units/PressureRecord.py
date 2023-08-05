
from datetime import date, datetime, time
from decimal import Decimal
from enum import Enum
from typing import List, Optional, Dict
from uuid import UUID

from pydantic import BaseModel


class PressureUnits(str, Enum):
    bar = "bar"
    Pa = "Pa"
    kPa = "kPa"
    MPa = "MPa"
    mbar = "mbar"


class PressureRecord(BaseModel):
    value: float
    unit: PressureUnits
