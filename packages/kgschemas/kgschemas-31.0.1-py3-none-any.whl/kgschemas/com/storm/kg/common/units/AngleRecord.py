
from datetime import date, datetime, time
from decimal import Decimal
from enum import Enum
from typing import List, Optional, Dict
from uuid import UUID

from pydantic import BaseModel


class AngleUnits(str, Enum):
    deg = "deg"
    rad = "rad"


class AngleRecord(BaseModel):
    value: float
    unit: AngleUnits
